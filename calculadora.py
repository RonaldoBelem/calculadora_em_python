while True:
    try:
        print("-----------------------------------------------")
        print("Escolha a opção")
        print("1-soma")
        print("2-subtração")
        print("3-multiplicão")
        print("4-divisão")
        print("5- sair do programa")
        print("-----------------------------------------------")
        
        opcao = int(input("digite sua opção aqui: "))
        if(opcao<=0 or opcao>=6):
            print("vc digitou uma opção invalida")
        elif(opcao==5):
            print("fim do programa ")
            break
        else:
            num1 = float(input("digite o primeiro valor: "))
            num2 = float(input("digite o segundo valor: "))
        
        print("-----------------------------------------------")

        def soma ():
            return num1+num2
        def subtracao ():
            return num1-num2
        def multiplicao ():
            return num1*num2
        def divisao ():
            return num1/num2          
        
        if(opcao==1):
            print("resultado: ",soma())
        elif(opcao==2):
            print("resultado: ",subtracao())
        elif(opcao==3):    
            print("resultado: ",multiplicao())
        elif(opcao==4):
            print("resultado: ",divisao())
        else:
            print("digite apenas numeros")
    except:
        print("vc digitou um valor invalido  ")
    