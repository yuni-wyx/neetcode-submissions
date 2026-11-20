import test from 'node:test'
import assert from 'node:assert/strict'
import {dayOffset,reviewPlan,streak} from '../src/review.mjs'
const p={id:1,submissions:1,practice:1,mastery:2}
test('calendar and interval',()=>{assert.equal(dayOffset('2026-02-27',3),'2026-03-02');assert.equal(reviewPlan([p],[{problemId:1,date:'2026-11-16',mastery:2}],'2026-11-19')[0].status,'due')})
test('unknown dates are not invented',()=>assert.equal(reviewPlan([p],[{problemId:1,date:null,mastery:2}],'2026-11-19')[0].status,'assess'))
test('future review is deferred',()=>assert.equal(reviewPlan([p],[{problemId:1,date:'2026-11-19',mastery:5}],'2026-11-19')[0].due,'2026-12-19'))
test('streak counts unique days',()=>assert.equal(streak([{date:'2026-11-18'},{date:'2026-11-18'},{date:'2026-11-17'}],'2026-11-19'),2))
