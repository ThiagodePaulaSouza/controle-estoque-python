from aplicacao.gestao_estoque import GestaoEstoque
from aplicacao.gestao_produto import GestaoProduto
from helpers.terminal_helper import TerminalHelper

class Main:
    def __init__(self):
        self.__gestao_produto = GestaoProduto()
        # Garante uma única instância de GestaoProduto na aplicação
        self.__estoque = GestaoEstoque( self.__gestao_produto )

        self.__executando = True
        self.__opcoes = {
            'C': ('Cadastrar Produto', self.__gestao_produto.cadastrar_produto),
            'L': ('Listar Todos Produtos', self.__gestao_produto.listar_todos_produtos),
            'P': ('Pesquisar Produto por nome', self.__gestao_produto.pesquisar_produto_nome),
            'E': ('Editar Produto', self.__gestao_produto.editar_produto), 
            'D': ('Deletar Produto (afeta estoque)', self.__gestao_produto.deletar_produto),
            'A': ('Adicionar ao Estoque', self.__estoque.adicionar_ao_estoque),
            'R': ('Retirar do Estoque', self.__estoque.retirar_do_estoque),
            'S': ('Sair', self.sair),
        }

    def executar_aplicacao(self) -> None:
        TerminalHelper.limpar_tela()

        print("Bem vindo ao Gerenciador de Estoque!\n")

        self.__estoque.produtos_com_baixo_estoque()

        while(self.__executando):
            for opt in self.__opcoes:
                print(f"{opt} - {self.__opcoes[opt][0]}") # opcoes[opt][0] é o descrição da função

            opcao = input("\nEscolha uma opção: ")
            opcao = opcao.strip().upper()

            self.executar_funcao(opcao)

    def executar_funcao(self, opcao) -> None:
        if(opcao == 'S'):
            self.sair()
            return None

        if opcao not in self.__opcoes:
            print("\nOpção inválida. Tente novamente.\n")
            continuar = input('\nDeseja Continuar? (S/N) ')
            continuar = continuar.strip().upper()
            if(continuar == 'N'):
                self.sair()
            else:
                TerminalHelper.limpar_tela()
            return None

        TerminalHelper.limpar_tela()

        print(f"Você escolheu a opção: {self.__opcoes[opcao][0]}\n") # opcoes[opcao][0] é o descrição da função
        self.__opcoes[opcao][1]() # Chama a função correspondente à opção escolhida

        continuar = input('\nDeseja Continuar? (S/N) ')
        continuar = continuar.strip().upper()

        if(continuar == 'N'):
            self.sair()
        else:
            TerminalHelper.limpar_tela()
            return None

    def sair(self):
        self.__executando = False
        print('\nPrograma finalizado.\n')
    
if __name__ == '__main__':
    Main().executar_aplicacao()