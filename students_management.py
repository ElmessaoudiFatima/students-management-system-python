# La classe Personne 
class Personne :
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    
    def afficherInfos(self):
        print("—" * 20)  
        print(f'Name : {self.nom}')
        print(f'Age : {self.age} years old')


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
        print(f'Field : {self.filliere}')
        print(f'Level : {self.niveau}')
        if len(self.notes) > 0 :
            print("Grades :", self.notes)
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
    nom = input('Student name : ')
    age = int(input('Student age : '))
    filliere = input('Student field : ')
    if(filliere == 'GI') :
        option = input('Student option : ')
    niveau = input('Student level : ')
    email = input('Email (optional) : ')
    ville = input('City (optional) : ')
    infos = {}
    if email : 
        infos['email'] = email   
    if ville : 
        infos['ville'] = ville
    if nom in etudiants :
        print('This student already exists!')
    else :
        if(filliere == 'GI') :
            etudiant = EtudiantGI(nom = nom ,age = age ,option = option ,niveau = niveau ,**infos)
        else :
            etudiant = Etudiant(nom,age,filliere,niveau,**infos)
        etudiants[nom] = etudiant
        print('Student added successfully!')
    

# 2. Ajouter des notes
def ajouterNotes() :
    nomEtudiant = input('Please enter the student name : ')
    if nomEtudiant in etudiants :
        nbrNotes = int(input('How many grades do you want to add : '))
        notes = []
        for i in range(nbrNotes) :
            note = float(input(f'Grade {i+1} : '))
            if   (0 <= note <= 20) :
                notes.append(note)
            else :
                print('Invalid grade!')

        etudiants[nomEtudiant].ajouterNotes(*notes)
        print("Grades added successfully!")
    else :
        print('This student does not exist!')


# 3. Afficher tous les étudiants
def afficherEtudiants():
    if len(etudiants) == 0 :
        print("No students registered!")
    else:
        for etudiant in etudiants.values():
            etudiant.afficherInfos()
            print("—" * 20)  


# 4. Rechercher un étudiant
def rechercherEtudiant() :
    nomEtudiantRecherche = input('Please enter the student name : ')
    if nomEtudiantRecherche in etudiants :
        etudiants[nomEtudiantRecherche].afficherInfos()
    else :
        print('This student does not exist!')


# 5. Afficher les statistiques
def afficherStatistiques():
    if len(etudiants) == 0:
        print("No students!")
        return

    moyennes = []
    for etudiant in etudiants.values():
        moyenne = etudiant.calculerMoyenne()
        moyennes.append(moyenne)

    moyenneGenerale = sum(moyennes) / len(moyennes)
    meilleure = max(moyennes)
    pire = min(moyennes)
    
    print(f"Overall average : {moyenneGenerale:.2f}")
    print(f"Best average : {meilleure:.2f}")
    print(f"Worst average : {pire:.2f}")


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
    nomEtudiantASupprimer = input('Please enter the student name : ')
    if nomEtudiantASupprimer in etudiants :
        del etudiants[nomEtudiantASupprimer]
        print("Student deleted successfully.")
    else :  
        print('This student does not exist!')


# Menu
while True :
    print('----------- MENU ----------- ')
    print('1. Add a student')
    print('2. Add grades')
    print('3. Display all students')
    print('4. Search for a student')
    print('5. Display statistics (overall, best and worst average)')
    print('6. Rank students by average')
    print('7. Delete a student')
    print('8. Quit')
    print('----------------------------- ')
    choix = int(input('Your choice : '))
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
        print('Invalid choice!')