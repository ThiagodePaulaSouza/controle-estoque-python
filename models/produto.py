class Produto:
  def __init__(self, id, nome, fornecedor, quantidade_minima):
    self.__id = id
    self.__nome = nome
    self.__fornecedor = fornecedor
    self.__quantidade_minima = quantidade_minima
    self.__quantidade_atual = 0
    
  @property
  def id(self):
    return self.__id

  @property
  def nome(self):
    return self.__nome

  @property
  def fornecedor(self):
    return self.__fornecedor
  
  @property
  def quantidade_minima(self):
    return self.__quantidade_minima
  
  @property
  def quantidade_atual(self):
    return self.__quantidade_atual

  def adicionar_estoque(self, quantidade):
    self.__quantidade_atual += quantidade

  def retirar_estoque(self, quantidade):
    self.__quantidade_atual -= quantidade

  def atualizar_produto(self, nome, fornecedor, quantidade_minima):
    self.__nome = nome
    self.__fornecedor = fornecedor
    self.__quantidade_minima = quantidade_minima
    return

  def gerar_lista_campos_arquivo(self):
    return [
        self.id,
        self.nome,
        self.fornecedor,
        self.quantidade_minima,
        self.quantidade_atual
    ]
  
  def gerar_produto_pela_linha(self, linha_dict):
    prd = Produto( int( linha_dict['id'] ), linha_dict['nome'], linha_dict['fornecedor'], float( linha_dict['quantidade_minima'] ) )
    prd.adicionar_estoque( float( linha_dict['quantidade_atual'] ) )
    return prd

  def __str__(self):
    return f"Id: {self.id} | Nome: {self.nome} | Fornecedor: {self.fornecedor} | Quantidade mínima: {self.quantidade_minima} | Estoque atual: {self.quantidade_atual}"