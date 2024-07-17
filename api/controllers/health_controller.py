from flask import Blueprint

app_health = Blueprint('health', __name__)

@app_health.route("/api/v1/posts/health")
def health():
  return {"status": 200, "controller": "posts"}