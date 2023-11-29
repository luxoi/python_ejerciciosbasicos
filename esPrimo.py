def numeroPrimo(num):
    for x in range(2, num):
        if(num%x==0):
            return False
    return True
print(numeroPrimo(13))
            