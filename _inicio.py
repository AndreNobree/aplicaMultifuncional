from colorama import init, Fore, Back
import time, rotasvolta

def menu():

    print(Back.BLUE + Fore.WHITE + '*-*-*  MENU  *-*-*\n')
    print(Back.RESET + Fore.YELLOW + '[1] - Questões Matemáticas\n')
    print(Back.RESET + Fore.YELLOW + '[99] - Sair\n')
    
    try:
        entrada = int(input(Fore.CYAN + 'Digite qual opção você deseja: '))
        if entrada == 1:
            print(Fore.GREEN + 'Abrindo Menu Matemático...\n')
            time.sleep(2)
            rotasvolta.volta()
        
        elif entrada == 99:
            print(Fore.GREEN + 'Terminando...\n')
            time.sleep(2)
        
        else:
            print(Fore.RED + '\n\n\nOPÇÃO INCORRETA\n')
            menu()
    except:
        print(Fore.RED + '\n\n\nENTRADA INCORRETA, REVEJA A ESCRITA\n')
        menu()
