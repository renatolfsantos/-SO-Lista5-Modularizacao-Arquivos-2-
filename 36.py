import os

num:int = 0
soma:float = 1.0
counter:int = 0

def grava(d, s):
    global num, counter

    file_path = '' 
    enc = 'utf-8' 
    tipo = 'r'

    dir = '/tmp/exercicios/'
    arq = '36.txt'
    
    file_path = dir + arq
    
    if not os.path.exists(dir) or not os.path.isdir(dir):
        os.makedirs(dir)
        
    os.chmod(dir, 0o744)

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        enc = 'utf-8'

        if os.path.exists(file_path) and counter != 1:
            tipo = 'a'

        with open(file_path, tipo, encoding=enc) as file:
            file.write(f'1/{counter}! = {d}\n')
            if counter == num:
                file.write(f'O resultado final é: {s}')


def calcSoma(div):
    global soma

    soma += div

    grava(div, soma)

def calcDiv(f):
    return 1/f

def calcFat(n):
    fat:int = 1

    for i in range(2, n + 1):
        fat *= i

    return fat


def main():
    global num, counter
    
    num = int(input("Digite o número para o cálculo da série 1 + 1/1! + 1/2! + ... + 1/N!: "))
    termo:float = 1.0

    for i in range(1, num + 1):
        termo = calcDiv(calcFat(i))
        
        counter += 1
        calcSoma(termo)

if __name__ == '__main__':
    main()