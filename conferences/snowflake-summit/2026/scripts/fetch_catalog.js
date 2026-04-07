#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const RAW_DIR = path.join(ROOT, 'raw');
const NORMALIZED_DIR = path.join(ROOT, 'normalized');
const ANALYSIS_DIR = path.join(ROOT, 'analysis');
const DOCS_DIR = path.join(ROOT, 'docs');

for (const dir of [RAW_DIR, NORMALIZED_DIR, ANALYSIS_DIR, DOCS_DIR]) {
  fs.mkdirSync(dir, { recursive: true });
}

function pick(headers, key) {
  for (const [k, v] of Object.entries(headers || {})) {
    if (k.toLowerCase() === key.toLowerCase()) return v;
  }
  return undefined;
}

function normalizeSession(session) {
  const times = (session.times || []).map((time) => ({
    session_time_id: time.sessionTimeID || null,
    date: time.date || null,
    date_formatted: time.dateFormatted || null,
    day_name: time.dayName || null,
    start_time: time.startTime || null,
    start_time_formatted: time.startTimeFormatted || null,
    end_time: time.endTime || null,
    end_time_formatted: time.endTimeFormatted || null,
    utc_start_time: time.utcStartTime || null,
    utc_end_time: time.utcEndTime || null,
    room: time.room || null,
    room_id: time.roomId || null,
    length_minutes: time.length ?? null,
    in_person_time: time.inPersonTime ?? null,
    virtual_time: time.virtualTime ?? null,
    view_access_public: time.viewAccessPublic ?? null,
  }));

  const speakers = (session.participants || []).map((speaker) => ({
    speaker_id: speaker.speakerId || null,
    full_name: speaker.preferredFullName || speaker.globalPreferredFullName || speaker.fullName || speaker.globalFullName || null,
    first_name: speaker.preferredFirstname || speaker.firstName || null,
    last_name: speaker.lastName || null,
    company: speaker.companyName || speaker.globalCompany || null,
    job_title: speaker.jobTitle || speaker.globalJobtitle || null,
    bio: speaker.bio || speaker.globalBio || null,
    photo_url: speaker.photoURL || null,
    linkedin: speaker.linkedIn || null,
    roles: speaker.roles || null,
  }));

  const attributes = {};
  for (const attr of session.attributevalues || []) {
    const key = attr.attributeCode || attr.attribute || attr.filterID || attr.name || attr.label;
    const value = attr.value ?? attr.displayValue ?? attr.attributeValue ?? attr.code ?? attr.name;
    if (!key || value == null) continue;
    if (!attributes[key]) attributes[key] = [];
    if (!attributes[key].includes(value)) attributes[key].push(value);
  }

  return {
    session_id: session.sessionID || null,
    external_id: session.externalID || null,
    code: session.code || null,
    code_id: session.code_id || null,
    title: session.title || null,
    abstract: session.abstract || null,
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
    virtual_time: session.virtualTime ?? null,
    use_waiting_list: session.useWaitingList ?? null,
    speakers,
    times,
    attributes,
  };
}

