import random

palavras = ["computador", "cachorro", "mulher", "brasil", "parede"]

palavra = random.choice(palavras)

print (palavra)

tentativas = 0

chances = 4

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)

print ("Bem vindo ao jogo da forca")
print ("Seu objetivo é tentar acertar a palavra secreta")
print ("Você terá que tentar uma letra por vez")
print ("Caso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar")
print ("Caso você erre, você percerá uma chance, você tem no máximo", chances, "tentativas")

while tentativas < chances and ''.join(estado_atual) != palavra:

	letra = input("\n\nQual letra você quer tentar? ")

	while letra in letras_escolhidas:
		print ("Você escolheu uma letra que já tinha tentado, escolha outra")
		letra = input("\nQual letra você quer tentar? ")

	letras_escolhidas.append(letra)

	if letra in palavra:
		print ("Parabéns, você acertou a letra!")
		for i in range(len(palavra)):
			if letra == palavra[i]:
				estado_atual[i] = letra
	else:
		print ("Que pena, você errou!")
		tentativas = tentativas + 1

	# quantas tentativas ele tem
	print ("Você já fez", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas" )

	# qual o estado atual da palavra
	print ("Esse é o estado atual:")
	print (estado_atual)

	# quais as letras ele já tentou
	print ("As letras que você já tentou são:")
	for item in letras_escolhidas:
		print (item, end=" ")

# fazer um final pro jogo
if tentativas == chances:
	print ("\n\nVocê perdeu")
	print ("Acabaram suas tentativas")
else:
	print ("\n\nVocê ganhou, parabéns")

print ("A palavra era", palavra)