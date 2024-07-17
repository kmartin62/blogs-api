from flask import Flask, jsonify, make_response, request
import logging
from dto.user import UserDto
from middleware import authenticated
from utils import encode_jwt_token
from service.user_service import UserService
from db.db_config import Session
from service.post_service import PostService
from werkzeug.security import check_password_hash

app = Flask(__name__)
post_service = PostService(session=Session)
user_service = UserService(session=Session)

@app.route("/api/v1/users/sign_up", methods=["POST"])
def sign_up():
    data = request.get_json()
    inserted_user = user_service.insert(data)
    if not inserted_user:
      return jsonify({"message": "User creation failed"}), 500
    return jsonify({"message": "User created successfully"}), 201


@app.route("/api/v1/users/sign_in", methods=["POST"])
def sign_in():
    data = request.get_json()
    user = user_service.get_by_email(data.get("email"))

    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"message": "Invalid credentials"}), 401
    
    token = encode_jwt_token(user)

    response = make_response()
    response.headers['Authorization'] = f"Bearer {token}"

    return response

@app.route("/api/v1/posts/create", methods=["POST"])
@authenticated
def create_post():
  data = request.get_json()
  post = post_service.insert(data)
  if not post:
    return jsonify({"message": "An error occured, check logs for more info"}), 500
  return jsonify({'message': 'Post created successfully'}), 201


@app.route("/api/v1/posts/get_all", methods=["GET"])
@authenticated
def get_all_posts():
  try:
    posts = post_service.get_all()
  except Exception as ex:
    return jsonify({"message": f"An error occured, message: {ex}"}), 500
  return jsonify({"posts": [post.to_dict() for post in posts]}), 200


@app.route("/api/v1/posts/get", methods=["GET"])
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


@app.route("/api/v1/posts/remove", methods=["DELETE"])
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


@app.route("/api/v1/posts/update", methods=["PUT"])
@authenticated
def update_post():
  data = request.get_json()
  to_update = post_service.update(data)
  if not to_update:
    return jsonify({"message": f"an error occured while trying to update the post"}), 500
  return jsonify({"message": "post updated"}), 200


@app.route("/api/v1/posts/health")
def health():
  return {"status": 200, "controller": "posts"}

if __name__ == "__main__":
  app.run(debug=False)