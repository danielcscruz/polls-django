import random




def lotofacil():
    
    lista = range(1,25)
    gen_loto = random.sample(lista, 15)
    
    gen_loto.sort()
    
    return gen_loto

