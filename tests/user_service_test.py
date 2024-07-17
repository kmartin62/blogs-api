import unittest

from api.db.db_config import Session
from api.service.user_service import UserService
import os
import json

class TestUserService(unittest.TestCase):
  def __init__(self):
    self.user_service = UserService(session=Session)
    self.user_request = json.load(open(os.path.join("request_json", "user_request.json")))

  def test_post_insertion(self):
    user_request = self.user_request.copy()
    inserted_user = self.user_service.insert(user_request)
    self.assertIsNotNone(inserted_user)

    with self.assertRaises(Exception):
      del user_request["email"]
      del user_request["password"]
      inserted_user = self.user_service.insert(user_request)
      self.assertIsNone(inserted_user)

  def test_post_get_by_email(self):
    user_request = self.user_request.copy()
    inserted_user = self.user_service.insert(user_request)
    self.assertIsNotNone(inserted_user)

    user_by_email = self.user_service.get_by_email(user_request.get("email"))
    self.assertIsNotNone(user_by_email)

    with self.assertRaises(Exception):
      user_by_email = self.user_service.get_by_email("non_existens#mail")
      self.assertIsNotNone(user_by_email)