
#NUMEROS PRIMOS 


def is_primo(value):
    if value <= 1:
        return False 
    elif value <= 3:
        return True
    elif value % 2 == 0 or value % 3 == 0:
        return False

    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            print("no es")
            
            return False  

    return True  

    