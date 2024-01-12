import random
import os
import msvcrt
import time

matrica = [[" " for a in range(10)] for b in range(10)]
zmija = [[2, 1], [2, 2], [2, 3]]
GAMEOVER = False
BRZINA_IGRE = 0.3
VELICINA_MATRICA = len(matrica)
print("Press any button to start.")
msvcrt.getch()
default_smer = 77
bonus_lokacija = [random.randrange(1, VELICINA_MATRICA - 2), random.randrange(1, VELICINA_MATRICA - 2)]
SCORE = 0


def bonus():
    brojac = 0
    global bonus_lokacija, SCORE, BRZINA_IGRE, GAMEOVER
    if bonus_lokacija in zmija:
        SCORE += 1
        zmija.insert(0, bonus_lokacija)
        matrica[bonus_lokacija[0]][bonus_lokacija[1]] = "@"

        if SCORE % 5 == 0:
            brojac = SCORE
        helperlista = []

        for i in range(1, len(matrica) - 1):
            for j in range(1, len(matrica) - 1):
                if [i, j] not in zmija:
                    helperlista.append([i, j])

        if len(helperlista) == 0:
            print("\nYou won!\n")
            GAMEOVER = True
        else:
            bonus_lokacija = random.choice(helperlista)


        if SCORE % 2 == 0:
            if BRZINA_IGRE > 0.1:
                BRZINA_IGRE -= 0.1
                brojac += 1
            else:
                BRZINA_IGRE = 0.1


def crtaj():

    os.system('cls')
    matrica[bonus_lokacija[0]][bonus_lokacija[1]] = "x"

    for element in zmija:
        matrica[element[0]][element[1]] = "@"

    for i in range(VELICINA_MATRICA):
        matrica[i][0] = "*"
        matrica[i][VELICINA_MATRICA - 1] = "*"
        matrica[0][i] = "*"
        matrica[VELICINA_MATRICA - 1][i] = "*"

    for elem in zmija:
        if elem[0] == 0 or elem[0] == VELICINA_MATRICA - 1 or elem[1] == 0 or elem[1] == VELICINA_MATRICA - 1 \
                or zmija[-1] in zmija[0:-1]:
            global GAMEOVER

            input("You suck")
            GAMEOVER = True
            print("\nYou lost!\n")
            break

    for red in matrica:
        for elem in red:
            print(elem, end=" ")
        print()
    print()

    for i in range(1, VELICINA_MATRICA - 1):
        for j in range(1, VELICINA_MATRICA - 1):
            matrica[i][j] = " "

    print("Score: " + str(SCORE))
    print("Game speed: %.1f" % BRZINA_IGRE)


def unos():
    global default_smer, zmija, BRZINA_IGRE

    while True:
        if msvcrt.kbhit():

            unos = ord(msvcrt.getch())

            if unos == 27:
                print("Game paused.")
                while True:
                    resume = ord(msvcrt.getch())
                    if resume == 27:
                        print("Game resuming...")
                        time.sleep(1)
                        if msvcrt.kbhit():
                            unos = ord(msvcrt.getch())
                            if unos == 224:
                                default_smer = 224
                                break
                        break
                break

            if unos == 224:
                default_smer = 224
                break
        break

    if default_smer == 224:
        default_smer = ord(msvcrt.getch())

    if default_smer == 77:  # desno

        glava = zmija[-1]
        glava = [glava[0], glava[1] + 1]
        for i in range(len(zmija) - 1):
            zmija[i] = zmija[i + 1]
        zmija[len(zmija) - 1] = glava

    if default_smer == 75:  # levo

        glava = zmija[-1]
        glava = [glava[0], glava[1] - 1]
        for i in range(len(zmija) - 1):
            zmija[i] = zmija[i + 1]
        zmija[len(zmija) - 1] = glava

    if default_smer == 72:  # gore

        glava = zmija[-1]
        glava = [glava[0] - 1, glava[1]]
        for i in range(len(zmija) - 1):
            zmija[i] = zmija[i + 1]
        zmija[len(zmija) - 1] = glava

    if default_smer == 80:  # dole

        glava = zmija[-1]
        glava = [glava[0] + 1, glava[1]]
        for i in range(len(zmija) - 1):
            zmija[i] = zmija[i + 1]
        zmija[len(zmija) - 1] = glava


########################################################################################################################

while GAMEOVER == False:
    time.sleep(BRZINA_IGRE)
    unos()
    crtaj()
    bonus()



