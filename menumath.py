from colorama import init, Fore, Back
import matem, time, _inicio

print(Fore.GREEN + '\nBem vindo ao Programa\n')

def menumath():

    print(Back.RED + Fore.WHITE + '*-*-*  MENU MATEMÁTICO  *-*-*\n')
    print(Back.RESET + Fore.YELLOW + '[1] - Bhaskara')
    print(Fore.YELLOW + '[2] - Fibonacci')
    print(Fore.YELLOW + '[99] - RETORNAR AO MENU PRINCIPAL\n')
    
    entrada = int(input(Fore.CYAN + 'Digite qual opção você deseja: '))
    
    try:
        if entrada == 1:
            print(Fore.GREEN + '\nIniciando Programa de Bhaskara...\n')
            time.sleep(2)
            matem.bhask()
        
        elif entrada == 2:
            print(Fore.GREEN + '\nIniciando Programa de Fibonacci...\n')
            time.sleep(2)
            matem.fibonacci()
            
        elif entrada == 99:
            print(Fore.GREEN + '\nRetornando ao menu principal...\n')
            time.sleep(2)
            return _inicio.menu()
            
        else:
            print(Fore.RED + '\n\nOPÇÃO INCORRETA\n')
            menumath()
    except:
        print(Fore.RED + '\nENTRADA INCORRETA\n')
        print(Fore.RED + 'REVEJA A ESCRITA\n')
