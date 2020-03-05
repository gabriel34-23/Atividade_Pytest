def album(N,C,M,F_carimbadas, F_compradas):
    if(len(F_carimbadas) != C):
        return 0
    if(len(F_compradas) != M):
        return 0    
    cont = 0
    Possui = []
    for figCon in F_compradas :
        if(figCon in Possui):
            cont = cont
        else:
            Possui.append(figCon)
            if(figCon in F_carimbadas):
                cont = cont +1
        
    return C - cont
        

        
    