print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 17

chute = input('Digite um número: ')
#chuteString = input('Digite um número')#

print('Você digitou o número', chute)

#chute = int(chuteString)#

if numeroSecreto == chute:
    print('Você acertou!')

else:
    print('Você errou!')

