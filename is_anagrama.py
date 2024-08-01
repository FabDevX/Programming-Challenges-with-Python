'''


 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.


'''
def is_anagrama(word_one,word_two):
    if (word_two.lower() == word_one.lower()):
             return False
                
    return sorted(word_two.lower()) == sorted(word_one.lower())
 
 
    
a=is_anagrama("Amor","AMOR")
print(a)
