/* Cache the core app for optional repeat/offline use over HTTPS. */
const CACHE='tech-xray-v1-20261012';
const FILES=['./','./index.html','./assets/app.js','./assets/engine.js','./assets/content.js','./assets/styles.css','./assets/icon.svg','./assets/cover.svg','./manifest.webmanifest'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('tech-xray-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin)return;e.respondWith(fetch(e.request).then(res=>{if(res.ok){let copy=res.clone();caches.open(CACHE).then(c=>c.put(e.request,copy)).catch(()=>{});}return res;}).catch(()=>caches.match(e.request)));});
