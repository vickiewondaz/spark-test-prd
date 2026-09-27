# SPARK — implementation.md (local test run)

Source: `SPARK TEST PRD.docx` (174 paras) + `PRD.md`.
One-line: SPARK is an AI-powered idea-to-action companion that turns unfinished ideas into practical projects.
Flow: IDEA → CLARIFY → PLAN → BUILD → TRACK → COMPLETE.
Principle: Clarity → One next step → Progress.

## 0. Locked decisions
- Framework: Django 5 + Tailwind + HTMX (Python 3.14, `python manage.py runserver`, no Node — local node binary is 0B).
- Database: SQLite `db.sqlite3` (Django ORM, zero install).
- Auth: Django built-in (`django.contrib.auth`, sessions, local only).
- Files: local `MEDIA_ROOT=media/`, `Attachment` model with UUID names.
- Scope: LOCAL TEST RUN only. No Docker, cloud DB, hosted auth, or deploy. `.venv/`, `db.sqlite3`, `media/*` git-ignored.
- Theme: warm/vibrant/hopeful sunrise (cream `#FFF7ED`, ember `#EA580C`→`#C2410C`, honey `#F59E0B`, peach `#FDBA74`, espresso text `#431407`).
- Mobile-first (mandatory): base styles = small screens (1-col, 32px hero, 48px touch targets, 16px inputs to stop iOS zoom); scale up with `min-width:660px` (2-col) and `min-width:960px` (3/4-col, 44px hero). No `max-width` desktop-first queries. Django templates follow the same rule.

## 1. MVP scope (PRD §6)
1. Auth 2. Create idea (title+desc) 3. AI clarification (5 questions) 4. Action plan (5–10 tasks) 5. Dashboard (tasks+progress) 6. AI assistant (per-project Q&A) 7. Checklist toggle 8. History. Plus: Next Action highlight, stage machine Ideas→Planning→Building→Testing→Completed, Notes, Milestones, metrics (PRD §8).

## 2. Architecture (as scaffolded)
```
browser → spark/urls.py (/, /admin/, /accounts/, /ideas/, /dashboard/, /uploads/ + media in DEBUG)
accounts/ (signup via UserCreationForm, LoginView/LogoutView, templates/accounts/)
ideas/ (Idea, Task, Note, Milestone models + migrations/0001; /ideas/, /ideas/<id>/, user-scoped queries)
dashboard/ (user's 20 recent ideas, templates/dashboard/)
uploads/ (Attachment FileField → media/uploads/<uuid>.<ext>, migrations/0001)
templates/ + db.sqlite3 + media/.gitkeep
```

## 3. Technical requirements
- macOS, Python 3.14, sqlite3 3.43.2, Django 5.2.17 (`requirements.txt`), modern mobile + desktop browser.
- Run: `python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt && ./.venv/bin/python manage.py migrate && ./.venv/bin/python manage.py runserver`.
- Verified: `manage.py check` clean. Design preview: `design.html` (Polaris tokens, warm theme, mobile-first) — open with `open design.html`.

## 4. Ordered phases (each ends with a runnable output)

### Phase 0 — Foundation ✅ DONE (`85ecaa8`)
Goal: runnable skeleton. Outputs: `manage.py`, `spark/settings.py` (SQLite, media, login redirects, templates dir), `spark/urls.py`, 4 apps, `requirements.txt`, `.gitignore`, `media/.gitkeep`, applied migrations. Accept: `check` clean, `migrate` ok, `/` + `/admin/` load.

### Phase 1 — Auth + Idea Capture + History
Tasks: signup/login/logout templates (mobile-first, 1-col, 48px buttons); idea create form (title+desc only); history list.
Outputs: `templates/accounts/*`, `templates/ideas/index.html`, idea create view + `POST /ideas/new`, `Idea(user,title,description,stage)` CRUD user-scoped. Accept: new user creates "solar charging station" and sees it in History on phone + desktop.

### Phase 2 — AI Clarifier + Action Plan + Next Action
Tasks: `ai/prompts/clarify.txt` (what/problem/who/why/simplest), `ai/prompts/plan.txt` (5–10 tasks); manual fallback when no key.
Outputs: `POST /ideas/<id>/clarify`, `POST /ideas/<id>/plan`, `Clarification(idea,qa_json)`, `Task(idea,title,done,order)`, clarify Q&A UI + checklist UI + "Your Next Action Today" card (from `design.html`). Accept: graphic-design example yields structured problem/user/solution + 5–7 tasks + one next action.

### Phase 3 — Track: Dashboard, Progress, Notes, Milestones
Tasks: stage auto-derivation from tasks; checklist toggle; notes (text+file); milestones.
Outputs: `/dashboard/` (progress %, stage badges), `PATCH /tasks/<id>/toggle`, `Note`, `Milestone`, `Attachment` upload wired to idea detail; all mouse + touch friendly (48px targets). Accept: completing tasks moves Ideas→…→Completed and updates %.

### Phase 4 — AI Project Assistant
Tasks: context injection (idea+tasks+notes) + streaming answer + suggested prompts.
Outputs: `ai/prompts/assistant.txt`, `POST /ideas/<id>/ask`, chat drawer on idea detail. Accept: "What next?" answers from that idea's real tasks, works on mobile drawer.

### Phase 5 — Metrics + Launch-ready (test)
Tasks: event logging + metrics page + polish (empty states, AI-failure handling, mobile pass).
Outputs: `Event(idea,user,type)` for idea_created/plan_generated/first_task_done/project_completed; `/metrics` with 7 PRD numbers; responsive QA at 360px + 1280px. Accept: can answer "did SPARK move user from thinking to doing?" with data.

## 5. Design contract (`design.html`)
Polaris token names, warm values; Inter type scale (hero 32→44px, body 15→16px); buttons (ember primary, white secondary, honey/success/critical variants); inputs (white, tan border, ember focus glow); Next Action sunrise card. Mobile-first verified in browser.

## 6. Git map
`a084a09` docx → `85ecaa8` scaffold+PRD → `4213a45` design preview → `dc21bff` warm theme → `674e25b` PRD change log. This file is next.
