export function validateLocal(value, ids) {
  if (!Array.isArray(value)) throw Error('Expected an array of sessions')
  const seen = new Set()
  return value.map(x => {
    if (!x || typeof x.id !== 'string' || !x.id || seen.has(x.id) || !ids.includes(x.problemId)
      || !Number.isInteger(x.mastery) || x.mastery < 1 || x.mastery > 5
      || typeof x.lesson !== 'string' || x.lesson.length > 2000
      || typeof x.date !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(x.date)
      || !Number.isFinite(Date.parse(x.date)) || new Date(x.date).toISOString().slice(0,10) !== x.date)
      throw Error('Invalid or duplicate practice session')
    seen.add(x.id)
    return {id:x.id,problemId:x.problemId,date:x.date,mastery:x.mastery,lesson:x.lesson}
  })
}
export function mergeLocal(existing, incoming, ids) {
  const merged = new Map(existing.map(x=>[x.id,x]))
  for (const x of validateLocal(incoming,ids)) {
    if (merged.has(x.id) && JSON.stringify(merged.get(x.id)) !== JSON.stringify(x)) throw Error('Conflicting session ID: '+x.id)
    merged.set(x.id,x)
  }
  return [...merged.values()]
}
export function latestMastery(assessments, local, id) {
  const entries = [...assessments,...local].filter(x=>x.problemId===id && Number.isInteger(x.mastery))
  entries.sort((a,b)=>(a.date||'').localeCompare(b.date||''))
  return entries.at(-1)?.mastery ?? null
}
export function reviewPriority(row) {
  if (row.mastery !== null && row.mastery <= 2) return 0
  if (row.mastery === null && row.submissions > 0) return 1
  if (row.mastery === 3) return 2
  return 3
}
