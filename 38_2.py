import os

def lerLinhas():
    counter:int = 0
    file_path = '' 
    enc = 'utf-8' 
    tipo = 'r'

    dir = '/tmp/exercicios/'
    arq = '38.txt'
    
    file_path = dir + arq
    
    with open(file_path, tipo, encoding=enc) as file:
        for linha in file:
            counter += 1
            verificaMult(linha, counter)
        

def verificaMult(line, counter):
    line = line.strip()

    file_path = '' 
    tipo = ''
    enc = '' 

    dir = '/tmp/exercicios/'
    arq = '38_2.txt'

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
            if "Maior" not in line and "Menor" not in line:
                if int(line) % 5 == 0:
                    file.write(f'{line}\n')   


def main():
    lerLinhas()

if __name__ == '__main__':
    main()