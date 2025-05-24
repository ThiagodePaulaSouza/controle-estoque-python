class Configurations():
  def __init__(self):
    self.__file_output = './out/estoque.csv'

  @property
  def arquivo_saida(self) -> str:
    return self.__file_output