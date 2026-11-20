export const cards:{id:number;prompt:string;hints:string[];follow:string;checks:string[]}[]
export function mistakeGroups(sessions:{lesson:string}[]):{label:string;count:number}[]
export function quizResult(choice:string,category:string):boolean
