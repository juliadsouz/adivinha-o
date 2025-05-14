import random

numero = random.randint(1, 100)

tentativa = input("Você consegue acertar o número que estou pensando? Coloque um número: ")


while not tentativa.isnumeric():
    tentativa = input("Coloque um número válido: ")

tentativa = int(tentativa)

while numero != tentativa:
   if numero > tentativa:
        print(f"O número {tentativa} é menor que o número que estou pensando")
        tentativa = input("Tente novamente: ")

        if not tentativa.isnumeric():
            print("Coloque um número válido")     
    
        tentativa = int(tentativa)  

   elif numero < tentativa:
        print(f"O número {tentativa} é maior que o número que estou pensando")
        tentativa = input("Tente novamente: ")
    
        if not tentativa.isnumeric():
            print("Coloque um número válido")     
    
        tentativa = int(tentativa) 

if numero == tentativa:
    print("Você acertou!")
