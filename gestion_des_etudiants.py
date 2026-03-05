# La classe Personne 
class Personne :
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    
    def afficherInfos(self):
        print("—" * 20)  
        print(f'Nom : {self.nom}')
        print(f'Age : {self.age} ans')


# La classe Etudiant
class Etudiant(Personne) :
    def __init__(self,nom,age,filliere = 'GI',niveau = 'GI2',**infos_optionnelles) :
        super().__init__(nom,age)
        self.filliere = filliere
        self.niveau = niveau
        self.notes = []
        self.infos_optionnelles = infos_optionnelles
    
    def afficherInfos(self):
        super().afficherInfos()
        print(f'Filliere : {self.filliere}')
        print(f'Niveau : {self.niveau}')
        if len(self.notes) > 0 :
            print("Les notes :", self.notes)
        if len(self.infos_optionnelles) > 0 :
            for cle,valeur in self.infos_optionnelles.items() :
                print(f'{cle} : {valeur}')
    
    def ajouterNotes(self, *notes):   
        for note in notes:
            self.notes.append(note)

    def calculerMoyenne(self) :
        if (len(self.notes) > 0) :
            return sum(self.notes) / len(self.notes)
        else :
            return 0

# La classe EtudiantGI
class EtudiantGI(Etudiant) :
    def __init__(self,nom,age,option,filliere = 'GI',niveau = 'GI2',**infos_optionnelles):
        super().__init__(nom,age,filliere,niveau,**infos_optionnelles)
        self.option = option
    
    def afficherInfos(self) :
        super().afficherInfos()
        print(f'Option : {self.option}')


# Dictionnaire pour stocker les étudiants
etudiants = {}
# 1. Ajouter un étudiant
def ajouterEtudiant() :
    nom = input('Nom de l\'étudiant : ')
    age = int(input('Age de l\'étudiant : '))
    filliere = input('La fillière de l\'étudiant : ')
    if(filliere == 'GI') :
        option = input('L\'option de l\'étudiant : ')
    niveau = input('Le niveau de l\'étudiant : ')
    email = input('Email (optionnel) : ')
    ville = input('Ville (optionnel) : ')
    infos = {}
    if email : 
        infos['email'] = email   
    if ville : 
        infos['ville'] = ville
    if nom in etudiants :
        print('Cet étudiant déjà existe !')
    else :
        if(filliere == 'GI') :
            etudiant = EtudiantGI(nom = nom ,age = age ,option = option ,niveau = niveau ,**infos)
        else :
            etudiant = Etudiant(nom,age,filliere,niveau,**infos)
        etudiants[nom] = etudiant
        print('Etudiant ajouté avec succès ! ')
    

# 2. Ajouter des notes
def ajouterNotes() :
    nomEtudiant = input('Veuillez entrer le nom de l\'étudiant : ')
    if nomEtudiant in etudiants :
        nbrNotes = int(input('Combien de notes voullez vous ajouter : '))
        notes = []
        for i in range(nbrNotes) :
            note = float(input(f'Note {i+1} : '))
            if   (0 <= note <= 20) :
                notes.append(note)
            else :
                print('La note est invalide !')

        etudiants[nomEtudiant].ajouterNotes(*notes)
        print("Notes ajoutées avec succès !")
    else :
        print('Cet étudiant est inexistant !')


# 3. Afficher tous les étudiants
def afficherEtudiants():
    if len(etudiants) == 0 :
        print("Aucun étudiant enregistré !")
    else:
        for etudiant in etudiants.values():
            etudiant.afficherInfos()
            print("—" * 20)  


# 4. Rechercher un étudiant
def rechercherEtudiant() :
    nomEtudiantRecherche = input('Veuillez entrer le nom de l\'étudiant : ')
    if nomEtudiantRecherche in etudiants :
        etudiants[nomEtudiantRecherche].afficherInfos()
    else :
        print('Cet étudiant est inexistant !')


# 5. Afficher les statistiques (moyenne générale, meilleure et pire moyenne)
def afficherStatistiques():
    if len(etudiants) == 0:
        print("Aucun étudiant !")
        return

    moyennes = []
    for etudiant in etudiants.values():
        moyenne = etudiant.calculerMoyenne()
        moyennes.append(moyenne)

    moyenneGenerale = sum(moyennes) / len(moyennes)

    meilleure = max(moyennes)
    
    pire = min(moyennes)
    
    print(f"Moyenne générale : {moyenneGenerale:.2f}")
    print(f"Meilleure moyenne : {meilleure:.2f}")
    print(f"Pire moyenne : {pire:.2f}")


# 6. Classer les étudiants par moyenne
def classerEtudiants() :
    etudiantsTries = sorted(
        etudiants.values(),              
        key=lambda etudiant: etudiant.calculerMoyenne(),  
        reverse=True                     
    )
    
    for i, etudiant in enumerate(etudiantsTries):
        print(f"{i+1}. {etudiant.nom} → {etudiant.calculerMoyenne():.2f}")
    

# 7. Supprimer un étudiant
def supprimerEtudiant() :
    nomEtudiantASupprimer = input('Veuillez entrer le nom de l\'étudiant : ')
    if nomEtudiantASupprimer in etudiants :
        del etudiants[nomEtudiantASupprimer]
        print("Etudiant supprimé avec succès.")
    else :  
        print('Cet étudiant est inexistant !')


# Menu
while True :
    print('----------- MENU ----------- ')
    print('1. Ajouter un étudiant ')
    print('2. Ajouter des notes ')
    print('3. Afficher tous les étudiants ')
    print('4. Rechercher un étudiant ')
    print('5. Afficher les statistiques (moyenne générale meilleure et pire moyenne)')
    print('6. Classer les étudiants par moyenne ')
    print('7. Supprimer un étudiant')
    print('8. Quitter ')
    print('----------------------------- ')
    choix = int(input('Votre choix : '))
    if (choix == 1) :
        ajouterEtudiant()
    elif (choix == 2) :
        ajouterNotes()
    elif (choix == 3) :
        afficherEtudiants()
    elif (choix == 4) :
        rechercherEtudiant()
    elif (choix == 5) :
        afficherStatistiques()
    elif (choix == 6) :
        classerEtudiants()
    elif (choix == 7) :
        supprimerEtudiant()
    elif (choix == 8) :
        break
    else :
        print('Votre choix est invalide !')


