# SPARK — PRD Note (Local Test Run)

Source PRD: `SPARK TEST PRD.docx` in this folder.
One-line definition: SPARK is an AI-powered idea-to-action companion that helps people turn unfinished ideas into practical projects.
Flow: IDEA → CLARIFY → PLAN → BUILD → TRACK → COMPLETE
Principle: Clarity → One next step → Progress

## Decision log (locked for local test)

### 1. Framework: Django 5 + Tailwind + HTMX (Python)
Why:
- Runs now with local Python 3.14, no build step: `python manage.py runserver`.
- Monolith serves UI + API together, fastest for solo local MVP.
- Local `node` binary is 0B/empty, so Next.js would require fixing Node first.
Rejected for now:
- Next.js + TypeScript — better for rich interactive UI / AI streaming / Vercel deploy, heavier + needs Node fix.
- FastAPI + React — better for heavy AI backend, but two apps to run.
- Flask — lighter than Django but auth/ORM/admin must be wired manually.

### 2. Database: SQLite (Django default, `db.sqlite3`)
Why:
- Zero install, `sqlite3` 3.43.2 already present. Django ORM migrates clean.
- File-based, perfect for single-laptop test run.
Rejected for now:
- Postgres via Docker — better for concurrency, full-text search, pgvector AI search. Overkill locally.

### 3. Authentication: Django built-in (`django.contrib.auth`)
Why:
- Fully local: User model, sessions, login/signup, password hashing. No external account.
Rejected for now:
- Clerk / Supabase Auth / Firebase — better for Google login, magic links, reset emails. Requires internet + external service, not local-only.

### 4. File storage: Local filesystem (`MEDIA_ROOT=media/`)
Why:
- Covers PRD Project Notes (photos, docs, interview notes) with `Attachment` model + UUID filenames. Serve via Django in DEBUG.
- Zero setup, move to S3 later via `django-storages` without logic change.
Rejected for now:
- MinIO (local S3) / Supabase Storage / Cloud S3 — better for scale/CDN/multi-server. Overkill for MVP.

### 5. Scope: LOCAL TEST RUN APP only
- No Docker, no cloud DB, no hosted auth, no deploy.
- Run: venv + `pip install django` + `migrate` + `runserver`.
- `db.sqlite3`, `.venv/`, `media/*` are local-only and git-ignored.

## MVP scope (from .docx §6)
1. Auth 2. Create idea 3. AI clarification 4. Action plan 5-10 tasks 5. Dashboard 6. AI assistant 7. Checklist 8. History
Plus: Next Action highlight, Progress Tracker (Ideas→Planning→Building→Testing→Completed), Notes, Milestones, metrics (§8: did user move from thinking to doing?).

## Local layout
```
manage.py, spark/settings.py, spark/urls.py
accounts/ ideas/ dashboard/ uploads/
media/ db.sqlite3 .venv/
requirements.txt README.md .gitignore
```

## Agent change log (in order requested)
1. Linked local folder `/Users/mac/Documents/SPARK TEST PRD` to OpenCode as working dir.
2. Connected folder to GitHub: created public repo `vickiewondaz/spark-test-prd`, `main`, pushed initial `SPARK TEST PRD.docx` (`a084a09`).
3. Read `.docx` PRD (174 paras) and wrote phased implementation plan (Phases 0–5 with concrete outputs).
4. Named local stack: Django 5 + Tailwind + HTMX / SQLite `db.sqlite3` / Django built-in auth / local `media/` — app & DB local only.
5. Explained scaffold = empty runnable skeleton (settings, apps, routes, DB, media).
6. Compared better alternatives: Next.js (rich UI/streaming), FastAPI+React (heavy AI), Postgres (concurrency/search/vectors), Clerk/Supabase (social login), S3/MinIO (scale/CDN) — kept local stack for speed.
7. Locked scope: LOCAL TEST RUN APP, no Docker/cloud/deploy.
8. Scaffolded Django: `spark` project + `accounts, ideas, dashboard, uploads` apps, Idea/Task/Note/Milestone/Attachment models, placeholder views/urls/templates, `requirements.txt`, `.gitignore`; `check` + `migrate` clean (`85ecaa8` pushed).
9. Wrote this PRD.md decision note.
10. Created `design.html`: unique SPARK × Shopify Polaris preview (colors, typography, buttons, inputs) (`4213a45` pushed).
11. Re-themed `design.html` to warm/vibrant/hopeful sunrise: cream `#FFF7ED`, ember `#EA580C`→hover `#C2410C`, honey `#F59E0B`, peach `#FDBA74`, espresso text `#431407` (`dc21bff` pushed).
