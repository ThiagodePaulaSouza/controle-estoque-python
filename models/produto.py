class Produto:
  def __init__(self, id, nome, quantidade_minima):
    self.__id = id
    self.__nome = nome
    self.__quantidade_minima = quantidade_minima
    self.__quantidade_atual = 0

  @property
  def nome(self):
    return self.__nome
  
  @property
  def quantidade_minima(self):
    return self.__quantidade_minima
  
  @property
  def quantidade_atual(self):
    return self.__quantidade_atual
  
  def atualizar_produto(self, nome, quantidade_minima, quantidade_atual):
    self.__nome = nome
    self.__quantidade_minima = quantidade_minima
    self.__quantidade_atual = quantidade_atual
    return