export type Session = {id:string;problemId:number;date:string;mastery:number;lesson:string}
export function validateLocal(value:unknown, ids:number[]):Session[]
export function mergeLocal(existing:Session[], incoming:unknown, ids:number[]):Session[]
export function latestMastery(assessments:{problemId:number;date:string|null;mastery:number|null}[], local:Session[], id:number):number|null
export function reviewPriority(row:{mastery:number|null;submissions:number}):number
