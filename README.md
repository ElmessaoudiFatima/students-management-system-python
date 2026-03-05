# 🎓 Student Management System

A Python console application to manage students, grades, and statistics — available in **French** and **English**.

---

## 📁 Project Structure

```
📦 student-management/
├── gestion_des_etudiants.py   # 🇫🇷 French version
├── students_managementen.py  # 🇬🇧 English version
└── README.md
```

---

## ✨ Features

- ➕ Add a student (with optional email & city)
- 📝 Add grades to a student
- 📋 Display all students and their info
- 🔍 Search for a student by name
- 📊 Display statistics (overall, best and worst average)
- 🏆 Rank students by average
- 🗑️ Delete a student

---

## 🏗️ Class Structure

```
Personne
└── Etudiant
    └── EtudiantGI
```

| Class | Description |
|-------|-------------|
| `Personne` | Base class — name and age |
| `Etudiant` | Inherits Personne — adds field, level, grades |
| `EtudiantGI` | Inherits Etudiant — adds specialization option |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed → [python.org](https://www.python.org/downloads/)

### Run the French version
```bash
py gestion_des_etudiants.py
```

### Run the English version
```bash
py students_management.py
```

> **Note for Windows users:** Use `py` instead of `python` if the `python` command is not recognized.

---

## 🖥️ Usage Example

```
----------- MENU -----------
1. Add a student
2. Add grades
3. Display all students
4. Search for a student
5. Display statistics
6. Rank students by average
7. Delete a student
8. Quit
-----------------------------
Your choice :
```

---

## 👤 Author

ELMESSAOUDI Fatima 
