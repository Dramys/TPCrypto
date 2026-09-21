if __name__ == "main":

    print("Ah oui on est dans le programme")

    def chiffrement_vigenere(texteClair : str, clef : str) -> str :

        longueurTexteClair = len(texteClair)
        longueurClef = len(clef)
        texteChiffré : str
        texteChiffré = ""

        while longueurClef < longueurTexteClair :
            if longueurTexteClair - longueurClef >= longueurClef :
                clef += clef
                longueurClef = len(clef)
            else :
                lettresManquantes = longueurTexteClair - longueurClef
                for i in range(lettresManquantes) :
                    clef.append(i)

        return texteChiffré

    print(chiffrement_vigenere("bonjour", "clef"));