import unittest

from api.db.db_config import Session
from api.service.post_service import PostService
import os
import json

class TestPostService(unittest.TestCase):
  def __init__(self):
    self.post_service = PostService(session=Session)
    self.post_request = json.load(open(os.path.join("request_json", "post_request.json")))

  def test_post_insertion(self):
    post_request = self.post_request.copy()
    inserted_post = self.post_service.insert(post_request)
    self.assertIsNotNone(inserted_post)

    with self.assertRaises(Exception):
      del post_request["id"]
      del post_request["title"]
      inserted_post = self.post_service.insert(post_request)
      self.assertIsNone(inserted_post)

  def test_post_deletion(self):
    post_request = self.post_request.copy()
    inserted_post = self.post_service.insert(post_request)
    self.assertIsNotNone(inserted_post)

    random_post = self.post_service.get_all()[0]
    random_post_id = random_post.id

    deleted_post = self.post_service.delete(random_post_id)
    self.assertIsNotNone(deleted_post)

    with self.assertRaises(Exception):
      deleted_post = self.post_service.delete(-99)
      self.assertIsNone(deleted_post)

  def test_post_get_all(self):
    post_request = self.post_request.copy()
    inserted_post = self.post_service.insert(post_request)
    self.assertIsNotNone(inserted_post)

    posts = self.post_service.get_all()
    self.assertGreater(len(posts), 0)

    for post in posts:
      self.post_service.delete(post.id)
    
    posts = self.post_service.get_all()
    self.assertEqual(len(posts), 0)

  def test_post_get_by_id(self):
    post_request = self.post_request.copy()
    inserted_post = self.post_service.insert(post_request)
    self.assertIsNotNone(inserted_post)

    posts = self.post_service.get_all()
    self.assertGreater(len(posts), 0)

    post = posts[0] # random post

    post_by_id = self.post_service.get_by_id(post.id)
    self.assertIsNotNone(post_by_id)

    self.post_service.delete(post.id)

    with self.assertRaises(Exception):
      post_by_id = self.post_service.get_by_id(post.id)
      self.assertIsNone(post_by_id)


  def test_post_update(self):
    post_request = self.post_request.copy()
    inserted_post = self.post_service.insert(post_request)
    self.assertIsNotNone(inserted_post)

    posts = self.post_service.get_all()
    self.assertGreater(len(posts), 0)

    post_request["title"] = "Edited title"

    updated_post = self.post_service.update(post_request)
    self.assertIsNotNone(updated_post)
    self.assertEqual(updated_post.title, "Edited title")

    with self.assertRaises(Exception):
      del post_request["id"]
      del post_request["title"]
      post_by_id = self.post_service.update(post_request)
      self.assertIsNone(post_by_id)