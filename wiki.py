from colorama import init, Fore, Back
import time, _inicio, wikipedia

def pesquisa():
    
    print(Fore.YELLOW + '\nWikipédia\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
    
    entr = str(input(Fore.CYAN + 'Digite a sua pesquisa: \n\n->'))
    wikipedia.set_lang('pt')
    
    try:
        if entr == 'quit':
            print(Fore.GREEN + 'Terminando...\n')
            time.sleep(2)
            _inicio.menu()
            
        else:
            resultado = wikipedia.summary(entr, 2) 
            print(Fore.GREEN + 'Pesquisando...')
            time.sleep(3)
            print(Fore.YELLOW + f'{resultado}')   
            pesquisa()
    except:
        time.sleep(2)
        print(Fore.RED + 'ERRO, Especifique sua pesquisa')
        time.sleep(1)
        pesquisa()