from aplicacao.estoque import Estoque
from aplicacao.produto import Produto

class Main:
    def __init__(self):
        self.__Estoque__ = Estoque()
        self.__Produto__ = Produto()

        self.__running__ = True
        self.__opcoes__ = {
            'L': ['Listar Todos Produtos', self.__Produto__.listar_todos_produtos],
            'P': ['Pesquisar Produto por nome', self.__Produto__.pesquisar_produto],
            'C': ['Cadastra Produto', self.__Produto__.cadastrar_produto],
            'E': ['Editar Produto', self.__Produto__.editar_produto],
            'D': ['Deletar Produto (afeta estoque)', self.__Produto__.deletar_produto],
            'A': ['Adicionar ao Estoque', self.__Estoque__.adicionar_estoque],
            'R': ['Remover do Estoque', self.__Estoque__.remover_estoque],
            'S': ['Sair', self.sair],
        }

    def run(self):
        while(self.__running__):
            print("\nBem vindo ao Gerenciador de Estoque!\n")

            # TODO mostrar produtos com estoque abaixo do minimo

            for opt in self.__opcoes__:
                print(f"{opt} - {self.__opcoes__[opt][0]}")

            opcao = input("\nEscolha uma opção: ").strip().upper()

            print('\n')
            
            self.__opcoes__[opcao][1]()
            
            pass

    def sair(self):
        self.__running__ = False
    
if __name__ == '__main__':
    Main().run()