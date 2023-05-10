import prob

def main():
    option = 1
    while option != 0:
        
        print('===================')
        print('Escolha uma opcao:')
        option = int(input('0-Sair\n1: DISC_Distr_Binomial\n2: DISC_Distr_Geometrica\n3: DISC_Esperanca_Hipergeometrica\n4: DISC_Esperanca_Binomial\n5: DISC_Esperanca_Geometrica\n6: DISC_Esperanca_Hipergeometrica\n7: Variancia_Hipergeometrica\n8: Poisson\n>>> '))

        if option == 1:
            max = int(input('Valor maximo: '))
            n = int(input('n: '))
            p = float(input('p: '))
            
            for i in range(0, max):
                print(f"RESPOSTA [{i}] = {prob.DISC_Distr_Binomial(n, p, i)}")
                
        elif option == 2:
            max = int(input('Valor maximo: '))
            p = float(input('p: '))
            
            for i in range(0, max):
                print(f"RESPOSTA [{i}] = {prob.DISC_Distr_Geometrica(p, i)}")
                
        elif option == 3:
            max = int(input('Valor maximo: '))
            r = int(input('r: '))
            N = int(input('N: '))
            k = int(input('k: '))
            
            for i in range(0, max):
                print(f"RESPOSTA [{i}] = {prob.DISC_Distr_Hipergeometrica(N, r, i, k)}")
                
        elif option == 4:
            n = int(input('n: '))
            p = float(input('p: '))
            print(f"RESPOSTA = {prob.DISC_Esperanca_Binomial(n, p)}")
            
        elif option == 5:
            p = float(input('p: '))
            print(f"RESPOSTA = {prob.DISC_Esperanca_Geometrica(p)}")
            
        elif option == 6:
            evento = int(input('evento: '))
            r = int(input('r: '))
            N = int(input('N: '))
            print(f"RESPOSTA = {prob.DISC_Esperanca_Hipergeometrica(evento, r, N)}")
            
        elif option == 7:
            evento = int(input('evento: '))
            r = int(input('r: '))
            N = int(input('N: '))
            print(f"RESPOSTA = {prob.DISC_Variancia_Hipergeometrica(evento, r, N)}")
        
        elif option == 8:
            max = int(input('Valor max: '))
            tetha = float(input('tetha: '))
            
            for i in range(0, max):
                print(f"RESPOSTA [{i}]= {prob.Poisson(tetha, i)}")

       
main()