#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const RAW_DIR = path.join(ROOT, 'raw');
const NORMALIZED_DIR = path.join(ROOT, 'normalized');
const ANALYSIS_DIR = path.join(ROOT, 'analysis');
const DOCS_DIR = path.join(ROOT, 'docs');

const CATALOG_URL = 'https://reg.snowflake.com/flow/snowflake/summit24/sessions/page/catalog';
const SESSIONS_API_URL = 'https://events.summit.snowflake.com/api/sessions';
const WIDGET_CONFIG_URL = 'https://events.summit.snowflake.com/api/widgetConfig';
const SESSION_DETAILS_BASE = 'https://reg.snowflake.com/flow/common/sessions/bysessionids';
const BATCH_SIZE = 40;

for (const dir of [RAW_DIR, NORMALIZED_DIR, ANALYSIS_DIR, DOCS_DIR]) {
  fs.mkdirSync(dir, { recursive: true });
}

function pick(headers, key) {
  for (const [k, v] of Object.entries(headers || {})) {
    if (k.toLowerCase() === key.toLowerCase()) return v;
  }
  return undefined;
}

function stripHtml(value) {
  if (!value || typeof value !== 'string') return value ?? null;
  return value.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim() || null;
}

function normalizeTimes(times) {
  return (times || []).map((time) => ({
    session_time_id: time.sessionTimeID || null,
    date: time.date || null,
    date_formatted: time.dateFormatted || null,
    day_name: time.dayName || time.dayDisplayName || null,
    start_time: time.startTime || null,
    start_time_formatted: time.startTimeFormatted || null,
    end_time: time.endTime || null,
    end_time_formatted: time.endTimeFormatted || null,
    utc_start_time: time.utcStartTime || null,
    utc_end_time: time.utcEndTime || null,
    room: time.room || null,
    room_id: time.roomId || null,
    length_minutes: time.length ?? null,
    capacity: time.capacity ?? null,
    in_person_time: time.inPersonTime ?? null,
    virtual_time: time.virtualTime ?? null,
    view_access_public: time.viewAccessPublic ?? null,
  }));
}

function normalizeSpeakers(participants) {
  return (participants || []).map((speaker) => ({
    speaker_id: speaker.speakerId || null,
    full_name: speaker.preferredFullName || speaker.globalPreferredFullName || speaker.fullName || speaker.globalFullName || null,
    first_name: speaker.preferredFirstname || speaker.firstName || speaker.globalFirstname || null,
    last_name: speaker.lastName || speaker.globalLastname || null,
    company: speaker.companyName || speaker.globalCompany || null,
    job_title: speaker.jobTitle || speaker.globalJobtitle || null,
    bio: stripHtml(speaker.bio || speaker.globalBio || null),
    photo_url: speaker.photoURL || speaker.globalPhotoURL || null,
    linkedin: speaker.linkedIn || null,
    twitter: speaker.twitter || null,
    roles: speaker.roles || null,
    display_order: speaker.displayorder ?? null,
  }));
}

function normalizeAttributes(attributevalues) {
  const attributes = {};
  for (const attr of attributevalues || []) {
    const key = attr.attribute || attr.attributeCode || attr.filterID || attr.name;
    const value = attr.value ?? attr.displayValue ?? attr.attributeValue ?? attr.code ?? attr.name;
    if (!key || value == null) continue;
    if (!attributes[key]) attributes[key] = [];
    if (!attributes[key].includes(value)) attributes[key].push(value);
  }
  return attributes;
}

function normalizeSession(session, sourceCatalogUrl) {
  const files = (session.files || []).map((file) => ({
    file_code: file.fileCode || null,
    file_type: file.fileType || null,
    filename: file.filename || null,
    url: file.url || null,
    is_private: file.isPrivate ?? null,
  }));
  const speakers = normalizeSpeakers(session.participants || []);
  return {
    session_id: session.sessionID || null,
    session_time_id: session.sessionTimeID || null,
    external_id: session.externalID || null,
    code: session.code || session.abbreviation || null,
    code_id: session.code_id || null,
    title: session.title || null,
    abstract: stripHtml(session.abstract || null),
    session_type: session.type || null,
    language: session.language || null,
    length_minutes: session.length ?? null,
    published: session.published ?? null,
    status: session.status || null,
    event_code: session.eventCode || null,
    event_id: session.eventId || null,
    event_name: session.eventName || null,
    modified: session.modified || null,
    featured_value: session.featured_value || null,
    view_access_public: session.viewAccessPublic ?? null,
    has_webinar_profile: session.hasWebinarProfile ?? null,
    has_webinar_chat_profile: session.hasWebinarChatProfile ?? null,
    embedable_webinar: session.embedableWebinar ?? null,
    webinar_provider: session.webinarProvider || null,
    source_catalog_url: sourceCatalogUrl,
    speakers,
    speaker_count: speakers.length,
    times: normalizeTimes(session.times || []),
    attributes: normalizeAttributes(session.attributevalues || []),
    files,
    file_count: files.length,
  };
}

