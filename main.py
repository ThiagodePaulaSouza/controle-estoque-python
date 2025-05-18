from aplicacao.estoque_app import EstoqueApp
from aplicacao.produto_app import ProdutoApp

class Main:
    def __init__(self):
        self.__Estoque__ = EstoqueApp()
        self.__Produto__ = ProdutoApp()

        self.__running__ = True
        self.__opcoes__ = {
            'L': ['Listar Todos Produtos', self.__Produto__.listar_todos_produtos],
            'P': ['Pesquisar Produto por nome', self.__Produto__.pesquisar_produto],
            'C': ['Cadastra Produto', self.__Produto__.cadastrar_produto],
            'E': ['Editar Produto', self.__Produto__.editar_produto],
            'D': ['Deletar Produto (afeta estoque)', self.__Produto__.deletar_produto],
            'A': ['Adicionar ao Estoque', self.__Estoque__.adicionar_ao_estoque],
            'R': ['Remover do Estoque', self.__Estoque__.remover_do_estoque],
            'S': ['Sair', self.sair],
        }

    def run(self):
        print("\nBem vindo ao Gerenciador de Estoque!\n")

        while(self.__running__):
            self.__Estoque__.produtos_com_baixo_estoque()

            for opt in self.__opcoes__:
                print(f"{opt} - {self.__opcoes__[opt][0]}")

            opcao = input("\nEscolha uma opção: ")
            opcao.strip().upper()

            self.executar_funcao(opcao)

    def executar_funcao(self, opcao):
        if(opcao == 'S'):
            self.sair()
            return

        self.__opcoes__[opcao][1]()
        continuar = input('\nDeseja Continuar? (S/N) ')
        continuar.strip().upper()

        if(continuar == 'N'):
            self.sair()
        else:
            return

    def sair(self):
        self.__running__ = False
        print('\nPrograma finalizado.\n')
    
if __name__ == '__main__':
    Main().run()