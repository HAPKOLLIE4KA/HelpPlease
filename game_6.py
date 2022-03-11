import random

def printQuiry():
    print("Подкидывается монетка")
    print("Выберите, что выпадет: 0 - Орёл или 1 - Решка")

def quitGame():
    print("Конец игры")
    quit()

def printNumberRound(stateGame):
    print(f"\n\n-------Раунд {stateGame['countRound']}-------")

def printScore(stateGame):
    print(f"      Счёт игры {stateGame['userWinner']}:{stateGame['userDefeat']}")
    print(f"Баланс на данный момент {stateGame['userMoney']}")

def printWinner(coinFlipping):
    stringFlipping = "решка" if coinFlipping else "орёл"
    print(f"Иу, вы угадали, действительно {stringFlipping}")

def printDefeat(coinFlipping):
    stringFlipping = "решка" if coinFlipping else "орёл"
    print(f"Упс, вы не угадали, на самом деле {stringFlipping}")

def inputResponse(): #обработка ввода
    while True:
        try:
            return int(input())
        except ValueError:
            print("Введите одно целое число")

def resultGame(response, stateGame):     #определяет результат игры
    coinFlipping = random.randint(0,1)

    if response == coinFlipping:
        printWinner(coinFlipping)
        stateGame["userWinner"] += 1
        stateGame["userMoney"] += 1
    else:
        printDefeat(coinFlipping)
        stateGame["userDefeat"] += 1
        stateGame["userMoney"] -= 1

    stateGame['countRound'] += 1

    return stateGame

def main():

    stateGame = {          #хранит состояние игры
        "countRound": 1,
        "userWinner": 0,
        "userDefeat": 0,
        "userMoney": 3
    }

    while True:

        printNumberRound(stateGame)

        printQuiry()
        response = inputResponse()

        if response not in [0,1]: quitGame()

        stateGame = resultGame(response, stateGame)

        printScore(stateGame)

        if stateGame["userMoney"] == 0: quitGame()

if __name__ == "__main__":
    main()