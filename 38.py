import os

def grava(n, me, ma, cont):
    file_path = '' 
    tipo = ''
    enc = '' 

    dir = '/tmp/exercicios'
    arq = '/38.txt'

    file_path = dir + arq

    if not os.path.exists(dir) or not os.path.isdir(dir):
        os.makedirs(dir)
        
    os.chmod(dir, 0o744)

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        enc = 'utf-8'

        if os.path.exists(file_path) and cont != 1:
            tipo = 'a'

        with open(file_path, tipo, encoding=enc) as file:
            file.write(f'{n}\n')

            if cont == 100:
                file.write(f'Maior: {ma}\n')
                file.write(f'Menor: {me}\n')


def getNum():
    num:int = 0
    maior = None
    menor = None

    for i in range(1, 101):
        num = int(input("Digite um número: "))
        
        if maior is None or num > maior:
            maior = num
        
        if menor is None or num < menor:
            menor = num
        
        grava(num, menor, maior, i)


def main():
    getNum()

if __name__ == '__main__':
    main()