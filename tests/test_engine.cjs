const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const dir=path.resolve(__dirname,'..');let c={};
const sandbox={window:{TECH_XRAY_CONTENT:JSON.parse(fs.readFileSync(path.join(dir,'assets/content.json'),'utf8'))},globalThis:c};
vm.runInNewContext(fs.readFileSync(path.join(dir,'assets/engine.js'),'utf8'),sandbox);
const E=sandbox.window.XRAY_ENGINE,content=sandbox.window.TECH_XRAY_CONTENT;
assert.equal(content.technologies.length,12);
assert.equal(content.contexts.length,4);
for(const t of content.technologies){
 assert.equal(t.cards.length,12);
 assert.equal(t.blindspots.length,3);
 assert.equal(new Set(t.cards.map(c=>c.id)).size,12);
 assert.equal(t.cards.filter(c=>c.critical).length,3);
 let a=E.freshAttempt(t.id,'education');
 assert.equal(E.allSorted(t,a),false);
 assert.equal(E.getGrade(t,a).score,0);
 t.cards.forEach(c=>a.placements[c.id]=c.layer);
 assert.equal(E.allSorted(t,a),true);
 assert.equal(E.getGrade(t,a).sorting,60);
 a.priorities=t.cards.filter(c=>c.critical).map(c=>c.id);
 Object.keys(E.FIELD_LABELS).forEach(k=>a.reflections[k]='A thoughtful question about evidence and real-world implementation.');
 assert.equal(E.getGrade(t,a).score,100,`${t.title} full score`);
 a.placements[t.cards[0].id]='limits'===t.cards[0].layer?'does':'limits';
 assert.equal(E.getGrade(t,a).sorting,55);
 assert.equal(E.getGrade(t,a).score,95);
 assert.match(E.asMarkdown(t,content.contexts[0],a),/Practice score/);
}
console.log('PASS: all 12 technology libraries, 144 cards, 36 blind spots, categories, priority scoring, complete and incomplete rubrics, Markdown.');
