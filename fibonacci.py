'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...

'''
def Fibonacci():
    first_number=0
    secund_number=1
    sum_number=0
    for i in range(50):
        print(sum_number)
        sum_number=first_number+secund_number
        first_number=secund_number
        secund_number=sum_number
      
 
 
    
Fibonacci()
