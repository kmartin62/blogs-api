from .utils import generate_category_model, generate_tag_models
from db.model.post import Post
from dto.post import PostDto
from service.service_templ import CrudService
from sqlalchemy.orm import joinedload
import logging
from datetime import datetime
class PostService(CrudService):

  def __init__(self, session):
    self.session = session

  def insert(self, dto):
    try:
      post_dto = PostDto(**dto)
      post_to_insert = Post(
        title = post_dto.title,
        content = post_dto.content,
        created_by = "martin.kostadinov@hotmail.com", #TODO: Change with currently logged in user
      )

      category = generate_category_model(post_dto.category, self.session)
      tags = generate_tag_models(post_dto.tags, self.session)

      post_to_insert.tags = tags
      post_to_insert.category = category

      self.session.add(post_to_insert)
      self.session.commit()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}. Object received: {dto}")
      return None
    finally:
      self.session.close()
    return post_to_insert
  
  def delete(self, id):
    try:
      post = self.session.query(Post).options(joinedload(Post.category), joinedload(Post.tags)).filter(Post.id==id).first()
      self.session.delete(post)
      self.session.commit()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}")
      self.session.rollback()
      return None
    finally:
      self.session.close()
    return post
  
  def get_all(self):
    try:
      posts = self.session.query(Post).all()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}")
      return None
    finally:
      self.session.close()
    return posts

  def get_by_id(self, id):
    try:
      post = self.session.query(Post).filter(Post.id == id).first()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}")
      return None
    finally:
      self.session.close()
    return post
  
  def update(self, dto):

    try:
      post_to_update = self.session.query(Post).filter(Post.id == dto.get("id")).one()

      post_to_update.title = dto.get("title")
      post_to_update.content = dto.get("content")
      post_to_update.updated_at = datetime.now()

      category = generate_category_model(dto.get('category'), self.session)
      post_to_update.category_id = category.id

      tags = generate_tag_models(dto.get("tags"), self.session)
      post_to_update.tags = tags

      self.session.commit()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}")
      return None
    finally:
      self.session.close()
    return post_to_update