from models.produto import Produto
from configurations.configurations import Configurations
from datetime import date
from csv import csv

class ArquivoHelper():
    def __init__(self):
        self.__configurations = Configurations()

    def ler_arquivo(self):
        with open(self.__configurations.arquivo_saida, 'r', encoding='UTF-8') as arquivo:

            arquivo_csv = csv.DictReader(arquivo)

            next(arquivo)

            lista_produtos = []

            for linha in arquivo_csv:
                lista_produtos.append(
                    Produto(linha)
                )

            return lista_produtos

    def escrever_arquivo(self, lista_produtos):
        with open(self.__configurations.arquivo_saida, 'w+', encoding='UTF-8') as arquivo:

            linhas_saida = [
                ['id', 'nome', 'fornecedor', 'quantidade_minima', 'quantidade_atual']
            ]

            for produto in lista_produtos:
                linhas_saida.append(produto.gerar_lista_campos_arquivo())

            escritor = csv.writer(arquivo)
            escritor.writerows(linhas_saida)