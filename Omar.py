def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Erreur: Division par zéro."
    return x / y

print("Sélectionnez l'opération :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Entrez le numéro de l'opération (1/2/3/4) : ")
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))

if choix == '1':
    print(f"{num1} + {num2} = {addition(num1, num2)}")
elif choix == '2':
    print(f"{num1} - {num2} = {soustraction(num1, num2)}")
elif choix == '3':
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
elif choix == '4':
    print(f"{num1} / {num2} = {division(num1, num2)}")
else:
    print("Opération invalide.")
