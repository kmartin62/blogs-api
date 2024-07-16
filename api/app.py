from flask import Flask, jsonify, request
import logging

from db.db_config import Session
from service.post_service import PostService
from dto.post import PostDto

app = Flask(__name__)
post_service = PostService(session=Session)

@app.route("/v1/create_post", methods=["POST"])
def create_post():
  data = request.get_json()
  try:
    post = PostDto(**data)
    post_service.insert(post)
  except Exception as ex:
    logging.error(f"An Exception caught. Error message: {repr(ex)}")
    return jsonify({'message': ex}), 500
  return jsonify({'message': 'Post created successfully'}), 201


@app.route("/v1/get_all", methods=["GET"])
def get_all_posts():
  posts = post_service.get_all()
  posts_list = [post.to_dict() for post in posts]
  return jsonify({"posts": posts_list}), 200

@app.route("/health")
def health():
  return {"status": 200}

if __name__ == "__main__":
  app.run(debug=False)