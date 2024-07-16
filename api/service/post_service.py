from db.model.category import Category
from db.model.post import Post
from db.model.tag import Tag
from dto.post import PostDto
from service.service_templ import CrudService
from sqlalchemy.exc import NoResultFound
import logging

class PostService(CrudService):

  def __init__(self, session):
    self.session = session

  def insert(self, dto):
    if not isinstance(dto, PostDto):
        raise AssertionError(f"Expected PostDto, got {type(dto)}")
    
    try:
      post_dto = dto
      post_to_insert = Post(
        title = post_dto.title,
        content = post_dto.content,
        created_by = "martin.kostadinov@hotmail.com", #TODO: Change with currently logged in user
      )

      """Move from here"""
      tags = list()
      for tag in post_dto.tags:
        try:
          tag = self.session.query(Tag).filter_by(id=tag.get('id')).one()
          tags.append(tag)
        except NoResultFound as no_result_found:
          logging.error(f"A NoResultFound error. Error message: {repr(no_result_found)}")
          return None
        except Exception as ex:
          logging.error(f"An Exception caught. Error message: {repr(ex)}")
          return None
        
      try:
        category = self.session.query(Category).filter_by(id=post_dto.category.get('id')).one()
      except NoResultFound as no_result_found:
        logging.error(f"A NoResultFound error. Error message: {repr(no_result_found)}")
        return None
      except Exception as ex:
        logging.error(f"An Exception caught. Error message: {repr(ex)}")
        return None
      """To here in a tag and category service"""

      post_to_insert.tags = tags
      post_to_insert.category = category

      self.session.add(post_to_insert)
      self.session.commit()
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}")
      return None
    finally:
      self.session.close()
  
  def delete(self, id):
    return super().delete()
  
  def get_all(self):
    try:
      posts = self.session.query(Post).all()
    except Exception as ex:
      raise
    finally:
      self.session.close()
    return posts

  def get_by_id(self, id):
    return super().get_by_id()
  
  def update(self, dto):
    return super().update()