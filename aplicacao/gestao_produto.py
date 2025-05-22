from models.produto import Produto

class GestaoProduto:
    def __init__(self):
        pass

    def listar_todos_produtos(self):
        # TODO acessa o csv e lista todos produtos
        print('listar_todos_produtos')

    def pesquisar_produto(self):
        # TODO acessa o csv e acha o produto pelo nome
        produto_achado = []
        if len(produto_achado) == 0:
            print('Nenhum produto foi encontrado...')
            return

    def seleciona_produto_por_id(self) -> Produto:
        # TODO acessa o csv e produrar por id
        print('get_produto_por_id')
        return Produto(0, 'teste', 10)

    def cadastrar_produto(self, nome, quantidade_minima):
        # TODO acessa o csv e pega maior id
        maior_id = 1
        produto = Produto(maior_id + 1, nome, quantidade_minima, 0)

        # TODO acessa o csv e adiciona o produto
        print('cadastrar_produto')

    def editar_produto(self, id, nome, quantidade_minima, quantidade_atual):
        produto = self.seleciona_produto_por_id(id)
        if produto is None:
            print('Nenhum produto foi encontrado...')
            return
        
        produto.atualizar_produto(nome, quantidade_minima, quantidade_atual)

        # TODO acessa o csv e modifica
        print('editar_produto')

    def deletar_produto(self):
        print('deletar_produto')