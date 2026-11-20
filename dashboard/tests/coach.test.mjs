import test from 'node:test'
import assert from 'node:assert/strict'
import {cards,mistakeGroups,quizResult} from '../src/coach.mjs'
import {readFileSync} from 'node:fs'
test('curated cards map to catalog and contain three hints',()=>{const rows=JSON.parse(readFileSync(new URL('../../data/problems.json',import.meta.url)));assert.equal(new Set(cards.map(c=>c.id)).size,cards.length);for(const c of cards){assert.ok(rows.some(r=>r.id===c.id));assert.equal(c.hints.length,3);assert.ok(c.follow&&c.checks.length)}})
test('quiz compares catalog label',()=>{assert.equal(quizResult('Trees','Trees'),true);assert.equal(quizResult('Stack','Trees'),false)})
test('note themes count documents not occurrences',()=>{assert.equal(mistakeGroups([{lesson:'index index'},{lesson:'unrelated'}]).find(x=>x.label==='Boundary / index').count,1)})
