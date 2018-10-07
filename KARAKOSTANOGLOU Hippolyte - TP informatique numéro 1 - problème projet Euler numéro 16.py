def solve(n):
    m=2**n
    k=0
    while m>10**k:
        k+=1
    # k est la partie entière supérieure du logarithme décimal de "2 puissance n"
    s=0
    for r in range(k):       # je retire à chaque étape le dernier chiffre de "2 puissance 15" et je l'ajoute à la somme s
        s+=m%10
        m=m//10
    return s

assert solve(15) == 26

print( solve(1000) )



