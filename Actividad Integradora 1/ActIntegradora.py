#Sergio Santiago Sánchez Salazar A01645255
#Emiliano Nuñez Felix A01645413

def buildLPS(string):
    n = len(string)
    lps = [0] * n

    length = 0
    i = 1

    while i < n:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def hasMaliciousCode(transmission, mCode): 
    lenTransmission = len(transmission)
    lenMCode = len(mCode)
    lps = buildLPS(mCode)
    positions = []

    i = 0
    j = 0

    while i < lenTransmission:
        
        if transmission[i] == mCode[j]:
            i += 1
            j += 1

            if j == lenMCode:
                positions.append(i - j)                
                j = lps[j - 1]
        
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions 

def longestPalindrome(transmission):
    n = len(transmission)

    longest = 1
    longestStart = 0
    
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and transmission[l] == transmission[r]:
            if r - l + 1 > longest:
                longest = r-l+1
                longestStart = l
            l-=1
            r+=1

        l, r = i, i+1
        while l >= 0 and r < n and transmission[l] == transmission[r]:
            if r - l + 1 > longest:
                longest = r-l+1
                longestStart = l
            l-=1
            r+=1

    longestEnd = longestStart + longest - 1 
    return longestStart, longestEnd

def longestSimilarity(transmission1,transmission2):
    t1 = len(transmission1)
    t2 = len(transmission2)
    dp = [[0 for _ in range(t2+1)] for _ in range(t1+1)]
    longest = 0
    longestEnd = -1
    for i in range(1,t1+1):
        for j in range(1,t2+1):
            if transmission1[i-1] == transmission2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    longestEnd = i -1
                    
    longestStart = longestEnd - longest + 1

    if longest > 0:
        return longestStart, longestEnd
    
    return -1,-1

def read_and_clean_file(filengthame):
    with open(filengthame, 'r') as f:
        # Lee todo el contenido y reemplaza los saltos de línea por nada
        return f.read().replace('\n', '')

def main():
    #Lectura de strings
    transmission1_str = read_and_clean_file('transmission1.txt')
    transmission2_str = read_and_clean_file('transmission2.txt')
    mcode1_str = read_and_clean_file('mcode1.txt')
    mcode2_str = read_and_clean_file('mcode2.txt')
    mcode3_str = read_and_clean_file('mcode3.txt')

    #Debugs
    '''''''''''
    print(transmission1_str)
    print(mcode1_str)
    print(buildLPS(mcode1_str))
    print(hasMaliciousCode(transmission1_str,mcode1_str))
    '''''''''''
    
    #Resultados primera parte
    mcode1_InTransmission1 = hasMaliciousCode(transmission1_str,mcode1_str)
    mcode2_InTransmission1 = hasMaliciousCode(transmission1_str,mcode2_str)
    mcode3_InTransmission1 = hasMaliciousCode(transmission1_str,mcode3_str)
    mcode1_InTransmission2 = hasMaliciousCode(transmission2_str,mcode1_str)
    mcode2_InTransmission2 = hasMaliciousCode(transmission2_str,mcode2_str)
    mcode3_InTransmission2 = hasMaliciousCode(transmission2_str,mcode3_str)
    
    #Transmision 1 mcode 1
    print(True, mcode1_InTransmission1[0] + 1) if len(mcode1_InTransmission1) > 0 else print(False)
    #Transmision 1 mcode 2
    print(True, mcode2_InTransmission1[0] + 1) if len(mcode2_InTransmission1) > 0 else print(False)
    #Transmision 1 mcode 3
    print(True, mcode3_InTransmission1[0] + 1) if len(mcode3_InTransmission1) > 0 else print(False)
    #Transmision 2 mcode 1
    print(True, mcode1_InTransmission2[0] + 1) if len(mcode1_InTransmission2) > 0 else print(False)
    #Transmision 2 mcode 2
    print(True, mcode2_InTransmission2[0] + 1) if len(mcode2_InTransmission2) > 0 else print(False)
    #Transmision 2 mcode 3
    print(True, mcode3_InTransmission2[0] + 1) if len(mcode3_InTransmission2) > 0 else print(False)

    #Resultados segunda parte
    #Palindromo mas largo transimision 1
    transmission1Palindrome = longestPalindrome(transmission1_str)
    print(transmission1Palindrome[0] + 1, transmission1Palindrome[1] + 1)
    #Palindromo mas largo transimision 2
    transmission2Palindrome = longestPalindrome(transmission2_str)
    print(transmission2Palindrome[0] + 1, transmission2Palindrome[1] + 1)


    #Resultados tercera partes
    #Inicio y final de coincidencia mas larga en transmision 1 (-1 si no hay concidencias)
    similarity = longestSimilarity(transmission1_str,transmission2_str)
    print(similarity[0] + 1, similarity[1] + 1)
    return 0

main()