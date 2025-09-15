#Sergio Santiago Sánchez Salazar A01645255
#Emiliano Nuñez Felix A01645413

def hashString(n,string):
    l = len(string)
    columnSum = [0] * n
    for i in range(0,l,n):
        row = string[i:i+n]
        if len(row) < n:
            row += str(n) * (n-len(row))
        
        for i in range(n):
            asciiValue = ord(row[i])
            columnSum[i] += asciiValue

    for i in range(len(columnSum)):
        columnSum[i] = columnSum[i] % 256

    hashSize = n//4
    result = ''
    for i in range(hashSize):
        result += f"{columnSum[i]:02X}"

    return result

def main():
    print(hashString(8,"HOLA\n"))

main()