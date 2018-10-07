f = open('p022_names.txt', 'r') 
L=[] 
for ligne in f: 
    L=L+ligne.split(',') 
L=sorted(L)

def solve(L):
    alphabet=['"','A','B','C','D','E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s=0                           # s représentera la somme totale désirée lors du problème
    for i in range(len(L)):       # i représente le numéro du Nom dans la liste triée; on s'intéresse à chaque mot un par un
        t=0                       # t représentera la somme des positions dans l'alphabet de chacune des lettres du "Nom numéro i" dans la liste triée
        for x in L[i]:            # On itère ici les lettres x composant le i-ème Nom de la liste une par une
            j=0
            while alphabet[j] != x:
                j+=1              # j est finalement la position dans l'alphabet de la lettre x
            t+=j
        s+=(i+1)*t
    return s

assert solve(["AARON","MIGUEL"]) == 183

print(solve(L))