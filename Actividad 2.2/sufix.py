#Sergio Santiago Sánchez Salazar A01645255
#Emiliano Nuñez Felix A01645413

def OrderedSuffixes(string):
    n = len(string)
    suffixes = []
    for i in range(n):
        suffixes.append(string[i::])

    suffixes = sorted(suffixes)

    return suffixes

def main():
    string = input("Ingresa palabra: ")
    suffixes = OrderedSuffixes(string)
    print("sufijos ordenados")
    print(suffixes)


main()