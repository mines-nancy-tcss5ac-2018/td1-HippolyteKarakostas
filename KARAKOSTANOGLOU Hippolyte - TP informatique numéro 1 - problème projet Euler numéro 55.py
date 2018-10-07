#Commentaire général: j'ai étrangement été contraint de créer une grosse fonction solve(), au lieu de séparer la fonction en plusieurs fonctions auxiliaires (notamment une fonction reverse qui permettait de permuter les chiffres d'un nombre) pour ne pas obtenir d'érreur d'indice de range...



def palindrome(m):                     # Cette fonction détermine si un nombre m est un palindrome ou non. On commence par créer une chaine de caractères M représentant l'entier puis une autre chaine t représentant le nombre m dont l'ordre des chiffres a été inversé (instruction réalisée par la première boucle for).
    M=str(m)
    t=''
    for x in M:
        t=str(x)+t
    for i in range(len(M)):             #Pour chaque lettre d'indice i, on cherche à savoir si elle est égale à celle de l'autre chaine. Dès lors qu'une inégalité a lieu, le programme s'interromp, le nombre n'étant assurément pas un palindrome.
        if M[i] != t[i]:
            return False
    return True
    
    
    
def solve():
    N=0
    for n in range(10000):               #Pour chaque nombre entre 0 et 9999, je teste s'il peut engendrer un palindrome en strictement moins de 50 intérations. N comptabilise le nombre de palindromes rencontrés entre 0 et 9999.
        m=n
        for k in range(49):         #Cette partie de la fonction sert à créer l'entier m + reverse(m), où reverse(m) est l'entier formé des chiffres de m dans le sens contraire.
            M=str(m)
            t=''
            for x in M:
                t=str(x)+t
            m=m+int(t)
            
            
            if palindrome(m):
                N+=1
                break                      # Si pour une certaine itération, un palindrome a été engendré, inutile de poursuivre jusqu'à la 49è itération.
                
    return 10000-N                         # On a compté le nombre N de nombres inférieurs à 10000 donnant naissance à un palindrome en moins de 50 itérations de l'algorithme.   Les nombres de Lychrel sont les nombres restants; on renvoie donc 10000-N.  
assert palindrome(1221) == True

print(solve())
        
    
