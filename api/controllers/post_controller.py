from flask import Blueprint, jsonify, request
import logging

from db.db_config import Session
from middleware import authenticated
from service.post_service import PostService

app_posts = Blueprint('posts', __name__)
post_service = PostService(session=Session)

@app_posts.route("/api/v1/posts/create", methods=["POST"])
@authenticated
def create_post():
  data = request.get_json()
  post = post_service.insert(data)
  if not post:
    return jsonify({"message": "An error occured, check logs for more info"}), 500
  return jsonify({'message': 'Post created successfully'}), 201


@app_posts.route("/api/v1/posts/get_all", methods=["GET"])
@authenticated
def get_all_posts():
  try:
    posts = post_service.get_all()
  except Exception as ex:
    return jsonify({"message": f"An error occured, message: {ex}"}), 500
  return jsonify({"posts": [post.to_dict() for post in posts]}), 200


@app_posts.route("/api/v1/posts/get", methods=["GET"])
@authenticated
def get_post_by_id():
  post_id = request.args.get('id')
  if not post_id:
    logging.error("/api/v1/posts/get expects an `id` query parameter but None was found")
    return jsonify({"message": "An error occured, check logs for more info"}), 500
  posts = post_service.get_by_id(post_id)
  if not posts:
    return jsonify({"posts": None}), 200
  return jsonify({"posts": posts.to_dict()}), 200


@app_posts.route("/api/v1/posts/remove", methods=["DELETE"])
@authenticated
def delete_post():
  post_id = request.args.get('id')
  if not post_id:
    logging.error("/api/v1/posts/remove expects an `id` query parameter but None was found")
    return jsonify({"message": "An error occured, check logs for more info"}), 500
  posts = post_service.delete(post_id)
  if not posts:
    return jsonify({"message": f"an error occured while trying to remove post with id: {post_id}"}), 500
  return jsonify({"message": "post deleted"}), 200


@app_posts.route("/api/v1/posts/update", methods=["PUT"])
@authenticated
def update_post():
  data = request.get_json()
  to_update = post_service.update(data)
  if not to_update:
    return jsonify({"message": f"an error occured while trying to update the post"}), 500
  return jsonify({"message": "post updated"}), 200