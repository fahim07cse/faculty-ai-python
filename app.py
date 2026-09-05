from pathlib import Path
from flask import Flask, send_from_directory, make_response

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"

app = Flask(__name__)


def secure_html(filename: str):
    response = make_response(send_from_directory(PUBLIC_DIR, filename))
    # Basic server-side browser protections. The admin page also contains
    # its own client-side session/inactivity protections.
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    return response


@app.get("/")
def home():
    return secure_html("index.html")


@app.get("/admin")
@app.get("/admin/")
def admin():
    # Latest secure admin HTML: hashed-password RPC login, Excel preview/import,
    # duplicate-file blocking, inactivity logout and URL/session protections.
    return secure_html("admin.html")


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
