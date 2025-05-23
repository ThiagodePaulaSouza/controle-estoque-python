from aplicacao.gestao_produto import GestaoProduto
from models.produto import Produto
from helpers.validacao_helper import ValidacaoHelper
from helpers.terminal_helper import TerminalHelper

class GestaoEstoque:
    def __init__(self, gestao_produto):
        self.__gestao_produto = gestao_produto

    def adicionar_ao_estoque(self):
        TerminalHelper.limpar_tela()
        self.__gestao_produto.listar_todos_produtos()

        id = input('Entre com o id do produto cujo estoque será aumentado: ')
        id = id.strip().upper()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("Digitado valor inválido para o id")
            return 

        id = int(id)

        produto = self.__gestao_produto.get_produto_por_id(id)

        if produto is None:
            print("Não foi encontrado um produto com o id digitado.")
            return

        quantidade = input(f'Qual quantidade do produto {produto.nome} deseja adicionar ao estoque? ')

        if not ValidacaoHelper.validar_string_numerica(quantidade):
            print("Quantidade inválida.")
            return

        quantidade = float(quantidade)

        if(quantidade <= 0):
            print('Quantidade inválida. Não é possível adicionar uma quantidade menor ou igual a 0 ao estoque.')
            return

        produto.adicionar_estoque(quantidade)

        self.__gestao_produto.salvar_lista_produtos()

        print('Quantidade adicionada ao estoque do produto com sucesso!')
        print(f"Nova quantidade: { produto.quantidade_atual }")

    def retirar_do_estoque(self):
        self.__gestao_produto.listar_todos_produtos()

        id = input('Entre com o id do produto cujo estoque será subtraído: ')
        id = id.strip().upper()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("Digitado valor inválido para o id")
            return 

        id = int(id)

        produto = self.__gestao_produto.get_produto_por_id(id)

        if produto is None:
            print("Não foi encontrado um produto com o id digitado.")
            return

        quantidade = input(f'Que quantidade do Produto {produto.nome} deseja remover do estoque: ')

        if not ValidacaoHelper.validar_string_numerica(quantidade):
            print("Quantidade inválida.")
            return

        quantidade = float(quantidade)

        if(quantidade <= 0):
            print('Quantidade inválida. Não é possível extrair uma quantidade negativa ou zerada do estoque.')
            return

        if(quantidade >= produto.quantidade_atual):
            print("Não é possível remover essa quantidade do estoque. Não há estoque suficiente.")
            return

        produto.retirar_estoque(quantidade)

        self.__gestao_produto.salvar_lista_produtos()

        print('Quantidade subtraída com sucesso do estoque do Produto!')
        print(f'Quantidade atual: { produto.quantidade_atual }')

    def produtos_com_baixo_estoque(self):
        lista_produtos_baixo_estoque = self.__gestao_produto.get_lista_produtos_quantidade_abaixo_minimo()

        if len(lista_produtos_baixo_estoque) > 0:
            print("ATENÇÃO! Os seguintes produtos estão com estoque menor ou igual à quantidade mínima cadastrada: ")
            print(" ")
            for produto in lista_produtos_baixo_estoque:
                print(produto)

            print(" ")

