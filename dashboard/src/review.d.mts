type Row={id:number;submissions:number;practice:number;mastery:number|null}
type Evidence={problemId:number;date:string|null;mastery:number|null}
export function dayOffset(date:string,n:number):string
export function reviewPlan<T extends Row>(rows:T[],sessions:Evidence[],today:string):(T&{due:string|null;status:string})[]
export function streak(sessions:{date:string|null}[],today:string):number
