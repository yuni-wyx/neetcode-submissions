"""Refresh tracked submission metadata; never execute submitted code."""
import argparse
import csv
import io
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

TOPIC = "Data Structures & Algorithms"
ROOT = Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode("utf-8").strip()

def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def dump(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"

def classify(rows, aliases, groups):
    owners = {}
    for row in rows:
        for slug in aliases[str(row["id"])]:
            if slug in owners and owners[slug] != row["id"]:
                raise ValueError("Ambiguous alias: " + slug)
            owners[slug] = row["id"]
    mapped = defaultdict(list)
    unknown = []
    for slug in sorted(groups):
        if slug in owners:
            mapped[owners[slug]].append(slug)
        else:
            unknown.append(slug)
    return mapped, unknown

def scan(previous):
    old = {s["path"]: s for p in previous["problems"] for s in p["submissions"]}
    groups = defaultdict(list)
    for entry in git("ls-tree", "-r", "HEAD", "--", TOPIC).splitlines():
        meta, path = entry.split("\t", 1)
        mode, kind, sha = meta.split()
        match = re.fullmatch(re.escape(TOPIC) + r"/([^/]+)/submission-(\d+)\.([a-zA-Z0-9]+)", path)
        if not match or kind != "blob" or mode not in ("100644", "100755"):
            continue
        slug, number, language = match.groups()
        prior = old.get(path)
        if prior and prior["blobSha"] == sha:
            record = prior
        else:
            evidence = git("log", "-1", "--format=%H%x09%aI", "--", path)
            commit, date = evidence.split("\t", 1) if evidence else (None, None)
            record = dict(path=path, language=language, blobSha=sha, syncCommit=commit, syncedAt=date)
        groups[slug].append(record)
    for records in groups.values():
        records.sort(key=lambda x: (int(re.search(r"submission-(\d+)\.", x["path"]).group(1)), x["path"]))
    return groups

def render(rows, aliases, groups, previous):
    mapped, unknown = classify(rows, aliases, groups)
    source = git("log", "-1", "--format=%H%x09%aI", "--", TOPIC)
    commit, date = source.split("\t", 1)
    # Keep the same timestamp representation for an unchanged source commit.
    if previous.get("sourceCommit") == commit:
        date = previous["sourceHeadTimestamp"]
    snap = dict(schemaVersion=1, sourceRepository="yuni-wyx/neetcode-submissions", sourceRef="main",
                sourceCommit=commit, sourceHeadTimestamp=date, uniqueProblems=len(groups),
                submissionCount=sum(map(len, groups.values())),
                problems=[dict(slug=s, submissionCount=len(groups[s]), submissions=groups[s]) for s in sorted(groups)])
    output = {"data/submissions.json": dump(snap)}
    by_folder = defaultdict(list)
    counts = {}
    for row in rows:
        slugs = mapped.get(row["id"], [])
        row["submissionSlug"] = slugs[0] if slugs else None
        counts[row["id"]] = sum(len(groups[s]) for s in slugs)
        by_folder[row["patternFolder"]].append(row)
    output["data/problems.json"] = dump(rows)
    covered = sum(n > 0 for n in counts.values())
    stats = dict(catalogTotal=len(rows), catalogCovered=covered, syncedFiles=snap["submissionCount"],
                 syncedSlugs=len(groups), unmappedSlugs=unknown,
                 categories=[dict(category=rs[0]["category"], total=len(rs), covered=sum(counts[r["id"]] > 0 for r in rs),
                                  submissions=sum(counts[r["id"]] for r in rs)) for rs in by_folder.values()])
    output["data/stats.json"] = dump(stats)
    for folder, rs in by_folder.items():
        path = folder + "/problems.md"
        existing = (ROOT / path).read_text(encoding="utf-8")
        familiarity = {}
        for line in existing.splitlines():
            cells = [cell.strip() for cell in line.split("|")]
            if len(cells) == 7 and cells[1].isdigit():
                familiarity[int(cells[1])] = cells[5]
        lines = [f'# {rs[0]["category"]} — {sum(counts[r["id"]] > 0 for r in rs)}/{len(rs)} synced',
                 "", "Counts reflect synced files, not independent attempts or acceptance. Familiarity is manually assessed.",
                 "", "| LC | Problem | Difficulty | Synced files | Familiarity |", "|---|---|---|---:|---|"]
        for r in rs:
            slugs = mapped.get(r["id"], [])
            links = ", ".join(f'[{len(groups[s])}](../../{quote(TOPIC)}/{quote(s)})' for s in slugs) or "0"
            lines.append(f'| {r["id"]} | [{r["title"]}]({r["url"]}) | {r["difficulty"]} | {links} | {familiarity.get(r["id"], "—")} |')
        output[path] = "\n".join(lines) + "\n"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    start, end = "<!-- tracker-stats:start -->", "<!-- tracker-stats:end -->"
    block = f"{start}\n\n**{covered}/{len(rows)} catalog problems · {snap['submissionCount']} synced files · {len(groups)} synced slugs**\n\n"
    block += "| Category | Covered | Submissions |\n|---|---:|---:|\n"
    block += "\n".join(f'| {x["category"]} | {x["covered"]}/{x["total"]} | {x["submissions"]} |' for x in stats["categories"])
    block += "\n\nUnmapped slugs: " + (", ".join(unknown) or "none") + "\n\n" + end
    if start in readme and end in readme:
        readme = readme.split(start)[0] + block + readme.split(end, 1)[1]
    else:
        readme = re.sub(r"150 catalog problems, 18 categories, .*? at migration\\. ", "", readme)
        readme = readme.rstrip() + "\n\n" + block + "\n"
    output["README.md"] = readme
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = read_json("data/problems.json")
    previous = read_json("data/submissions.json")
    output = render(rows, read_json("data/slug-aliases.json"), scan(previous), previous)
    stale = []
    for path, content in output.items():
        p = ROOT / path
        if not p.exists() or p.read_text(encoding="utf-8") != content:
            stale.append(path)
            if not args.check:
                p.write_text(content, encoding="utf-8")
    print(f"{len(stale)} generated files {'out of date' if args.check else 'updated'}")
    return int(args.check and bool(stale))

if __name__ == "__main__":
    raise SystemExit(main())
