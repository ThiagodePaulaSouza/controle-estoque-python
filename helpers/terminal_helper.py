import os
import platform

class TerminalHelper:

    @staticmethod
    def limpar_tela():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')