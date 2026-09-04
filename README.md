# Faculty AI Explorer — Python wrapper around the working HTML

This version deliberately does **not** re-implement authentication in Python.
It serves the already-working HTML pages unchanged so the same Supabase logic is used.

- `/` serves `public/index.html`
- `/admin/` serves `public/admin.html`
- Admin login uses the existing database User ID + Password flow via the Supabase RPC `verify_admin_login`.

## Run on macOS

```bash
cd faculty_ai_python_working_html
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m flask --app app run --debug --port 5001
```

Open:
- http://127.0.0.1:5001/
- http://127.0.0.1:5001/admin/

## Important

Use the **same User ID + Password** that works in `Admin_Users_Hashed_Password.html`.
Do not use email login for this version.

If the database RPC/table setup has not been run, run `database_setup.sql` in Supabase SQL Editor first.
