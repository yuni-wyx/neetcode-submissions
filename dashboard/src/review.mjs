export function dayOffset(date,n){const d=new Date(date+'T00:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10)}
export function reviewPlan(rows, sessions, today){
 return rows.map(p=>{
  const last=sessions.filter(s=>s.problemId===p.id&&s.date&&Number.isInteger(s.mastery)&&s.mastery>=1&&s.mastery<=5).sort((a,b)=>a.date.localeCompare(b.date)).at(-1)
  const due=last?dayOffset(last.date,[1,3,7,14,30][last.mastery-1]):null
  const status=due?(due<=today?'due':'later'):(p.submissions||p.practice||p.mastery!==null?'assess':'new')
  return {...p,due,status}
 }).sort((a,b)=>['due','assess','new','later'].indexOf(a.status)-['due','assess','new','later'].indexOf(b.status)||(a.due||'').localeCompare(b.due||'')||a.id-b.id)
}
export function streak(sessions,today){
 const dates=new Set(sessions.filter(s=>s.date&&s.date<=today).map(s=>s.date));let d=dates.has(today)?today:dayOffset(today,-1),n=0
 while(dates.has(d)){n++;d=dayOffset(d,-1)}return n
}
