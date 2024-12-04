def main():
    tamanho = int(input("coloque o tamanho do bloco: "))
    bloco(tamanho)

def bloco(tamanho):
    bloco = ("🧊" * tamanho)
    print (f"{bloco}\n" * tamanho, end = '')

main()