from pathlib import Path
import json, re, sys
errors=[]
html=Path('index.html')
news=Path('data/asset-news.json')
if not html.exists(): errors.append('index.html missing')
if not news.exists(): errors.append('data/asset-news.json missing')
if html.exists():
 s=html.read_text('utf-8')
 ids=re.findall(r'\bid=["\']([^"\']+)',s)
 dup=sorted({x for x in ids if ids.count(x)>1})
 if dup: errors.append('duplicate HTML ids: '+', '.join(dup[:20]))
 if 'integratedUpdatePanel' not in s: errors.append('integrated update panel missing')
if news.exists():
 try: d=json.loads(news.read_text('utf-8'))
 except Exception as e: errors.append('asset-news.json invalid: '+str(e)); d={}
 for k in ['schemaVersion','generatedAt','analysisDate','dataAsOf','portfolioState','coveredAssets','items']:
  if k not in d: errors.append('asset-news missing '+k)
 if d.get('schemaVersion')!='1.0': errors.append('unsupported schemaVersion')
 if not isinstance(d.get('items',[]),list): errors.append('items must be array')
 seen=set()
 for i,x in enumerate(d.get('items',[]) if isinstance(d.get('items',[]),list) else []):
  rid=x.get('id')
  if not rid or rid in seen: errors.append(f'item {i}: missing/duplicate id')
  seen.add(rid)
  if x.get('verificationStatus') not in ['verified','partiallyVerified']: errors.append(f'{rid}: unapproved verificationStatus')
  if x.get('confidence') not in ['medium','high']: errors.append(f'{rid}: confidence too low')
  src=x.get('sources',[])
  if not src or not all(isinstance(a,dict) and str(a.get('url','')).startswith('https://') for a in src): errors.append(f'{rid}: valid HTTPS source required')
if errors:
 print('\n'.join('ERROR: '+x for x in errors)); sys.exit(1)
print('Portal validation passed')
