class Configurations():
  def __init__(self):
    self.__file_output = './out/estoque.csv'

  @property
  def file_output(self):
    return self.__file_output