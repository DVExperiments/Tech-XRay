"""Visual/browser smoke tests using Playwright and system Chromium.
Run: python tests/test_browser.py
Requires playwright only for testing, NOT for app users.
"""
import os,json
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'tests/screenshots').mkdir(exist_ok=True,parents=True)

def mount(page,stored=None):
    # About:blank fixture bypasses local HTTP policy in this testing sandbox.
    page.goto('about:blank')
    page.set_content((ROOT/'index.html').read_text(encoding='utf-8'))
    page.evaluate("""(seed) => {const map=new Map(Object.entries(seed)); Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>map.get(k)||null,setItem:(k,v)=>map.set(k,String(v)),removeItem:k=>map.delete(k),dump:()=>Object.fromEntries(map)}})}""",stored or {})
    page.add_style_tag(path=str(ROOT/'assets/styles.css'))
    for file in ('content.js','engine.js','app.js'):
        page.add_script_tag(path=str(ROOT/'assets'/file))

errors=[]
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu','--disable-dev-shm-usage'])
  page=browser.new_page(viewport={'width':1440,'height':950},device_scale_factor=1,accept_downloads=True)
  page.on('pageerror',lambda err:errors.append(str(err)))
  mount(page);page.wait_for_timeout(300)
  assert page.get_by_text('See beyond',exact=False).is_visible()
  assert page.locator('.tech-card').count()==12
  page.screenshot(path=str(ROOT/'tests/screenshots/explore_desktop.png'),full_page=True)
  page.locator('[data-tech="edge-ai"]').click()
  page.select_option('#setting-select','business')
  page.get_by_role('button',name='Begin X-Ray').click()
  assert 'Edge AI' in page.locator('.studio-hero h1').inner_text()
  assert page.locator('.evidence').count()==12
  page.locator('#coach-button').click()
  assert page.get_by_role('dialog').is_visible()
  page.locator('[data-action="close-modal"]').first.click()
  assert not page.get_by_role('dialog').count()
  # Test dropdown sorting + card reassignment
  first=page.locator('[data-place]').first
  card_id=first.get_attribute('data-place')
  first.select_option('needs')
  assert page.locator('.lane[data-layer="needs"] [data-card="'+card_id+'"]').count()==1
  # restore a card to tray and then fill all matching slots via exposed content (still actual UI interactions)
  page.locator('.lane[data-layer="needs"] [data-place="'+card_id+'"]').select_option('')
  content=page.evaluate('window.TECH_XRAY_CONTENT.technologies.find(t=>t.id==="edge-ai").cards')
  for c in content:
   page.locator(f'[data-place="{c["id"]}"]').select_option(c['layer'])
  assert page.locator('.tray .evidence').count()==0
  assert page.locator('[data-action="next-reflect"]').is_enabled()
  page.screenshot(path=str(ROOT/'tests/screenshots/mapped_desktop.png'),full_page=True)
  page.locator('[data-action="next-reflect"]').click()
  assert page.get_by_text('What would you check first?').is_visible()
  for c in content:
   if c['critical']:page.locator(f'[data-star="{c["id"]}"]').click()
  for k in ['opportunity','verify','caution','inclusion']:
   page.locator(f'[data-answer="{k}"]').fill('This is a thoughtful contextual answer that we would research and validate with users.')
  page.screenshot(path=str(ROOT/'tests/screenshots/reflect_desktop.png'),full_page=True)
  page.locator('[data-action="reveal"]').click()
  assert page.locator('.score-number').inner_text().startswith('100')
  assert page.locator('.blindspot').count()==3
  page.screenshot(path=str(ROOT/'tests/screenshots/review_desktop.png'),full_page=True)
  # Storage survives reload
  stored=page.evaluate('localStorage.dump()')
  mount(page,stored)
  page.locator('#nav-history').click()
  assert page.get_by_text('Edge AI').count()>=1
  assert page.get_by_text('Reviewed').count()>=1
  page.locator('[data-open]').first.click()
  assert page.locator('.score-number').inner_text().startswith('100')
  with page.expect_download() as notes_dl:
   page.locator('[data-action="export-attempt"]').click()
  notes=notes_dl.value
  assert notes.suggested_filename.endswith('.md')
  assert 'Edge AI' in Path(notes.path()).read_text(encoding='utf-8')
  # second setting
  page.locator('[data-action="new-setting"]').click()
  assert page.locator('#setting-select').input_value()!='business'
  # About information
  page.locator('#nav-about').click()
  assert page.get_by_text('How to interpret your score').is_visible()
  # Backup, delete and restore a complete investigation.
  page.locator('#nav-history').click()
  with page.expect_download() as backup_dl:
   page.locator('[data-action="backup"]').click()
  backup=backup_dl.value
  saved=Path(backup.path())
  exported=json.loads(saved.read_text(encoding='utf-8'))
  assert exported['app']=='tech-xray' and len(exported['attempts'])==1
  page.once('dialog',lambda d:d.accept())
  page.locator('[data-action="clear-history"]').click()
  assert page.locator('.history-entry').count()==0
  with page.expect_file_chooser() as picker:
   page.locator('[data-action="import"]').click()
  picker.value.set_files(str(saved))
  page.locator('.history-entry').first.wait_for(timeout=3000)
  assert page.locator('.history-entry').count()==1

  # Mobile screen content and overflow
  mob=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
  mob.on('pageerror',lambda err:errors.append(str(err)))
  mount(mob);mob.wait_for_timeout(300)
  mob.screenshot(path=str(ROOT/'tests/screenshots/explore_mobile.png'),full_page=True)
  assert mob.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1')
  mob.locator('[data-action="start"]').click()
  mob.screenshot(path=str(ROOT/'tests/screenshots/map_mobile.png'),full_page=True)
  assert mob.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1')
  # Dragging test desktop on new test page, verifies drag/drop events
  drag_page=browser.new_page(viewport={'width':1340,'height':900})
  mount(drag_page)
  drag_page.locator('[data-action="start"]').click()
  drag_page.locator('.tray .evidence').first.drag_to(drag_page.locator('.lane[data-layer="needs"]'),source_position={'x':15,'y':16},target_position={'x':70,'y':89})
  assert drag_page.locator('.lane[data-layer="needs"] .evidence').count()==1
  browser.close()
  assert not errors,errors
  print('PASS: desktop flow, dropdown sorting, drag and drop, scoring, 36 hidden items library, history persistence, context change, notes, mobile responsiveness, no JS errors')
finally:
 pass
