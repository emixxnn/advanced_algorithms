# Sergio Santiago Sánchez Salazar A01645255
# Emiliano Nuñez Felix A01645413


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


def searchWordInTrie(trie: TrieNode, word: str):
    currentNode = trie
    for char in word:
        charIndex = ord(char.lower()) - ord("a")
        if currentNode.children[charIndex]:
            currentNode = currentNode.children[charIndex]

        else:
            return False

    return currentNode.isEndOfWord


# Funcion generada por Gemini CLI para imprimir el trie como un arbol
def print_trie_as_tree(node: TrieNode, level=0):
    for i, child in enumerate(node.children):
        if child:
            char = chr(ord("a") + i)
            indent = "  " * level
            marker = " (*)" if child.isEndOfWord else ""
            print(f"{indent}{char}{marker}")
            print_trie_as_tree(child, level + 1)


def main():
    n = int(input("Numero de palabras: "))
    trie = TrieNode()
    for _ in range(n):
        word = input()
        currentNode = trie
        for char in word:
            charIndex = ord(char.lower()) - ord("a")
            if not currentNode.children[charIndex]:
                currentNode.children[charIndex] = TrieNode()
            currentNode = currentNode.children[charIndex]
        currentNode.isEndOfWord = True

    print_trie_as_tree(trie)
    print()
    m = int(input("Numero de busquedas: "))
    for _ in range(m):
        word = input()
        print(searchWordInTrie(trie, word))


main()
