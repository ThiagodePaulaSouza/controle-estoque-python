from aplicacao.gestao_estoque import GestaoEstoque
from aplicacao.gestao_produto import GestaoProduto

class Main:
    def __init__(self):
        self.__estoque = GestaoEstoque()
        self.__gestao_produto = GestaoProduto()

        self.__executando = True
        self.__opcoes = {
            'L': ['Listar Todos Produtos', self.__gestao_produto.listar_todos_produtos],
            'P': ['Pesquisar Produto por nome', self.__gestao_produto.pesquisar_produto_nome],
            'C': ['Cadastra Produto', self.__gestao_produto.cadastrar_produto],
            'E': ['Editar Produto', self.__gestao_produto.editar_produto],
            'D': ['Deletar Produto (afeta estoque)', self.__gestao_produto.deletar_produto],
            'A': ['Adicionar ao Estoque', self.__estoque.adicionar_ao_estoque],
            'R': ['Retirar do Estoque', self.__estoque.retirar_do_estoque],
            'S': ['Sair', self.sair],
        }

    def executar(self):
        print("\nBem vindo ao Gerenciador de Estoque!\n")
        self.__estoque.produtos_com_baixo_estoque()

        while(self.__executando):

            for opt in self.__opcoes:
                print(f"{opt} - {self.__opcoes[opt][0]}")

            opcao = input("\nEscolha uma opção: ")
            opcao = opcao.strip().upper()

            self.executar_funcao(opcao)

    def executar_funcao(self, opcao):
        if(opcao == 'S'):
            self.sair()
            return

        self.__opcoes[opcao][1]()
        continuar = input('\nDeseja Continuar? (S/N) ')
        continuar = continuar.strip().upper()

        if(continuar == 'N'):
            self.sair()
        else:
            return

    def sair(self):
        self.__executando = False
        print('\nPrograma finalizado.\n')
    
if __name__ == '__main__':
    Main().executar()