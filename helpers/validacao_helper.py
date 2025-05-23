class ValidacaoHelper():
    def validar_string_numerica(entrada):
        if entrada == "":
          return False

        lista_caracteres = list(entrada)

        lista_caracteres_invalidos = list( filter(lambda c: not c.isdigit() and c not in ('-', '.'), lista_caracteres ) )
        if ( len(lista_caracteres_invalidos) > 0 ):
          return False

        if lista_caracteres.count("-") > 1 or lista_caracteres.count(".") > 1:
          return False

        if lista_caracteres.count("-") > 0 and lista_caracteres[0] != "-":
          return False

        return True