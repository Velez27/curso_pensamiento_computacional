def busca_pais(paises, pais):

    try:
        return paises[pais]
    except KeyError:
        return None

my_dict = {'Mexico': 1, 'Colombia': 2}

print(busca_pais(my_dict, 'Mexi'))