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
            if planszadogry['7']==planszadogry['8']==planszadogry['9']!='':
                drukujplansze(planszadogry)
                print('\nKoniecgry!\n')
                print(f'wygrał gracz: {gracz}')
                break
        elif planszadogry['4']==planszadogry['5']==planszadogry['6']!='':
                drukujplansze(planszadogry)
                print('\nKoniecgry!\n')
                print(f'wygrał gracz: {gracz}')
                break
        elif planszadogry['1']==planszadogry['2']==planszadogry['3']!='':
                drukujplansze(planszadogry)
                print('\nKoniecgry!\n')
                print(f'wygrał gracz: {gracz}')
                break
        elif planszadogry['7']==planszadogry['5']==planszadogry['3']!='':
                drukujplansze(planszadogry)
                print('\nKoniecgry!\n')
                print(f'wygrał gracz: {gracz}')
                break
        elif planszadogry['1']==planszadogry['5']==planszadogry['9']!='':
                drukujplansze(planszadogry)
                print('\nKoniecgry!\n')
                print(f'wygrał gracz: {gracz}')
                break
        if licznik==9:
            print('\nkoniec gry!!!\n')