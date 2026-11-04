from pathlib import Path
import json,re,sys
s=Path('index.html').read_text('utf-8');e=[]
for f in ['assets/membership-v3.js','assets/membership-v3.css','data/asset-news.json']:
 if not Path(f).exists():e.append(f+' missing')
if 'membershipAutoBenefit' not in s:e.append('transaction membership hook missing')
ids=re.findall(r'\bid=["\']([^"\']+)',s)
if len(ids)!=len(set(ids)):e.append('duplicate HTML id')
json.loads(Path('data/asset-news.json').read_text('utf-8'))
print('PASS' if not e else '\n'.join(e));sys.exit(bool(e))
