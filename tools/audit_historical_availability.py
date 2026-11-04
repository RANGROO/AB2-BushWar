"""Check every selector against nation coverage and report monthly purchase availability."""
from pathlib import Path
import json,re,sys
from audit_database_loading import parse

ROOT=Path(__file__).resolve().parents[1]
# Preserve saved selector ordinals while retiring duplicate single-vehicle fixtures.
RETIRED_CUBA_RHODESIA=set()  # Legacy parked selectors removed by owner-authorized vanilla restructuring.


def audit(path):
    """Inspect all months without claiming that the engine purchase screen was tested."""
    result={'errors':[],'factions':[],'monthly_counts':[],'quarantined':[]}
    # Compatibility selectors parked outside the mod horizon; no migration import.
    QUARANTINE={(11,'formation13'),(11,'formation28'),(11,'formation20'),(11,'formation59'),(11,'formation62'),(11,'flight18')}
    for faction in parse(path):
        fid=int(faction.get('name'))
        if fid<11:continue
        selectors=[];coverage=set();phase_names=[];phase_intervals=[]
        for sec in faction.findall('section'):
            if not sec.get('name','').startswith('date'):continue
            d={x.get('name'):x.get('value') for x in sec.findall('string')}
            sy,sm=map(int,d['from'].split(','));ey,em=map(int,d['to'].split(','))
            phase_names.append(sec.get('name'));phase_intervals.append((sy*12+sm-1,ey*12+em-1))
            for n in range(sy*12+sm-1,ey*12+em):
                if n in coverage:result['errors'].append(f'Faction {fid} overlapping setting intervals at {n//12}-{n%12+1}')
                coverage.add(n)
        if phase_names!=['date'+str(i) for i in range(1,len(phase_names)+1)]:
            result['errors'].append(f'Faction {fid} date phase ordinals/document order differ from native format')
        if any(phase_intervals[i-1][1]>=phase_intervals[i][0] for i in range(1,len(phase_intervals))):
            result['errors'].append(f'Faction {fid} date phases are not chronological/nonoverlapping')
        for x in faction.findall('string'):
            key=x.get('name')
            if not re.fullmatch(r'(formation|flight)\d+',key):continue
            ident,sy,sm,ey,em,weight=map(int,x.get('value').split(','))
            # Retired purchase duplicates retain their ordinals outside the mod period.
            retired_infantry={(11,'formation45'),(11,'formation47')}
            retired_transport={(11,'formation7'),(11,'formation8'),(11,'formation98')}  # Retired Y2 keeps its compatibility ordinal.
            retired_long_range={(11,f'formation{i}') for i in [11,15,27,64,65,66,75,76]}
            if (fid,key) in QUARANTINE or (fid,key) in RETIRED_CUBA_RHODESIA or (fid,key) in retired_infantry or (fid,key) in retired_transport or (fid,key) in retired_long_range:
                if (sy,sm,ey,em)!=(1995,1,1995,12):result['errors'].append(f'Unexpected quarantine sentinel for {fid} {key}')
                result['quarantined'].append({'faction':fid,'selector':key,'id':ident});continue
            months=set(range(sy*12+sm-1,ey*12+em))
            missing=months-coverage
            if missing:result['errors'].append(f'Faction {fid} {key} has {len(missing)} months outside faction settings')
            selectors.append((key,ident,months))
        result['factions'].append({'id':fid,'ground':sum(k.startswith('formation') for k,_,_ in selectors),'flights':sum(k.startswith('flight') for k,_,_ in selectors)})
        for year in range(1965,1995):
            for month in range(1,13):
                n=year*12+month-1
                result['monthly_counts'].append({'faction':fid,'year':year,'month':month,'ground':sum(k.startswith('formation') and n in m for k,_,m in selectors),'flights':sum(k.startswith('flight') and n in m for k,_,m in selectors)})
    result['passed']=not result['errors']
    return result


if __name__=='__main__':
    p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'package/data/database/Bush War/factions.xml'
    (ROOT/'dist').mkdir(exist_ok=True)
    r=audit(p);(ROOT/'dist/historical-availability-monthly-audit.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({'passed':r['passed'],'errors':r['errors'],'factions':r['factions']},indent=2));sys.exit(0 if r['passed'] else 1)
