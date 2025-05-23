class Configurations():
  def __init__(self):
    self.__file_output = './out/estoque.csv'

  @property
  def arquivo_saida(self):
    return self.__file_output