function buildSummary(normalized, pages, headers) {
  const byType = new Map();
  const byDay = new Map();
  let speakerCount = 0;

  for (const session of normalized) {
    byType.set(session.session_type || 'Unknown', (byType.get(session.session_type || 'Unknown') || 0) + 1);
    for (const time of session.times) {
      byDay.set(time.date || 'Unknown', (byDay.get(time.date || 'Unknown') || 0) + 1);
    }
    speakerCount += session.speakers.length;
  }

  const topTypes = [...byType.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10);
  const days = [...byDay.entries()].sort((a, b) => a[0].localeCompare(b[0]));

  return [
    '# Snowflake Summit 2026 catalog snapshot',
    '',
    `- captured_at_utc: ${new Date().toISOString()}`,
    `- total_sessions: ${normalized.length}`,
    `- api_page_count: ${pages.length}`,
    `- total_speaker_links: ${speakerCount}`,
    `- rf_api_profile_id: ${headers.rfApiProfileId}`,
    `- rf_widget_id: ${headers.rfWidgetId}`,
    '',
    '## Sessions by type',
    ...topTypes.map(([type, count]) => `- ${type}: ${count}`),
    '',
    '## Scheduled slots by day',
    ...days.map(([day, count]) => `- ${day}: ${count}`),
    '',
  ].join('\n');
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const requestMatches = [];

  page.on('request', (request) => {
    const url = request.url();
    if (url.includes('/api/sessions') || url.includes('/api/widgetConfig')) {
      requestMatches.push({
        url,
        method: request.method(),
        headers: request.headers(),
        postData: request.postData(),
      });
    }
  });

  await page.goto('https://reg.snowflake.com/flow/snowflake/summit26/sessions/page/catalog', {
    waitUntil: 'networkidle',
    timeout: 120000,
  });
  await page.waitForTimeout(5000);

  const sessionRequest = requestMatches.find((req) => req.url.includes('/api/sessions'));
  const widgetRequest = requestMatches.find((req) => req.url.includes('/api/widgetConfig'));
  if (!sessionRequest || !widgetRequest) {
    throw new Error('Could not observe catalog API requests in the browser session');
  }

  const rfApiProfileId = pick(sessionRequest.headers, 'rfapiprofileid');
  const rfWidgetId = pick(sessionRequest.headers, 'rfwidgetid');
  if (!rfApiProfileId || !rfWidgetId) {
    throw new Error('Missing RainFocus widget headers from observed API request');
  }

  const headers = {
    'rfApiProfileId': rfApiProfileId,
    'rfWidgetId': rfWidgetId,
    'referer': 'https://reg.snowflake.com/',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': pick(sessionRequest.headers, 'user-agent') || 'Mozilla/5.0',
  };

  const firstSessionsResponse = await page.request.post('https://events.summit.snowflake.com/api/sessions', {
    headers,
    form: {
      type: 'session',
      browserTimezone: 'America/Los_Angeles',
      catalogDisplay: 'grid',
    },
  });

  const widgetConfigResponse = await page.request.post('https://events.summit.snowflake.com/api/widgetConfig', {
    headers: {
      ...headers,
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    },
  });

  const firstSessionsJson = await firstSessionsResponse.json();
  const widgetConfigJson = await widgetConfigResponse.json();

  if (firstSessionsJson.responseCode !== '0') {
    throw new Error(`Unexpected sessions API response: ${JSON.stringify(firstSessionsJson).slice(0, 500)}`);
  }

  const firstSection = (firstSessionsJson.sectionList || [])[0] || {};
  const total = Number(firstSessionsJson.totalSearchItems || firstSection.total || 0);
  const pageSize = Number(firstSection.size || firstSection.numItems || 50);
  const pagedResponses = [firstSessionsJson];
  const rawSessions = [...(firstSection.items || [])];

  for (let from = rawSessions.length; from < total; from += pageSize) {
    const response = await page.request.post('https://events.summit.snowflake.com/api/sessions', {
      headers,
      form: {
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
    rawSessions.push(...(json.items || []));
  }

  const dedupedSessions = Array.from(new Map(rawSessions.map((session) => [session.sessionID, session])).values());
  const normalized = dedupedSessions.map(normalizeSession);

  fs.writeFileSync(path.join(RAW_DIR, 'widget_config.json'), JSON.stringify(widgetConfigJson, null, 2));
  fs.writeFileSync(path.join(RAW_DIR, 'sessions_api.json'), JSON.stringify({
    total,
    pageSize,
    pagesCaptured: pagedResponses.length,
    responses: pagedResponses,
  }, null, 2));
  fs.writeFileSync(path.join(NORMALIZED_DIR, 'sessions.json'), JSON.stringify(normalized, null, 2));
  fs.writeFileSync(path.join(ANALYSIS_DIR, 'summary.md'), buildSummary(normalized, pagedResponses, { rfApiProfileId, rfWidgetId }));
  fs.writeFileSync(path.join(DOCS_DIR, 'api-notes.md'), [
    '# Snowflake Summit 2026 catalog API notes',
    '',
    `- page: https://reg.snowflake.com/flow/snowflake/summit26/sessions/page/catalog`,
    `- main catalog API: POST https://events.summit.snowflake.com/api/sessions`,
    `- widget config API: POST https://events.summit.snowflake.com/api/widgetConfig`,
    `- observed rfApiProfileId: ${rfApiProfileId}`,
    `- observed rfWidgetId: ${rfWidgetId}`,
    '',
    '## Required headers',
    '- `rfApiProfileId`',
    '- `rfWidgetId`',
    '- browser-like `referer` / `user-agent`',
    '',
    '## Main catalog request body',
    '```',
    'type=session&browserTimezone=America/Los_Angeles&catalogDisplay=grid',
    '```',
    '',
    '## Notes',
    '- Static HTML is not enough; the real catalog is hydrated client-side.',
    '- The public catalog returned 319 sessions during this capture.',
    '- A raw `requests.post()` without the observed RainFocus headers returns `Required parameter missing: apiProfile`.',
    '- Some RainFocus `flow/common/sessions/*` endpoints also expect CSRF (`rfcsrf`) and are better treated as secondary/detail endpoints.',
    '',
  ].join('\n'));

  console.log(`Captured ${normalized.length} sessions across ${pagedResponses.length} API page(s) to ${path.join(NORMALIZED_DIR, 'sessions.json')}`);
  await browser.close();
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
