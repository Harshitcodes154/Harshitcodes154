/* Rebuild the vector UI and raster hero. npm install --no-save sharp */
const fs = require('node:fs');
const path = require('node:path');
const { createRequire } = require('node:module');
let sharp;
try { sharp = require('sharp'); }
catch { sharp = createRequire(process.env.NODE_DEPENDENCIES + '/package.json')('sharp'); }
const root = path.resolve(__dirname, '..');
const C = { bg:'#080d14', panel:'#101a25', line:'#213748', text:'#eaf5ff', muted:'#91a7b9', cyan:'#48dcff', green:'#6cf5b0', purple:'#ab9cff' };
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const text = (x,y,s,size=20,color=C.text,weight=400,mono=false,extra='') => `<text x="${x}" y="${y}" font-family="${mono?'Consolas, monospace':'Segoe UI, Arial, sans-serif'}" font-size="${size}" fill="${color}" font-weight="${weight}" ${extra}>${esc(s)}</text>`;
const line = (x1,y1,x2,y2,color=C.line,extra='') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" ${extra}/>`;
const rect = (x,y,w,h,fill=C.panel,rx=12,stroke=C.line) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}"/>`;
const dot = (x,y,color=C.green) => `<circle cx="${x}" cy="${y}" r="4" fill="${color}" class="pulse"/>`;
const css = `<style>.pulse{animation:pulse 3s ease-in-out infinite}.flow{stroke-dasharray:8 12;animation:flow 5s linear infinite}.sweep{transform-box:fill-box;transform-origin:center;animation:sweep 12s linear infinite}.cursor{animation:pulse 1.4s steps(2,end) infinite}@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}@keyframes flow{to{stroke-dashoffset:-100}}@keyframes sweep{to{transform:rotate(360deg)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style>`;
const svg = (w,h,title,body) => `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(title)}"><title>${esc(title)}</title>${css}<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#12222f" stroke-width=".7"/></pattern><linearGradient id="fade"><stop stop-color="#48dcff" stop-opacity=".18"/><stop offset="1" stop-color="#48dcff" stop-opacity="0"/></linearGradient></defs><rect width="100%" height="100%" rx="16" fill="${C.bg}"/><rect x=".5" y=".5" width="${w-1}" height="${h-1}" rx="16" fill="url(#grid)" stroke="${C.line}"/>${body}</svg>`;
const save = (file,data) => { const p=path.join(root,file);fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,data); };
const pill = (x,y,label,color=C.cyan,w=null) => {w=w||label.length*9.2+26;return rect(x,y,w,30,'#0d1924',5,color)+text(x+13,y+20,label,13,color,600,true);};
async function main(){
 const arg = process.argv.find(x=>x.startsWith('--photo='));
 const photoPath = arg ? path.resolve(root,arg.slice(8)) : path.join(root,'assets/profile/cinematic-headshot.png');
 const mime = /\.jpe?g$/i.test(photoPath) ? 'image/jpeg' : 'image/png';
 const photo = fs.readFileSync(photoPath).toString('base64');
 const image=(x,y,w,h)=>`<image x="${x}" y="${y}" width="${w}" height="${h}" href="data:${mime};base64,${photo}" preserveAspectRatio="xMidYMid slice"/>`;
 let h=text(44,48,'HK / SYSTEM 01',15,C.cyan,600,true)+text(822,48,'PERSONAL ENGINEERING ENVIRONMENT',13,C.muted,400,true)+line(44,70,1156,70);
 h+=text(44,122,'AI ENGINEERING COMMAND CENTER',18,C.green,600,true)+text(40,209,'HARSHIT',88,C.text,700)+text(40,300,'KUMAR',88,C.text,700);
 h+=text(47,352,'AI/ML ENGINEER   /   GENAI BUILDER',21,C.cyan,600)+text(47,386,'COMPUTER VISION   /   SYSTEMS EXPLORER',19,C.muted,500);
 h+=rect(44,423,616,178,'#0b141e',8)+text(65,457,'harshit@linux:~/profile',17,C.green,400,true)+text(65,493,'$ ./initialize_profile',20,C.text,400,true)+text(65,527,'[OK] model → inference → application',18,C.muted,400,true)+dot(70,567)+text(85,573,'ONLINE  /  BUILDING THE NEXT ITERATION',16,C.green,600,true);
 h+=image(712,95,443,506)+rect(712,95,443,506,'none',0,C.cyan)+`<path d="M700 130V83h48M1120 83h47v48M700 564v49h48M1120 613h47v-49" fill="none" stroke="${C.green}" stroke-width="3"/>`;
 h+=text(44,644,'VIT-AP  /  AI & MACHINE LEARNING',15,C.muted,400,true)+text(744,644,'HARSHITCODES154  //  ENGINEER PROFILE',14,C.muted,400,true);
 await sharp(Buffer.from(svg(1200,680,'HARSHIT KUMAR — AI Engineering Command Center',h))).png({palette:false,compressionLevel:9}).toFile(path.join(root,'assets/hero.png'));
 let m=text(30,40,'HK / AI ENGINEERING COMMAND CENTER',16,C.green,600,true)+line(30,59,570,59)+text(25,139,'HARSHIT',72,C.text,700)+text(25,211,'KUMAR',72,C.text,700);
 m+=image(275,240,294,335)+rect(275,240,294,335,'none',0,C.cyan)+text(30,282,'AI/ML',25,C.cyan,700)+text(30,313,'ENGINEER',25,C.text,600)+text(30,373,'GENAI',25,C.cyan,700)+text(30,404,'BUILDER',25,C.text,600)+text(30,464,'VISION +',24,C.muted,500)+text(30,495,'SYSTEMS',24,C.muted,500)+dot(36,550)+text(52,556,'ONLINE',18,C.green,600,true);
 m+=rect(30,605,540,126,'#0b141e',8)+text(50,640,'harshit@linux:~/profile',19,C.green,400,true)+text(50,676,'$ ./initialize_profile',22,C.text,400,true)+text(50,711,'[OK] BUILD. TEST. ITERATE.',19,C.muted,400,true)+text(30,771,'VIT-AP  /  HARSHITCODES154',16,C.muted,400,true);
 await sharp(Buffer.from(svg(600,810,'HARSHIT KUMAR — mobile hero',m))).png({compressionLevel:9}).toFile(path.join(root,'assets/hero-mobile.png'));
 // Large titles carry the visual story. Full technical detail remains native Markdown.
 function card(file,num,title,subtitle,status,accent,art,foot){
  let b=text(30,37,`MODULE ${num} / PROJECT DIRECTORY`,13,C.muted,400,true)+dot(678,32,accent)+text(692,37,status,13,accent,600,true)+line(30,53,870,53);
  b+=text(30,110,title,title.length>20?35:48,C.text,700)+text(32,146,subtitle,15,accent,600,true)+text(32,204,foot,16,C.muted,400,true)+art;
  b+=line(30,237,870,237)+`<path d="M30 237H870" fill="none" stroke="${accent}" opacity=".55" class="flow"/>`+text(30,268,'SOURCE / ARCHITECTURE / IMPLEMENTATION BELOW',12,C.muted,400,true);
  save(`assets/projects/${file}.svg`,svg(900,290,`${title}: ${subtitle}`,b));
 }
 let wafer='';for(let i=-4;i<=4;i++)for(let j=-4;j<=4;j++){if(i*i+j*j<22){let defect=(i-j===1&&i>0)||(i===2&&j===-1);wafer+=`<rect x="${764+i*12}" y="${138+j*12}" width="8" height="8" rx="1" fill="${defect?C.purple:C.cyan}" opacity="${defect?1:.35}"/>`;}}
 wafer+=`<circle cx="768" cy="142" r="71" fill="none" stroke="${C.cyan}" stroke-opacity=".5"/><circle cx="768" cy="142" r="83" fill="none" stroke="${C.cyan}" stroke-dasharray="2 10" class="flow"/>`;
 card('wafer-gpt','01','WAFER-GPT','AI-POWERED WAFER DEFECT INTELLIGENCE','SOURCE INSPECTED',C.cyan,wafer,'CNN CLASSIFICATION  /  GRAD-CAM  /  GEMINI');
 let thermal=`<circle cx="768" cy="144" r="78" fill="none" stroke="${C.line}"/><circle cx="768" cy="144" r="51" fill="none" stroke="${C.line}"/><circle cx="768" cy="144" r="24" fill="none" stroke="${C.line}"/>`+line(680,144,856,144)+line(768,66,768,222);
 for(const [x,y,r] of [[752,122,8],[796,145,12],[750,175,6]]) thermal+=`<circle cx="${x}" cy="${y}" r="${r+8}" fill="${C.green}" opacity=".08"/><circle cx="${x}" cy="${y}" r="${r}" fill="${C.green}" opacity=".6" class="pulse"/>`;
 card('thermowatch-ai','02','ThermoWatch-AI','SATELLITE THERMAL / INDUSTRIAL RISK','SOURCE INSPECTED',C.green,thermal,'NASA FIRMS  /  GEOSPATIAL ML  /  STREAMLIT');
 let radar=`<g><circle cx="768" cy="144" r="78" fill="#0d1923" stroke="${C.line}"/><circle cx="768" cy="144" r="52" fill="none" stroke="${C.line}"/><circle cx="768" cy="144" r="26" fill="none" stroke="${C.line}"/>${line(690,144,846,144)}${line(768,66,768,222)}<g class="sweep"><circle cx="768" cy="144" r="78" fill="none" stroke="none"/><path d="M768 144L840 114A78 78 0 0 1 844 161Z" fill="${C.purple}" opacity=".2"/><path d="M768 144L840 114" stroke="${C.purple}"/></g><path d="M766 128l-7 22 9-5 9 5-7-22z" fill="${C.text}"/></g>`;
 card('operation-sindoor','03','OPERATION SINDOOR','FICTIONAL AERIAL COMBAT / GAME DEVELOPMENT','GAME PROJECT',C.purple,radar,'RADAR  /  TARGET LOCK  /  MISSIONS  /  HUD');
 let focus=text(28,37,'CURRENT FOCUS / EXPLORATION MAP',14,C.muted,500,true)+dot(866,31);
 ['AI SYSTEMS','COMPUTER VISION','GENERATIVE AI','AGENTIC SYSTEMS','LINUX','CLOUD','GAME DEVELOPMENT','SYSTEM DESIGN'].forEach((s,i)=>{let x=28+(i%2)*437,y=60+Math.floor(i/2)*51;focus+=rect(x,y,409,39,'#0d1822',5)+text(x+16,y+26,s,19,i<4?C.cyan:C.green,600,true);});
 save('assets/ui/current-focus.svg',svg(900,286,'Current focus: AI systems, computer vision, generative AI, agents, Linux, cloud, games and system design',focus));
 const stages=['DATA','MODEL','INFERENCE','API','APPLICATION','DEPLOYMENT'];
 let pipe=text(28,37,'ENGINEERING LOOP / FROM SIGNAL TO SOFTWARE',14,C.muted,500,true);
 stages.forEach((s,i)=>{let x=32+(i%3)*295,y=69+Math.floor(i/3)*102;pipe+=rect(x,y,245,65,'#101d29',8)+text(x+16,y+24,`0${i+1}`,13,C.green,600,true)+text(x+16,y+50,s,20,C.text,600);if(i%3<2)pipe+=line(x+249,y+33,x+290,y+33,C.cyan,'stroke-width="2" class="flow"');});
 pipe+=`<path d="M866 101h14v55H15v47h13" fill="none" stroke="${C.cyan}" stroke-width="2" class="flow"/>`+text(31,271,'observe → train → evaluate → integrate → ship → improve',16,C.muted,400,true);
 save('assets/ui/engineering-pipeline.svg',svg(900,300,'Workflow: data to model to inference to API to application to deployment',pipe));
 let ctf=text(28,36,'SECURITY CHALLENGES / COMPETITION RECORD',13,C.muted,500,true)+dot(866,31)+text(28,96,'NULL CHAPTER CTF',40,C.text,700)+pill(28,118,'STATUS: WINNER',C.green,180)+text(28,187,'Cryptography · Web challenges · Reverse engineering',18,C.muted,400)+`<path d="M795 71l40 15v39q-8 25-40 42-32-17-40-42V86z" fill="#102823" stroke="${C.green}"/><path d="M777 117l13 13 24-28" fill="none" stroke="${C.green}" stroke-width="4"/>`;
 save('assets/achievements/ctf.svg',svg(900,218,'Null Chapter CTF — winner',ctf));
 let sig=text(28,37,'SESSION PERSISTENT / NEXT BUILD',13,C.muted,400,true)+text(28,86,'harshit@github:~ $ ./next_iteration',25,C.text,600,true)+text(28,131,'STATUS   ONLINE',19,C.green,500,true)+text(28,168,'MODE     BUILD → TEST → LEARN → SHIP',19,C.cyan,500,true)+text(28,208,'Better questions. Stronger systems. One commit at a time.',18,C.muted)+`<rect x="800" y="158" width="12" height="22" fill="${C.green}" class="cursor"/>`;
 save('assets/ui/signature.svg',svg(900,241,'Online. Build, test, learn, ship. Better questions. Stronger systems. One commit at a time.',sig));
 for(const [name,label,color] of [['source','VIEW SOURCE',C.cyan],['interface','OPEN INTERFACE',C.green],['demo','OPEN APP',C.green],['resume','DOWNLOAD RESUME',C.green],['linkedin','CONNECT ON LINKEDIN',C.cyan],['mail','SEND EMAIL',C.green],['github','GITHUB',C.cyan]]){
   const w=label.length*9+59;save(`assets/ui/${name}.svg`,svg(w,42,label,text(16,27,label,14,color,600,true)+text(w-29,27,'↗',18,color)));
 }
 // Static counterparts are useful for reduced-motion readers and documentation.
 for(const folder of ['assets/ui','assets/projects','assets/achievements']) for(const f of fs.readdirSync(path.join(root,folder)).filter(f=>f.endsWith('.svg'))){
  const src=fs.readFileSync(path.join(root,folder,f),'utf8');const staticDir=path.join(root,'assets/static',folder.split('/').pop());fs.mkdirSync(staticDir,{recursive:true});fs.writeFileSync(path.join(staticDir,f),src.replace(/<style>[\s\S]*?<\/style>/g,''));
 }
 console.log('Created hero layouts, project modules, workflow, focus, CTF, signature and buttons.');
}
main().catch(e=>{console.error(e);process.exit(1)});
