    def join(*args):
        resultat = ""
        
        separateur = args[0]
        elements = args[1:]
        
        for element in elements:
            resultat += element + separateur
     
        return resultat[:-1]
     
    j = join(":", "Bonjour", "tout", "le", "monde")
    print(j)
