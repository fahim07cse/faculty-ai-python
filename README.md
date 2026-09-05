# Faculty AI Explorer — Python/Flask Security Version

This package serves the existing Faculty AI Explorer and the latest secure Admin HTML from Flask.

## Local run (Mac)

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m flask --app app run --debug --port 5001
```

Open:
- Main site: http://127.0.0.1:5001/
- Admin: http://127.0.0.1:5001/admin/

## Render

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn app:app
```

## Included admin protections

- Existing hashed-password Supabase RPC login
- Excel preview/import
- Exact duplicate Excel import blocking
- Blank Excel cells do not overwrite existing database values
- Auto logout after inactivity
- Login-attempt temporary lockout
- URL/query/hash cleanup
- No-cache browser headers
- Anti-framing and basic browser security headers

The Supabase publishable key remains browser-visible by design. Security for database access must still be enforced with Supabase RLS/RPC permissions. Never place a Supabase service-role key in these HTML files.
