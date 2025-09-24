#Importar random para aleatoriedades
#Laço para que o código rode indefinidamente
#Input para o usuario escolher se ele quer jogar ou não
#Se o usuario escolher SIM, um número aleatorio entre 1 a 6 será gerado (duas vezes)
#Imprimir o valor gerado
#Se o usuario escolher NÃO, imprimir uma mensagem de despedidade e encerrar o laço
#Entretanto, se nem SIM e NÃO forem digitados, imprimir uma mensagem de confusão

import random

while True:
    escolha = input('Jogar os dados? (S/N): ').lower()
    
    if escolha == 's':
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        print(f'{dado1} {dado2}')
        
    elif escolha == 'n':
        print("Obrigado por jogar!")
        break
    
    else:
        print("Mensagem inválida, tente novamente")