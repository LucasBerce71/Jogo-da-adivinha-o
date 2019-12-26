#iniccio do game
import random

guessesTaken = 0

print('Olá! Qual é o seu nome?')
myName = input()

number = random.randint(1, 20)
print('Bem ' + myName + ', eu estou pensando em um número entre 1 e 20.')

while guessesTaken < 6:
    print('Consegue advinhar em qual número estou pensando?')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Seu palpite está muito abaixo das minhas espectativas!')

    if guess > number:
        print('Seu palpite está muito acima das minhas expectativas')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Muito Bom ' + myName + '! Você conseguiu advinhar o número em que estou pensando em ' + guessesTaken + ' tentativas!')

if guess != number:
    number = str(number)
    print('Game Over! O número em que eu estou pensando é o número ' + number)
