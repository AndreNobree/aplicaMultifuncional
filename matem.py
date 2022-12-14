from colorama import init, Fore, Back
import time, rotasvolta

def bhask():
    try:
        print(Fore.YELLOW + '\nBhaskara\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
        time.sleep(3)
        
        a = input(Fore.CYAN + '\nEntre com o valor de a: ').lower()
        if a == 'quit':
            print('retornando ao menu matemático...\n')
            time.sleep(2)
            rotasvolta.volta()
            
        b = input(Fore.CYAN + 'Entre com o valor de b: ').lower()
        if b == 'quit':
            print('retornando ao menu matemático...\n')
            time.sleep(2)
            rotasvolta.volta()
            
        c = input(Fore.CYAN + 'Entre com o valor de c: ').lower()
        if c == 'quit':
            print(Fore.LIGHTMAGENTA_EX + 'retornando ao menu matemático...\n')
            time.sleep(2)
            rotasvolta.volta()
            
        a = float(a)
        b = float(b)
        c = float(c)

        delta = (b ** 2) - 4 * a * c

        print("\n**************************\n")

        if a == 0:
            print(Fore.RED + "O valor de a, deve ser diferente de 0")
            bhask()
                    
        elif delta < 0:
            print(Fore.RED + "Sem raízes reais")
            bhask()
            
        else:
            x1 = (-b + delta ** (1 / 2)) / (2 * a)
            x2 = (-b - delta ** (1 / 2)) / (2 * a)

            print(Fore.GREEN + "RESPOSTA -> x1: {}, x2: {}".format(x1, x2))
                    
            bhask()

    except:
        print(Fore.RED + '\n\n\nENTRADA INCORRETA, REVEJA A ESCRITA\n')
        bhask()

def fibonacci():
    print(Fore.YELLOW + '\nFibonacci\nDIGITE [quit] PARA SAIR A QUALQUER MOMENTO DO PROGRAMA\n ')
    time.sleep(3)
    
    nterms = input("Quantos Termos? ").lower()

    if nterms == 'quit':
        print(Fore.LIGHTMAGENTA_EX + 'retornando ao menu matemático...\n')
        time.sleep(2)
        rotasvolta.volta()
    
    nterms = int(nterms)
    
    n1, n2 = 0, 1
    count = 0

    
    if nterms <= 0:
        print(Fore.RED + "Favor entrar com um número positivo")
        fibonacci()
        
    elif nterms == 1:
        print(Fore.GREEN + "Apenas uma sequencia",nterms,":")
        print(Fore.YELLOW + f'{n1}')
        fibonacci()
        
    else:
        print(Fore.GREEN + "Sequencia Fibonacci:")
        while count < nterms:
            print(Fore.YELLOW + f'{n1}')
            nth = n1 + n2
        
            n1 = n2
            n2 = nth
            count += 1
        time.sleep(2)
        fibonacci()
