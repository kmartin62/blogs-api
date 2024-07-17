from flask import Flask
from controllers.post_controller import app_posts
from controllers.user_controller import app_users
from controllers.health_controller import app_health

app = Flask(__name__)

app.register_blueprint(app_posts)
app.register_blueprint(app_users)
app.register_blueprint(app_health)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=False)