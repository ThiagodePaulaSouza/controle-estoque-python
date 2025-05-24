from helpers.validacao_helper import ValidacaoHelper

class GestaoEstoque:
    def __init__(self, gestao_produto):
        self.__gestao_produto = gestao_produto

    def adicionar_ao_estoque(self) -> None:
        self.__gestao_produto.listar_todos_produtos()

        id = input('\nEntre com o id do produto cujo estoque será aumentado: ')
        id = id.strip()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("\nDigitado valor inválido para o id")
            return None

        id = int(id)

        produto = self.__gestao_produto.listar_produto_por_id(id)
        if produto is None:
            print("\nNão foi encontrado um produto com o id digitado.")
            return None

        quantidade = input(f'Qual quantidade do produto {produto.nome} deseja adicionar ao estoque? ')
        quantidade = quantidade.strip()

        if not ValidacaoHelper.validar_string_numerica(quantidade):
            print("\nQuantidade inválida.")
            return None

        quantidade = float(quantidade)
        if(quantidade <= 0):
            print('\nQuantidade inválida. Não é possível adicionar uma quantidade menor ou igual a 0 ao estoque.')
            return None

        produto.adicionar_estoque(quantidade)
        self.__gestao_produto.salvar_lista_produtos()

        print('\nQuantidade adicionada ao estoque do produto com sucesso!')
        print(f"Nova quantidade: { produto.quantidade_atual }")

    def retirar_do_estoque(self) -> None:
        self.__gestao_produto.listar_todos_produtos()

        id = input('\nEntre com o id do produto cujo estoque será subtraído: ')
        id = id.strip()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("\nDigitado valor inválido para o id")
            return None

        id = int(id)

        produto = self.__gestao_produto.listar_produto_por_id(id)
        if produto is None:
            print("\nNão foi encontrado um produto com o id digitado.")
            return None

        quantidade = input(f'Que quantidade do Produto {produto.nome} deseja remover do estoque: ')
        quantidade = quantidade.strip()

        if not ValidacaoHelper.validar_string_numerica(quantidade):
            print("\nQuantidade inválida.")
            return None

        quantidade = float(quantidade)

        if(quantidade <= 0):
            print('\nQuantidade inválida. Não é possível extrair uma quantidade negativa ou zerada do estoque.')
            return None

        if(quantidade >= produto.quantidade_atual):
            print("\nNão é possível remover essa quantidade do estoque. Não há estoque suficiente.")
            return None

        produto.retirar_estoque(quantidade)
        self.__gestao_produto.salvar_lista_produtos()

        print('\nQuantidade subtraída com sucesso do estoque do Produto!')
        print(f'Quantidade atual: { produto.quantidade_atual }')

    def produtos_com_baixo_estoque(self) -> None:
        lista_produtos_baixo_estoque = self.__gestao_produto.listar_produtos_quantidade_abaixo_minimo()
        if len(lista_produtos_baixo_estoque) == 0:
            return None

        print("ATENÇÃO! Os seguintes produtos estão com estoque menor ou igual à quantidade mínima cadastrada: \n")
        for produto in lista_produtos_baixo_estoque:
            print(produto)

        print(" ")
