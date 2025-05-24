from models.produto import Produto
from configurations.configurations import Configurations
import csv 
import os

class ArquivoHelper():
    def __init__(self):
        self.__configurations = Configurations()

    def ler_arquivo(self) -> list:
        if os.path.exists(self.__configurations.arquivo_saida):
            with open(self.__configurations.arquivo_saida, 'r', encoding='UTF-8') as arquivo:
                arquivo_csv = csv.DictReader(arquivo)

                lista_produtos = []

                for linha in arquivo_csv:
                    lista_produtos.append(
                        Produto.construir_produto_pela_linha(linha)
                    )

                return lista_produtos
        else:
            return []

    def escrever_arquivo(self, lista_produtos) -> None:
        with open(self.__configurations.arquivo_saida, 'w+', encoding='UTF-8') as arquivo:
            linhas_saida = [
                ['id', 'nome', 'fornecedor', 'quantidade_minima', 'quantidade_atual']
            ]

            for produto in lista_produtos:
                linhas_saida.append(produto.gerar_lista_campos_arquivo())

            escritor = csv.writer(arquivo)
            escritor.writerows(linhas_saida)