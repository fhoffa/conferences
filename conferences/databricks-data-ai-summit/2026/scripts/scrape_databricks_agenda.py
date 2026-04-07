import json, re, requests
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "raw"
NORMALIZED = BASE / "normalized"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def clean_html(s):
    if not s:
        return None
    s = re.sub(r"<[^>]+>", " ", s)
    return " ".join(s.split())

def main():
    RAW.mkdir(parents=True, exist_ok=True)
    NORMALIZED.mkdir(parents=True, exist_ok=True)
    html = requests.get("https://www.databricks.com/dataaisummit/agenda", headers=HEADERS, timeout=30).text
    (RAW / "agenda-full.html").write_text(html)
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
    if not m:
        raise RuntimeError("Could not find __NEXT_DATA__ on agenda page")
    data = json.loads(m.group(1))
    sessions = data['props']['pageProps']['agenda']['sessions']
    records = []
    for session in sessions:
        slug = (session.get('alias') or '').split('/session/')[-1] if session.get('alias') else None
        rec = {
            'conference':'databricks-data-ai-summit',
            'year':2026,
            'session_id':session.get('nid'),
            'title':session.get('title'),
            'abstract':clean_html(session.get('body')),
            'description_raw':session.get('body'),
            'track':(session.get('categories',{}).get('track') or [None])[0],
            'format':(session.get('categories',{}).get('type') or [None])[0],
            'level':(session.get('categories',{}).get('level') or [None])[0],
            'industry':session.get('categories',{}).get('industry') or [],
            'topic_tags':session.get('categories',{}).get('category') or [],
            'areas_of_interest':session.get('categories',{}).get('areasofinterest') or [],
            'delivery':(session.get('categories',{}).get('delivery') or [None])[0],
            'day':session.get('day') or None,
            'start_time':session.get('start_time') or None,
            'end_time':session.get('end_time') or None,
            'starts_pst':session.get('starts_pst') or None,
            'ends_pst':session.get('ends_pst') or None,
            'duration_minutes':session.get('duration'),
            'session_url':'https://www.databricks.com/dataaisummit'+session.get('alias',''),
            'catalog_url':'https://www.databricks.com/dataaisummit/agenda',
            'source_url':'https://www.databricks.com/dataaisummit/agenda',
            'source_type':'agenda_next_data_embedded_json',
            'raw_ref':'raw/agenda-full.html',
            'speakers':[],
            'companies': sorted({sp.get('company') for sp in session.get('speakers',[]) if sp.get('company')}),
            'slug': slug,
        }
        for sp in session.get('speakers',[]):
            rec['speakers'].append({
                'name':sp.get('name'),
                'job_title':sp.get('job_title'),
                'company':sp.get('company'),
                'bio':clean_html(sp.get('bio')),
                'profile_url':('https://www.databricks.com/dataaisummit'+sp.get('alias')) if sp.get('alias') else None,
                'image_url':(sp.get('image') or {}).get('url'),
                'source_url':('https://www.databricks.com/dataaisummit'+sp.get('alias')) if sp.get('alias') else 'https://www.databricks.com/dataaisummit/agenda',
            })
        records.append(rec)
    (NORMALIZED / 'sessions.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
    summary = {
        'session_count': len(records),
        'sessions_with_speakers': sum(1 for r in records if r['speakers']),
        'speaker_count': sum(len(r['speakers']) for r in records),
        'speakers_with_job_title': sum(1 for r in records for s in r['speakers'] if s.get('job_title')),
        'unique_companies': len({c for r in records for c in r.get('companies', []) if c}),
        'sessions_with_any_timing': sum(1 for r in records if r.get('start_time') or r.get('starts_pst') or r.get('day')),
    }
    (NORMALIZED / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f'wrote {len(records)} sessions')

if __name__ == '__main__':
    main()
