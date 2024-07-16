from abc import ABC, abstractmethod

class CrudService(ABC):

  def __init__(self):
    pass

  @abstractmethod
  def insert(self, dto):
    raise NotImplementedError()
  
  @abstractmethod
  def get_all(self):
    raise NotImplementedError()
  
  @abstractmethod
  def get_by_id(self, id):
    raise NotImplementedError()
  
  @abstractmethod
  def update(self, dto):
    raise NotImplementedError()
  
  @abstractmethod
  def delete(self, id):
    raise NotImplementedError()
