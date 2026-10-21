import csv,json,pathlib,math
root=pathlib.Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'models.csv').open()))
numeric="inches frame cutout depth fs qts vas re le qms mms sd bl xmax watts impedance netLitres ventedLitres tuningHz msrp displacement".split()
models=[]
for row in rows:
 for k in numeric:
  row[k]=float(row[k])
  assert math.isfinite(row[k]) and row[k]>=0,(row['id'],k)
 for k in ['enabled','tested']: row[k]=str(row[k]).lower()=='true'
 assert 0<row['cutout']<row['frame']<=1000
 assert all(row[k]>0 for k in ['fs','qts','vas','re','qms','mms','sd','bl','xmax','netLitres','depth'])
 assert row['kind'] in ['full_range','sub'] and row['tier'] in ['good','better','best']
 assert row['source'].startswith('https://') and row['datasheet'].startswith('https://')
 assert row['tested'] is False, 'Physical validation requires a documented measured-design record, not a catalog checkbox'
 for k in ['image','drawing']: assert row[k].startswith('assets/') and '..' not in row[k] and (root/row[k]).is_file()
 # Never accept a different tracking ID from a product URL.
 from urllib.parse import urlparse,parse_qs,urlencode,urlunparse
 u=urlparse(row['amazonUrl']);assert u.scheme=='https' and u.hostname in ['www.amazon.com','amazon.com']
 q=parse_qs(u.query);q['tag']=['johnwickstu04-20'];row['amazonUrl']=urlunparse(u._replace(query=urlencode(q,doseq=True)))
 models.append(row)
assert len({m['id'] for m in models})==len(models) and 0<len(models)<=100
from datetime import datetime,timezone
catalog={'schema':'jw-speaker-catalog-v1','revision':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'models':models,'associateTag':'johnwickstu04-20'}
(root/'catalog.json').write_text(json.dumps(catalog,indent=2)+'\n')
# Desktop data contains no Amazon links or account tag. The separate guide owns purchasing.
app={**catalog,'models':[{k:v for k,v in m.items() if not k.startswith('amazon') and k!='priceNote'} for m in models if m['enabled']]};del app['associateTag']
(root/'app-catalog.json').write_text(json.dumps(app,indent=2)+'\n')
print('Validated',len(models),'models; generated guide and desktop catalogs')
