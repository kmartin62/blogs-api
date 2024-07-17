from db.model.user import User
from dto.user import UserDto, UserSignIn
from service.service_templ import CrudService
import logging
from werkzeug.security import generate_password_hash

class UserService(CrudService):

  def __init__(self, session):
    self.session = session

  def insert(self, dto):
    try:
      user_dto = UserDto(**dto)
      user_to_insert = User(
        first_name = user_dto.first_name,
        last_name = user_dto.last_name,
        email = user_dto.email,
        middle_name = user_dto.middle_name,
        password = generate_password_hash(user_dto.password)
      )

      self.session.add(user_to_insert)
      self.session.commit()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}. Object received: {dto}")
      return None
    finally:
      self.session.close()
    return user_to_insert
  
  
  def get_by_email(self, data):
    try:
      signed_user = UserSignIn(**data)
      user = self.session.query(User).filter(User.email == signed_user.email).first()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}")
      return None
    finally:
      self.session.close()
    return user

  
  def delete(self, id):
    pass
  
  def get_all(self):
    pass

  def get_by_id(self, id):
    pass
  
  def update(self, dto):
    pass