from db.model.category import Category
from db.model.tag import Tag
from dto.post import PostDto
from sqlalchemy.exc import NoResultFound
import logging

def generate_tag_models(dto_tags, session):
  tags = list()
  for t in dto_tags:
    try:
      tag = session.query(Tag).filter_by(id=t.get('id')).one()
      tags.append(tag)
    except NoResultFound as no_result_found:
      logging.error(f"A NoResultFound error. Error message: {repr(no_result_found)}. Object received: {dto_tags}")
      return None
    except Exception as ex:
      logging.error(f"An Exception caught. Error message: {repr(ex)}. Object received: {dto_tags}")
      return None
  return tags


def generate_category_model(dto_category, session):
  try:
    category = session.query(Category).filter_by(id=dto_category.get('id')).one()
    return category
  except NoResultFound as no_result_found:
    logging.error(f"A NoResultFound error. Error message: {repr(no_result_found)}. Object received: {dto_category}")
    session.rollback()
    return None
  except Exception as ex:
    logging.error(f"An Exception caught. Error message: {repr(ex)}. Object received: {dto_category}")
    session.rollback()
    return None