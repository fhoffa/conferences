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
    all_slugs = []
    for page in range(1, 10):
        url = f"https://www.databricks.com/dataaisummit/agenda?page={page}"
        html = requests.get(url, headers=HEADERS, timeout=30).text
        (RAW / f"agenda-page-{page}.html").write_text(html)
        for m in re.finditer(r'/dataaisummit/session/([^"?#]+)', html):
            slug = m.group(1)
            if slug not in all_slugs:
                all_slugs.append(slug)
    records = []
    for slug in all_slugs:
        url = f"https://www.databricks.com/dataaisummit/session/{slug}"
        html = requests.get(url, headers=HEADERS, timeout=30).text
        (RAW / f"session-{slug}.html").write_text(html)
        m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
        if not m:
            continue
        data = json.loads(m.group(1))
        session = data['props']['pageProps']['sessionInfo']
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
            'source_url':url,
            'source_type':'next_data_embedded_json',
            'raw_ref':f'raw/session-{slug}.html',
            'speakers':[],
            'companies': sorted({sp.get('company') for sp in session.get('speakers',[]) if sp.get('company')})
        }
        for sp in session.get('speakers',[]):
            rec['speakers'].append({
                'name':sp.get('name'),
                'job_title':sp.get('job_title'),
                'company':sp.get('company'),
                'bio':clean_html(sp.get('bio')),
                'profile_url':('https://www.databricks.com/dataaisummit'+sp.get('alias')) if sp.get('alias') else None,
                'image_url':(sp.get('image') or {}).get('url'),
                'source_url':('https://www.databricks.com/dataaisummit'+sp.get('alias')) if sp.get('alias') else url,
            })
        records.append(rec)
    (NORMALIZED / 'sessions.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
    print(f'wrote {len(records)} sessions')

if __name__ == '__main__':
    main()
