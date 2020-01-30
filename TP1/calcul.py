def somme(x, y):
    """Fonction de sommation"""
    return x + y

def soustraire(x, y):
    """Fonction de soustraction"""
    return x - y

def multiplier(x, y):
    """Fonction de multiplication"""
    return x * y

def diviser(x, y):
    """Fonction de division"""
    if y == 0:
        raise ValueError('Pas de division par zero!!!')
    return x / y



#print(somme(10, 15))