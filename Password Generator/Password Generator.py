import hashlib
import json
import random
import string

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password

def generate_random_password():
    length = random.randint(10, 15)
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=2)

def add_password():
    username = input("Entrez le nom d'utilisateur : ")

    while True:
        generated_password = generate_random_password()
        print(f"Mot de passe généré : {generated_password}")
        choice = input("Voulez-vous utiliser ce mot de passe ? (Oui/Non) : ").lower()
        if choice == "oui":
            break

    hashed_password = hash_password(generated_password)
    
    passwords = load_passwords()

    while username in passwords:
        print("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        username = input("Entrez le nom d'utilisateur : ")

    passwords[username] = hashed_password
    
    save_passwords(passwords)
    print("Mot de passe ajouté avec succès.")

def display_passwords():
    passwords = load_passwords()
    if passwords:
        print("Liste des mots de passe enregistrés :")
        for username, hashed_password in passwords.items():
            print(f"Utilisateur : {username}, Mot de passe (hashé) : {hashed_password}")
    else:
        print("Aucun mot de passe enregistré.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        
        choice = input("Choisissez une option (1/2/3) : ")

        if choice == "1":
            add_password()
        elif choice == "2":
            display_passwords()
        elif choice == "3":
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")