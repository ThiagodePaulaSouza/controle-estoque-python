from aplicacao.produto_app import ProdutoApp
from models.produto import Produto

class EstoqueApp:
    def __init__(self):
        self.__produto_app__ = ProdutoApp()
        pass

    def adicionar_ao_estoque(self):
        self.__produto_app__.listar_todos_produtos()

        produto_selecionado = input('Selecione qual produto deseja adicionar ao estoque (id): ')
        produto_selecionado.strip().upper()

        produto = self.__produto_app__.seleciona_produto_por_id(produto_selecionado)

        quantidade = input(f'Quantos do Produto {produto.nome} deseja adicionar ao estoque (unidade): ')
        quantidade = int(quantidade)

        if(quantidade <= 0):
            print('Quantidade inválida...')
            return

        # TODO acessa o csv e adicionar mais um produto ao estoque

        print('Produto(s) adicionado ao estoque com sucesso!')

    def remover_do_estoque(self):
        self.__produto_app__.listar_todos_produtos()

        produto_selecionado = input('Selecione qual produto deseja adicionar ao estoque (id): ')
        produto_selecionado.strip().upper()

        produto = self.__produto_app__.seleciona_produto_por_id(produto_selecionado)

        quantidade = input(f'Quantos do Produto {produto.nome} deseja remover do estoque (unidade): ')
        quantidade = int(quantidade)

        if(quantidade <= 0):
            print('Quantidade inválida...')
            return

        if(quantidade >= produto.quantidade_atual):
            # TODO acessa o csv e remove todo o estoque desse produto
            pass

        # TODO acessa o csv e remove a quantidade do estoque desse produto

        print('Produto(s) removidos do estoque com sucesso!')

    def produtos_com_baixo_estoque(self):
        # TODO acessa o csv vendo todos os produto que produto.quantidade_atual < produto.quantidade_minima
        pass