function buildSummary({ normalized, listingCount, pageCount, pageSize, rfApiProfileId, rfWidgetId, detailBatchCount, detailSessionCount }) {
  const uniqueSessionIds = new Set(normalized.map((s) => s.session_id)).size;
  const duplicateSessionIds = listingCount - uniqueSessionIds;
  const totalSpeakerLinks = normalized.reduce((sum, s) => sum + s.speaker_count, 0);
  const withFiles = normalized.filter((s) => s.file_count > 0).length;
  const byType = new Map();
  for (const session of normalized) {
    const key = session.session_type || 'Unknown';
    byType.set(key, (byType.get(key) || 0) + 1);
  }
  const topTypes = [...byType.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10);

  return [
    '# Snowflake Summit 2024 catalog snapshot',
    '',
    `- source catalog: ${CATALOG_URL}`,
    `- source sessions API: ${SESSIONS_API_URL}`,
    `- source detail API: ${SESSION_DETAILS_BASE}`,
    `- captured catalog listings: ${listingCount}`,
    `- unique session IDs captured: ${uniqueSessionIds}`,
    `- duplicate session IDs across catalog listings: ${duplicateSessionIds}`,
    `- sessions API page count: ${pageCount}`,
    `- sessions API page size observed: ${pageSize}`,
    `- detail batches fetched: ${detailBatchCount}`,
    `- detail records fetched: ${detailSessionCount}`,
    `- normalized sessions written: ${normalized.length}`,
    `- sessions with speaker links: ${normalized.filter((s) => s.speaker_count > 0).length}`,
    `- total speaker links: ${totalSpeakerLinks}`,
    `- sessions with public files/images: ${withFiles}`,
    `- observed rfApiProfileId: ${rfApiProfileId}`,
    `- observed rfWidgetId: ${rfWidgetId}`,
    '',
    '## What this capture is',
    '',
    'This is a public browser-backed RainFocus capture for Snowflake Summit 2024. It uses the same unauthenticated catalog API the public page calls, then enriches deduplicated session IDs through the public `flow/common/sessions/bysessionids` endpoint observed from the same page context.',
    '',
    '## Why this is the practical depth limit',
    '',
    '- The main catalog API is enough to enumerate the full public catalog and speaker/time metadata.',
    '- The `bysessionids` endpoint adds useful public fields like session files/images and slightly richer detail records, but it requires a live `rfcsrf` token from a browser session.',
    '- Beyond that, secondary RainFocus endpoints are better treated as optional follow-up rather than a stable deeper export path.',
    '',
    '## Sessions by type',
    ...topTypes.map(([type, count]) => `- ${type}: ${count}`),
    '',
  ].join('\n');
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const requestMatches = [];

  page.on('request', (request) => {
    const url = request.url();
    if (url.includes('/api/sessions') || url.includes('/api/widgetConfig') || url.includes('/flow/common/sessions/bysessionids')) {
      requestMatches.push({
        url,
        method: request.method(),
        headers: request.headers(),
        postData: request.postData(),
      });
    }
  });

  await page.goto(CATALOG_URL, { waitUntil: 'networkidle', timeout: 120000 });
  await page.waitForTimeout(5000);

  fs.writeFileSync(path.join(RAW_DIR, 'catalog.html'), await page.content());

  const sessionRequest = requestMatches.find((req) => req.url.includes('/api/sessions'));
  const widgetRequest = requestMatches.find((req) => req.url.includes('/api/widgetConfig'));
  const detailRequest = requestMatches.find((req) => req.url.includes('/flow/common/sessions/bysessionids'));
  if (!sessionRequest || !widgetRequest || !detailRequest) {
    throw new Error('Could not observe one or more required catalog API requests in the browser session');
  }

  const rfApiProfileId = pick(sessionRequest.headers, 'rfapiprofileid');
  const rfWidgetId = pick(sessionRequest.headers, 'rfwidgetid');
  const rfcsrf = pick(detailRequest.headers, 'rfcsrf');
  if (!rfApiProfileId || !rfWidgetId || !rfcsrf) {
    throw new Error('Missing RainFocus headers or rfcsrf token from observed requests');
  }

  const baseHeaders = {
    rfApiProfileId,
    rfWidgetId,
    referer: 'https://reg.snowflake.com/',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': pick(sessionRequest.headers, 'user-agent') || 'Mozilla/5.0',
  };

  const firstSessionsResponse = await page.request.post(SESSIONS_API_URL, {
    headers: baseHeaders,
    form: {
      'tab.sessioncatalogtab': '1714168666431001NNiH',
      type: 'session',
      browserTimezone: 'America/Los_Angeles',
      catalogDisplay: 'grid',
    },
  });
  const widgetConfigResponse = await page.request.post(WIDGET_CONFIG_URL, { headers: baseHeaders });

  const firstSessionsJson = await firstSessionsResponse.json();
  const widgetConfigJson = await widgetConfigResponse.json();
  if (firstSessionsJson.responseCode !== '0') {
    throw new Error(`Unexpected sessions API response: ${JSON.stringify(firstSessionsJson).slice(0, 500)}`);
  }

  const firstSection = (firstSessionsJson.sectionList || [])[0] || {};
  const total = Number(firstSection.total || firstSessionsJson.totalSearchItems || 0);
  const pageSize = Number(firstSection.size || firstSection.numItems || 50);
  const pagedResponses = [firstSessionsJson];
  const rawCatalogListings = [...(firstSection.items || [])];

  for (let from = rawCatalogListings.length; from < total; from += pageSize) {
    const response = await page.request.post(SESSIONS_API_URL, {
      headers: baseHeaders,
      form: {
        'tab.sessioncatalogtab': '1714168666431001NNiH',
        type: 'session',
        browserTimezone: 'America/Los_Angeles',
        catalogDisplay: 'grid',
        from: String(from),
      },
    });
    const json = await response.json();
    if (json.responseCode !== '0') {
      throw new Error(`Unexpected paginated response at from=${from}: ${JSON.stringify(json).slice(0, 500)}`);
    }
    pagedResponses.push(json);
    rawCatalogListings.push(...(json.items || []));
  }

  const dedupedCatalogSessions = Array.from(new Map(rawCatalogListings.map((session) => [session.sessionID, session])).values());
  const detailUrl = new URL(detailRequest.url);
  const workflowApiToken = detailUrl.searchParams.get('workflowApiToken');
  const ver = detailUrl.searchParams.get('ver');
  const detailHeaders = {
    rfcsrf,
    referer: CATALOG_URL,
    'user-agent': pick(detailRequest.headers, 'user-agent') || pick(sessionRequest.headers, 'user-agent') || 'Mozilla/5.0',
  };

  const detailedSessions = [];
  const detailResponses = [];
  for (let i = 0; i < dedupedCatalogSessions.length; i += BATCH_SIZE) {
    const batch = dedupedCatalogSessions.slice(i, i + BATCH_SIZE);
    const sessionIds = batch.map((session) => session.sessionID).join(',');
    const url = `${SESSION_DETAILS_BASE}?sessionIds=${encodeURIComponent(sessionIds)}&workflowApiToken=${encodeURIComponent(workflowApiToken)}&ver=${encodeURIComponent(ver)}`;
    const response = await page.request.get(url, { headers: detailHeaders });
    const json = await response.json();
    const payload = json?.data?.data || [];
    detailResponses.push({ requested: batch.length, returned: payload.length, url });
    detailedSessions.push(...payload);
  }

  const detailedById = new Map(detailedSessions.map((session) => [session.sessionID, session]));
  const normalized = dedupedCatalogSessions.map((session) => normalizeSession(detailedById.get(session.sessionID) || session, CATALOG_URL));

  fs.writeFileSync(path.join(RAW_DIR, 'widget_config.json'), JSON.stringify(widgetConfigJson, null, 2));
  fs.writeFileSync(path.join(RAW_DIR, 'sessions_api.json'), JSON.stringify({ total, pageSize, pagesCaptured: pagedResponses.length, responses: pagedResponses }, null, 2));
  fs.writeFileSync(path.join(RAW_DIR, 'session_details.json'), JSON.stringify({ batches: detailResponses, sessions: detailedSessions }, null, 2));
  fs.writeFileSync(path.join(NORMALIZED_DIR, 'sessions.json'), JSON.stringify(normalized, null, 2));
  fs.writeFileSync(path.join(NORMALIZED_DIR, 'sample_sessions.json'), JSON.stringify(normalized.slice(0, 5), null, 2));
  fs.writeFileSync(path.join(ANALYSIS_DIR, 'summary.md'), buildSummary({ normalized, listingCount: rawCatalogListings.length, pageCount: pagedResponses.length, pageSize, rfApiProfileId, rfWidgetId, detailBatchCount: detailResponses.length, detailSessionCount: detailedSessions.length }));
  fs.writeFileSync(path.join(DOCS_DIR, 'api-notes.md'), [
    '# Snowflake Summit 2024 catalog API notes',
    '',
    `- page: ${CATALOG_URL}`,
    `- main catalog API: POST ${SESSIONS_API_URL}`,
    `- widget config API: POST ${WIDGET_CONFIG_URL}`,
    `- secondary detail API: GET ${SESSION_DETAILS_BASE}`,
    `- observed rfApiProfileId: ${rfApiProfileId}`,
    `- observed rfWidgetId: ${rfWidgetId}`,
    `- observed workflowApiToken: ${workflowApiToken}`,
    '',
    '## Required browser-observed headers/tokens',
    '- `rfApiProfileId`',
    '- `rfWidgetId`',
    '- `rfcsrf` (for `flow/common/sessions/bysessionids`)',
    '',
    '## Main catalog request body',
    '```',
    'tab.sessioncatalogtab=1714168666431001NNiH&type=session&browserTimezone=America/Los_Angeles&catalogDisplay=grid',
    '```',
    '',
    '## Practical conclusion',
    '- The public catalog is still deeply scrapable in 2024.',
    '- The best practical path is: observe public browser headers/tokens, paginate `api/sessions`, then batch-enrich unique session ids through `flow/common/sessions/bysessionids`.',
    '- Treat the detail endpoint as opportunistic public enrichment rather than a guaranteed stable contract.',
    '',
  ].join('\n'));
  fs.writeFileSync(path.join(DOCS_DIR, 'discovery.md'), [
    '# Snowflake Summit 2024 discovery notes',
    '',
    '## Entry point',
    `- ${CATALOG_URL}`,
    '',
    '## What worked',
    '- The public catalog page is still live and accessible without login.',
    '- Browser network inspection shows the page calling a public RainFocus sessions API at `POST https://events.summit.snowflake.com/api/sessions`.',
    '- That API paginates with `from=<offset>` and exposes the full public catalog, including times, rooms, speaker records, and attribute buckets.',
    '- The same live page also calls `GET /flow/common/sessions/bysessionids` with a valid `rfcsrf` token, and that endpoint can be replayed to enrich deduplicated session ids.',
    '',
    '## What did not work cleanly',
    '- Static HTML alone does not expose the RainFocus request headers used by the public JSON APIs.',
    '- The detail endpoint depends on a live `rfcsrf` token from the browser session, so bare replay without a prior browser step is brittle.',
    '',
    '## Practical conclusion',
    'The deepest practical public path for Snowflake Summit 2024 is browser-backed: observe headers/tokens from the public catalog, paginate the public catalog API, then optionally enrich the deduplicated session ids via `bysessionids` from the same page session. That is implemented in `../scripts/fetch_catalog.js`.',
    '',
  ].join('\n'));
  fs.writeFileSync(path.join(DOCS_DIR, 'proof-of-scrape.md'), [
    '# Proof of scrape',
    '',
    'We verified that the Snowflake Summit 2024 public session catalog is still available and can be captured without login.',
    '',
    'Current status:',
    '- proof of public catalog availability: yes',
    '- proof of deeper public API path: yes',
    '- proof of secondary public detail enrichment: yes',
    '- proof of structured repeatable extraction: yes',
    '',
    'Evidence committed in this tree:',
    '- `raw/catalog.html`',
    '- `raw/widget_config.json`',
    '- `raw/sessions_api.json`',
    '- `raw/session_details.json`',
    '- `normalized/sessions.json`',
    '- `analysis/summary.md`',
    '',
    'Scope note:',
    '- this is a public catalog + public detail capture from unauthenticated browser traffic',
    '- it does not claim attendee-only or admin-only access',
    '- the detail endpoint still depends on browser-observed public tokens, so the scripted approach keeps that browser step explicit',
    '',
  ].join('\n'));

  console.log(`Captured ${rawCatalogListings.length} catalog listings / ${normalized.length} unique sessions across ${pagedResponses.length} API page(s) to ${path.join(NORMALIZED_DIR, 'sessions.json')}`);
  await browser.close();
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
