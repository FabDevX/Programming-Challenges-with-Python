def is_primo(num):
    cont=0
    for i in range(1,num+1):
            if(num%i==0):
                cont=cont+1
    if cont>2:
        print(str(num)+" No es Primo")
    else:
        print(str(num)+" es primo")
            
            
def check_numbers():
    for i in range(2,100):
        is_primo(i)

check_numbers()
