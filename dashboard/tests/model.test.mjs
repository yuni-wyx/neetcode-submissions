import test from 'node:test'
import assert from 'node:assert/strict'
import {validateLocal,mergeLocal,latestMastery,reviewPriority} from '../src/model.mjs'
const a={id:'a',problemId:1,date:'2026-11-19',mastery:3,lesson:'test'}
test('valid session and duplicate import',()=>{assert.deepEqual(mergeLocal([a],[a],[1]),[a])})
test('reject invalid data',()=>{assert.throws(()=>validateLocal([{...a,mastery:9}],[1]));assert.throws(()=>validateLocal([{...a,date:'2026-02-30'}],[1]));assert.throws(()=>validateLocal([a,a],[1]))})
test('reject conflicting session',()=>assert.throws(()=>mergeLocal([a],[{...a,mastery:4}],[1])))
test('latest dated mastery and unknown',()=>{assert.equal(latestMastery([{problemId:1,date:null,mastery:2}],[a],1),3);assert.equal(latestMastery([],[],1),null)})
test('review priority',()=>{assert.equal(reviewPriority({mastery:2,submissions:0}),0);assert.equal(reviewPriority({mastery:null,submissions:1}),1);assert.equal(reviewPriority({mastery:5,submissions:1}),3)})
