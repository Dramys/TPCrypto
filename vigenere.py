if __name__ == "__main__":
    
    print("Ah oui on est dans le programme")
    
    def vigenere(texteClair : str, clef : str) -> str :
        longueurClef : int
        longueurTexteClair : int
        texteChiffré : str
        
        longueurTexteClair = len(texteClair)
        longueurClef = len(clef)
        texteChiffré = ""
        
        print(longueurTexteClair)
        print(longueurClef)
        
        # Définir la taille de la clé pour la longueur du mot
        
        while longueurClef < longueurTexteClair :
            if longueurTexteClair - longueurClef >= longueurClef :
                clef += clef
                longueurClef = len(clef)
            
            else :
                lettresManquantes = longueurTexteClair - longueurClef
                for i in range(lettresManquantes) :
                    clef.append(clef[i])
        return texteChiffré
    
    vigenere("bonjour", "clef")