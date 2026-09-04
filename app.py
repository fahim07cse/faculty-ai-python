from pathlib import Path
from flask import Flask, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"

app = Flask(__name__)

@app.get("/")
def home():
    # Serve the original working Faculty AI Explorer HTML unchanged.
    return send_from_directory(PUBLIC_DIR, "index.html")

@app.get("/admin")
@app.get("/admin/")
def admin():
    # Serve the original working hashed-password admin HTML unchanged.
    # Login is handled by the existing Supabase RPC: verify_admin_login.
    return send_from_directory(PUBLIC_DIR, "admin.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
