/* Pure offline learning and scoring functions. No dependencies. */
(function(root){
  'use strict';
  const LAYERS = [
    {id:'does',label:'What it does',short:'Does',symbol:'✦',verb:'Capabilities'},
    {id:'needs',label:'What it needs',short:'Needs',symbol:'⬡',verb:'Dependencies'},
    {id:'limits',label:'What limits it',short:'Limits',symbol:'△',verb:'Constraints'},
    {id:'affects',label:'Who it affects',short:'Affects',symbol:'◎',verb:'Stakeholders'}
  ];
  const FIELD_LABELS = {
    opportunity:'What could this technology enable in your chosen setting?',
    verify:'What would you investigate before relying on it?',
    caution:'What could go wrong, or what might limit its usefulness?',
    inclusion:'Who benefits, who carries risk, and who might be overlooked?'
  };
  const content=()=>root.TECH_XRAY_CONTENT||{technologies:[],contexts:[]};
  const tech=id=>content().technologies.find(t=>t.id===id);
  const context=id=>content().contexts.find(c=>c.id===id);
  const now=()=>new Date().toISOString();
  const uniqueId=()=>('xr'+Date.now().toString(36)+Math.random().toString(36).slice(2,8));
  function freshAttempt(techId,contextId){
    return {id:uniqueId(),techId,contextId,step:'map',placements:{},priorities:[],reflections:{opportunity:'',verify:'',caution:'',inclusion:''},revealed:false,createdAt:now(),completedAt:null};
  }
  function sortScore(t,a){
    return t.cards.filter(card=>a.placements?.[card.id]===card.layer).length;
  }
  function getGrade(t,a){
    if(!t || !a) return null;
    const correct=sortScore(t,a), mapped=t.cards.filter(c=>LAYERS.some(l=>l.id===a.placements?.[c.id])).length;
    const crit=t.cards.filter(c=>c.critical).map(c=>c.id);
    const chosen=(a.priorities||[]).filter(id=>crit.includes(id)).length;
    const complete=Object.keys(FIELD_LABELS).filter(k=>(a.reflections?.[k]||'').trim().length>=35).length;
    const sorting=Math.round(60*correct/t.cards.length);
    const priorities=5*chosen;
    const reflection=complete===4?25:Math.round(25*complete/4);
    const score=Math.min(100,sorting+priorities+reflection);
    return {score, sorting,priorities,reflection,correct,total:t.cards.length,mapped,chosen,complete,detail:t.cards.map(c=>({id:c.id,text:c.text,layer:c.layer,placed:a.placements?.[c.id]||null,match:a.placements?.[c.id]===c.layer,why:c.why,critical:c.critical})),
      message:score>=85?'Strong exploration — now test your assumptions in a real setting.':score>=65?'A useful first X-Ray. Inspect the mismatches and overlooked dependencies.':'You have uncovered some layers. Use the feedback to trace more of the system.'};
  }
  const allSorted=(t,a)=>!!t&&t.cards.every(c=>LAYERS.some(l=>l.id===a.placements?.[c.id]));
  const keepPriorities=(t,a)=>{a.priorities=(a.priorities||[]).filter(id=>a.placements?.[id]==='needs'&&t.cards.some(c=>c.id===id)).slice(0,3);};
  const safe=(s)=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function asMarkdown(t,ctx,a){
    const grade=getGrade(t,a);
    const lines=[`# Tech X-Ray: ${t.title}`,'',`Setting: ${ctx?.label||'General'}`,`Date: ${a.completedAt||a.createdAt}`,`Practice score: ${grade.score}/100 (sorting ${grade.sorting}/60, priorities ${grade.priorities}/15, reflection ${grade.reflection}/25)`,'',
      'This is formative practice feedback, not verification of factual accuracy or a grade for creativity.',''];
    for(const layer of LAYERS){
      lines.push(`## ${layer.label}`,'');
      const placed=t.cards.filter(c=>a.placements?.[c.id]===layer.id);
      if(!placed.length) lines.push('_No cards placed._');
      for(const c of placed){lines.push(`- ${c.text}${c.layer===layer.id?'':' [Reference category: '+LAYERS.find(l=>l.id===c.layer).label+']'}${(a.priorities||[]).includes(c.id)?' ★ Check first':''}`);}
      lines.push('');
    }
    lines.push('## Reflection','');
    for(const [k,label] of Object.entries(FIELD_LABELS))lines.push(`### ${label}`,(a.reflections?.[k]||'No response.'),'');
    if(a.revealed){lines.push('## Often-overlooked dependencies','');for(const b of t.blindspots)lines.push(`- **${b.title}**: ${b.explanation}`);}
    return lines.join('\n');
  }
  const coach={
    map:['What is the card actually describing: an ability, a requirement, a constraint or a person?','Try starting each claim with “It can…”, “It needs…”, “It might struggle with…” or “This changes things for…”.','Who or what must be present before the capability can work?','Different settings may change importance, but the type of claim stays the same.'],
    reflect:['Which dependency would stop the whole system if it failed?','What would you test with a small pilot before investing heavily?','Who gets the benefits, and who does the extra work or carries the risk?','What evidence would change your mind about adopting this technology?'],
    review:['Compare the reference categories with your own reasoning, not just the number.','Are the blind spots technological, organisational, social or environmental?','Which unseen dependency is most important in your chosen setting?','What question would you bring to a practitioner or stakeholder next?']
  };
  root.XRAY_ENGINE={LAYERS,FIELD_LABELS,tech,context,freshAttempt,getGrade,allSorted,keepPriorities,safe,asMarkdown,coach};
})(typeof window!=='undefined'?window:globalThis);
