from models.produto import Produto
from helpers.arquivo_helper import ArquivoHelper
from helpers.validacao_helper import ValidacaoHelper

class GestaoProduto:
    def __init__(self, linhas = None):
        self.__arquivo_helper = ArquivoHelper()

        self.__lista_produtos = []

        self.carregar_produtos_arquivo(self)

    def carregar_produtos_arquivo(self):
        self.__lista_produtos = self.__arquivo_helper.ler_arquivo()

    def salvar_lista_produtos(self):
        self.__arquivo_helper.escrever_arquivo(self.__lista_produtos)

    def get_lista_produtos_quantidade_abaixo_minimo(self):
        return list(filter(
            lambda p: p.quantidade_atual <= p.quantidade_minima,
            self.__lista_produtos
        ))

    def listar_todos_produtos(self):
        print('Lista de produtos cadastrados:')

        for produto in self.__lista_produtos:
            print(produto)

    def pesquisar_produto_nome(self):
        nome = input("Entre com o nome do produto que você deseja visualizar. ")

        produto = self.pesquisar_produto_nome(nome)
        if produto is not None:
            print( produto )

    def pesquisar_produto_nome(self, nome):
        produto_encontrado = list( filter(
            lambda p: p.nome.strip().upper() == nome.strip().upper(), 
            self.__lista_produtos ) )

        if len(produto_encontrado) == 0:
            print('Nenhum produto foi encontrado...')
            return 
        else:    
            return produto_encontrado[0] 

    def pesquisar_produto_por_id(self):

        id = input("Entre com o id do produto que você deseja visualizar. ")

        if not ValidacaoHelper().validar_string_numerica(id):
            print("Digitado valor inválido para o id")
            return 

        id = int(id)

        produto = self.pesquisar_produto_por_id(id)
        if produto is not None:    
            print( produto )

    def pesquisar_produto_por_id(self, id):
        produto_encontrado = list( filter(
            lambda p: p.id == int(id), 
            self.__lista_produtos ) )

        if len(produto_encontrado) == 0:
            print('Nenhum produto foi encontrado...')
            return None
        else:    
            return produto_encontrado[0]


    def cadastrar_produto(self):
        nome = print("Entre com o nome do produto. ")

        produto = self.pesquisar_produto_nome(nome)
        if produto is not None:
            print("Já existe um produto cadastrado com o nome digitado")
            return

        fornecedor = print("Entre com o nome do fornecedor. ")

        quantidade_minima = print("Entre com a quantidade mínima para o produto. ")

        if not ValidacaoHelper().validar_string_numerica(quantidade_minima):
            print("Digitado valor inválido para a quantidade mínima")
            return 

        quantidade_minima = float(quantidade_minima)

        maior_id = max( list(map( lambda p: p.id, self.__lista_produtos )) )

        self.__lista_produtos.append( 
            Produto(maior_id + 1, nome, fornecedor, quantidade_minima)
        )

        self.salvar_lista_produtos()

        print(f"Produto cadastrado com sucesso! {produto}")

    def editar_produto(self):

        id = input("Entre com o id do produto que você deseja editar. ")

        if not ValidacaoHelper().validar_string_numerica(id):
            print("Digitado valor inválido para o id")
            return 

        id = int(id)

        produto = self.pesquisar_produto_por_id(id)
        if produto is None:
            print('Nenhum produto foi encontrado...')
            return

        print(f"Produto encontrado. Dados atuais: {produto}")

        nome = print("Entre com o novo nome do produto. ")

        produto = self.pesquisar_produto_nome(nome)
        if produto is not None:
            print("Já existe um produto cadastrado com o nome digitado")
            return

        fornecedor = print("Entre com o nome do novo fornecedor. ")

        quantidade_minima = print("Entre com a nova quantidade mínima para o produto. ")

        if not ValidacaoHelper().validar_string_numerica(quantidade_minima):
            print("Digitado valor inválido para a quantidade mínima")
            return 

        quantidade_minima = float(quantidade_minima)
        
        produto.atualizar_produto(nome, fornecedor, quantidade_minima)

        self.salvar_lista_produtos()

        print(f"Produto editado com sucesso! {produto}")

    def deletar_produto(self):

        id = input("Entre com o id do produto que você deseja excluir. ")

        if not ValidacaoHelper().validar_string_numerica(id):
            print("Digitado valor inválido para o id")
            return 

        id = int(id)

        produto = self.pesquisar_produto_por_id(id)
        if produto is None:
            print('Nenhum produto foi encontrado...')
            return

        self.__lista_produtos = list(filter(
            lambda p: p.id != int(id),
            self.__lista_produtos
        ))

        self.salvar_lista_produtos()

        print("Produto excluído com sucesso!")

