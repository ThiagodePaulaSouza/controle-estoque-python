from models.produto import Produto
from helpers.arquivo_helper import ArquivoHelper
from helpers.validacao_helper import ValidacaoHelper

class GestaoProduto:
    def __init__(self):
        self.__arquivo_helper = ArquivoHelper()
        self.__lista_produtos = self.__arquivo_helper.ler_arquivo()

    def salvar_lista_produtos(self) -> None:
        self.__arquivo_helper.escrever_arquivo(self.__lista_produtos)
        return None

    def listar_produtos_quantidade_abaixo_minimo(self) -> list:
        return list(filter(lambda p: p.quantidade_atual <= p.quantidade_minima, self.__lista_produtos))

    def listar_todos_produtos(self) -> None:
        if len(self.__lista_produtos) == 0:
            print("\nNenhum produto cadastrado!")
            return None
        
        print('Lista de produtos cadastrados:')

        for produto in self.__lista_produtos:
            print(produto)

    def pesquisar_produto_nome(self) -> None:
        nome = input("Entre com o nome do produto que você deseja visualizar. ")
        produto = self.listar_produto_por_nome(nome)

        print(f"\n{produto}") if produto is not None else print("\nNenhum produto foi encontrado...")

    def listar_produto_por_nome(self, nome) -> Produto | None:
        produto_encontrado = list(filter(lambda p: p.nome.strip().upper() == nome.strip().upper(), self.__lista_produtos))
        return produto_encontrado[0] if len(produto_encontrado) > 0 else None

    def pesquisar_produto_por_id(self) -> None:
        id = input("Entre com o id do produto que você deseja visualizar. ")
        id = id.strip()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("\nValor digitado é inválido para o id")
            return 

        id = int(id)
        produto = self.listar_produto_por_id(id)
        
        print(f"\n{produto}") if produto is not None else print("\nNenhum produto foi encontrado...")

    def listar_produto_por_id(self, id) -> Produto:
        produto_encontrado = list(filter(lambda p: p.id == int(id), self.__lista_produtos))
        return produto_encontrado[0] if len(produto_encontrado) > 0 else None

    def cadastrar_produto(self) -> None:
        nome = input("Entre com o nome do produto. ")

        produto = self.listar_produto_por_nome(nome)
        if produto is not None:
            print("\nJá existe um produto cadastrado com o nome digitado")
            return None

        fornecedor = input("Entre com o nome do fornecedor. ")
        fornecedor = fornecedor.strip()

        quantidade_minima = input("Entre com a quantidade mínima para o produto. ")
        quantidade_minima = quantidade_minima.strip()

        if not ValidacaoHelper.validar_string_numerica(quantidade_minima):
            print("\nDigitado valor inválido para a quantidade mínima")
            return None

        quantidade_minima = float(quantidade_minima)

        if quantidade_minima <= 0:
            print("\nQuantidade mínima inválida. Não é possível cadastrar um produto com quantidade mínima menor ou igual a 0.")
            return None

        ids = list(map(lambda p: p.id, self.__lista_produtos))

        maior_id = max(ids) if len(ids) > 0 else 0

        produto = Produto(maior_id + 1, nome, fornecedor, quantidade_minima)

        self.__lista_produtos.append(produto)
        self.salvar_lista_produtos()

        print(f"\nProduto cadastrado com sucesso!\n{produto}")

    def editar_produto(self) -> None:
        id = input("Entre com o id do produto que você deseja editar. ")
        id = id.strip()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("\nDigitado valor inválido para o id")
            return None

        id = int(id)

        produto = self.listar_produto_por_id(id)
        if produto is None:
            print('\nNenhum produto foi encontrado...')
            return None

        print(f"Produto encontrado. Dados atuais: {produto}")

        nome = input("Entre com o novo nome do produto. ")
        nome = nome.strip()

        fornecedor = input("Entre com o nome do novo fornecedor. ")
        fornecedor = fornecedor.strip()

        quantidade_minima = input("Entre com a nova quantidade mínima para o produto. ")
        quantidade_minima = quantidade_minima.strip()

        if not ValidacaoHelper.validar_string_numerica(quantidade_minima):
            print("\nDigitado valor inválido para a quantidade mínima")
            return None

        quantidade_minima = float(quantidade_minima)

        if quantidade_minima <= 0:
            print("\nQuantidade mínima inválida. Não é possível cadastrar um produto com quantidade mínima menor ou igual a 0.")
            return None
        
        produto.atualizar(nome, fornecedor, quantidade_minima)
        self.salvar_lista_produtos()

        print(f"\nProduto editado com sucesso!\n{produto}")

    def deletar_produto(self) -> None:
        id = input("Entre com o id do produto que você deseja excluir. ")
        id = id.strip()

        if not ValidacaoHelper.validar_string_numerica(id):
            print("\nDigitado valor inválido para o id")
            return None

        id = int(id)

        produto = self.listar_produto_por_id(id)
        if produto is None:
            print('\nNenhum produto foi encontrado...')
            return None

        self.__lista_produtos = list(filter(lambda p: p.id != int(id), self.__lista_produtos))
        self.salvar_lista_produtos()

        print("\nProduto excluído com sucesso!")
