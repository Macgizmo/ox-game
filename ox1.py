planszadogry = {
    "7": "", "8": "", "9": "",
    "4": "", "5": "", "6": "",
    "1": "", "2": "", "3": "",}
klawiszegry= []
for key in planszadogry:
    klawiszegry.append(key)

def drukujplansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print("-+-+-")
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print("-+-+-")
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")
    print("-+-+-")

def gra():
    gracz='x'
    licznik=0
    for i in range(1,10):
        drukujplansze(planszadogry)
        move=input(f'To jest ruch, {gracz}. Wybierz gdzie chcesz wstawić znak')
        if planszadogry[move] =='':
            planszadogry[move] = gracz
            licznik += 1
        else:
            print('Miejsce jest już zajęte\nWstaw swój znakgdzieś indziej')
            continue
        if licznik >= 5: