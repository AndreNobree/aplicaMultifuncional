from colorama import init, Fore, Back
import time, rotasvolta, os

def menu():

    print(Back.BLUE + Fore.WHITE + '*-*-*  MENU  *-*-*\n' + Back.RESET)
    print(Fore.YELLOW + '[1] - Questões Matemáticas\n')
    print(Fore.YELLOW + '[2] - Pesquisa Wikipédia\n')
    print(Back.RESET + Fore.YELLOW + '[quit] - Sair\n')
    
    try:
        entrada = input(Fore.CYAN + 'Digite qual opção você deseja: ')
        
        if entrada == 'quit':
            print(Fore.GREEN + 'Terminando...\n')
            time.sleep(2)
            os._exit(0)
        
        entrada = int(entrada)
        
        #print(type(entrada))
        if entrada == 1:
            print(Fore.GREEN + 'Abrindo Menu Matemático...\n')
            time.sleep(2)
            rotasvolta.volta()
        
        if entrada == 2:
            print(Fore.GREEN + 'Entrando wikipédia')
            time.sleep(2)
            rotasvolta.volta2()
        
        
        else:
            print(Fore.RED + '\n\n\nOPÇÃO INCORRETA\n')
            menu()
    except:
        print(Fore.RED + '\n\n\nENTRADA INCORRETA, REVEJA A ESCRITA\n')
        menu()
