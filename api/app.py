from flask import Flask
from dotenv import load_dotenv

from db.db_config import Base

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World!"


if __name__ == "__main__":
  load_dotenv()
  app.run(debug=True)