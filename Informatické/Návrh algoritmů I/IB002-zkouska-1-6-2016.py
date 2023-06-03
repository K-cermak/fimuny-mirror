#!/usr/bin/python
import sys

"""
Zadani:

Vasim ukolem je implementovat funkce, ktere pracuji s datovou strukturou 2-3 strom.
2-3 strom je B-strom, jehoz kazdy vnitrni uzel obsahuje 1 nebo 2 klice (a tedy 2 nebo 3 potomky).
Prazdny strom ma korenovy uzel None. Delka vetvi musi byt stejna (vsechny listy jsou ve
stejne hloubce od korene) a zaroven musi platit vyhledavaci vlastnost.

Ve vsech ukolech muzete predpokladat, ze strom neobsahuje dva klice se stejnou hodnotou.
Take muzete predpokladat, ze hodnoty keyCount a isLeaf jsou v celem strome nastaveny korektne.

1. ukol (10 bodu): Implementovat funkci firstK, ktera ulozi prvnich k klicu vzestupne podle
    velikosti ze zadaneho stromu do pripraveneho seznamu.
2. ukol (10 bodu): Implementovat funkci checkDepth, ktera overi, ze vsechny vetve maji
    stejnou hloubku.
3. ukol (10 bodu): Implementovat funkci check23Tree, ktera overi, zda plati vyhledavaci
    vlastnost (vztah mezi hodnotami klicu v uzlech a klicu v odpovidajicich podstromech).
4. ukol (20 bodu): Implementovat funkci findSuccNode ktera nalezene uzel s klicem,
    ktery je nejmensim klicem vetsim nez zadany klic.
"""

"""
Po spusteni se generuji soubory se stromy na kterych jsou funkce testovany.
Pro jejich vizualizaci muzete pouzit nastroj Graphviz.
Vygenerovane soubory nahrajte do online nastroje pro zobrazeni graphvizu:
http://sandbox.kidstrythisathome.com/erdos/
nebo http://www.webgraphviz.com/

Alternativne muzete pouzit prekladac z jazyka dot do obrazku na svem pocitaci.
"""

# Trida reprezentujici uzel 2-3 stromu.
# 'keys' - pole klicu
# 'keyCount' - pocet klicu
# 'isLeaf' - True pokud je uzel listem, jinak False
# 'parent' - ukazatel na rodice uzlu
# 'children' - pole ukazatelu na potomky
class MultiNode:
    def __init__(self):
        self.keys = [None] * 2
        self.keyCount = 0
        self.isLeaf = False
        self.parent = None
        self.children = [None] * 3

# Trida reprezentujici 2-3 strom.
# 'root' - ukazatel na koren stromu
class MultiTree:
    def __init__(self):
        root = None

# Ukol 1
# Ulozi prvnich k klicu (brano vzestupne podle velikosti) ze zadaneho stromu do pripraveneho seznamu 'nodeList'.
# Funkce predpoklada, ze na vstupu je korektni 2-3 strom a ze pripraveny seznam je prazdny.
#
# Pro zisk plneho poctu bodu je pozadovano reseni s lepsi nez linearni casovou slozitosti vuci velikosti
# (poctu uzlu) vstupniho stromu.
#
# :param 'tree' vstupni 2-3 strom
# :param 'nodeList' seznam, do ktereho se maji pridat klice ze stromu 'tree'
# :param 'k' pocet klicu, ktere se maji vlozit
#
# Klice do seznamu vkladejte v poradi podle velikosti.
#
# Pro vkladani do nodeList pouzijte funkci append(key), kde 'key' je pridavany klic.
# Jinak nodeList nemodifikujte! Zjistit delku seznamu je mozne pomoci len(nodeList).
def firstK(tree, nodeList, k):
    node = tree.root
    if tree.root == None:
        return nodeList
    
    return firstKRec(tree, nodeList, k, node)


def firstKRec(tree, nodeList, k, node):
    if len(nodeList) == k:
        return nodeList

    if node.isLeaf == True:
        for i in range(k - len(nodeList)):
            if i >= node.keyCount:
                return nodeList
            nodeList.append(node.keys[i])
        return nodeList
    
    else:
        for i in range(node.keyCount + 1):
            firstKRec(tree, nodeList, k, node.children[i])
            
            if len(nodeList) == k:
                return nodeList
            
            if i < node.keyCount:
                nodeList.append(node.keys[i])

            if len(nodeList) == k:
                return nodeList

    return nodeList
    

# Ukol 2
# Implementujte funkci checkDepth, ktera overi, ze vsechny vetve maji stejnou delku.
# Muzete predpokladat, ze hodnoty keyCount a isLeaf jsou v celem strome nastaveny korektne,
# a ze sedi pocty uzlu a nasledniku.
#
# :param 'tree' strom, pro ktery testujeme, zdali vsechny jeho vetve maji stejnou delku
# :return 'True' pokud vsechny vetve maji stejnou delku, jinak 'False'
def checkDepth(tree):
    node = MultiNode()

    if tree.root == None:
        return True
    
    node = tree.root
    if checkDepthRec(tree, node) == False:
        return False
    else:
        return True
    
def checkDepthRec(tree, node):
    
    if node.isLeaf == True:
        return 1
    
    else:
        count1 = checkDepthRec(tree, node.children[0])       
        count2 = checkDepthRec(tree, node.children[1])
        if node.keyCount == 2:
            count3 = checkDepthRec(tree, node.children[2])
            
            if count1 == count2 == count3 != False:
                return count1 + 1
            else:
                return False

        else:
            if count1 == count2 != False:
                return count1 + 1
            else:
                return False
                
            
        
    
# Ukol 3
# Implementujte funkci check23Tree, ktera overi, zda plati vyhledavaci
# vlastnost (vztah mezi hodnotami klicu v uzlech a klicu v odpovidajicich podstromech).
#
# :param 'tree' strom, ktery funkce testuje
# :return 'True', pokud vyhledavaci vlastnost plati, jinak 'False'
def check23Tree(tree):
    if tree.root == None:
        return True
    node = tree.root
    return check23TreeRec(tree, node, None, None)
        
def check23TreeRec(tree, node, minimal, maximal):
    if maximal != None and maximal < node.keys[node.keyCount - 1]:
        return False
    if minimal != None and minimal > node.keys[0]:
        return False

    for i in range(1, node.keyCount):
        if node.keys[i] < node.keys[i - 1]:
            return False
        
    if node.isLeaf != True:
        correct1 = check23TreeRec(tree, node.children[0], None, node.keys[0])
        if correct1 == False:
            return False
        
        if node.keyCount == 1:
            correct2 = check23TreeRec(tree, node.children[1], node.keys[0], None)
            if correct2 == False:
                return False
            
        if node.keyCount == 2:
            correct2 = check23TreeRec(tree, node.children[1], node.keys[0], node.keys[1])
            correct3 = check23TreeRec(tree, node.children[2], node.keys[1], None)
            if correct3 == False or correct2 == False:
                return False

    return True
# Ukol 4
# Implementujte funkci findSuccNode, ktera nalezene ve strome 'tree' 
# uzel s nejmensim klicem takovym, ze je vetsi nez hodnota 'key'.
# Pro zisk plneho poctu bodu pozadujeme reseni s logaritmickou slozitosti (vuci poctu uzlu).
# Funkce predpoklada, ze na vstupu je korektni 2-3 strom.
#
# Napoveda: Hledany uzel se nachazi na vetvi z korene stromu do listu, 
# do ktereho by patril klic (o malinko vetsi nez) 'key'.
# S vyhodou lze vyuzit funkce succSearch, jejiz hlavicku mate k dispozici.
#
# :param 'tree' strom, ve kterem hledame uzel s klicem, ktery je nejmensim klicem,
# ktery je vetsi nez hodnota 'key'.
# :param 'key' hodnota pro hledani uzlu
# :return nalezeny uzel. Pokud takovy uzel neexistuje, vrati 'None'.
def findSuccNode(tree, key):
    if tree.root == None:
        return None

    node = tree.root
    return succSearch(node, key, None, None)
    

def succSearch(node, key, candidate, candidateNode):
    for i in range(node.keyCount):
        if node.keys[i] < candidate and node.keys[i] > key:
            candidate = node.keys[i]
            candidateNode = node
        if candidate == None and node.keys[i] > key:
            candidate = node.keys[i]
            candidateNode = node
    if node.isLeaf == True:
        return candidateNode
    for i in range(node.keyCount):
        if key < node.keys[i]:
            return succSearch(node.children[i], key, candidate, candidateNode)
    return succSearch(node.children[node.keyCount], key, candidate, candidateNode)
        
        
# Hlavni funkce volana automaticky po spusteni programu.
# Pokud chcete krome dodanych testu spustit vlastni testovaci kod, dopiste ho sem.
# Odevzdavejte reseni s puvodni verzi teto funkce.
def main():

    testCheckList()
    print("")
    testCheckDepth()
    print("")
    testCheck23tree()
    print("")
    testFindSuccNode()

########################################################################
###             Nasleduje kod testu, NEMODIFIKUJTE JEJ               ###
########################################################################

"""
Dodatek k graphvizu:
Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
coz se hodi predevsim pro ladeni.
Tento program generuje nekolik souboru neco.dot v mainu
Vygenerovane soubory nahrajte do online nastroje pro zobrazeni graphvizu:
http://sandbox.kidstrythisathome.com/erdos/
nebo http://graphviz-dev.appspot.com/ - zvlada i vetsi grafy

Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku na svuj pocitac.
"""
def make_graphviz(node, i, f):
    if node == None:
        return
    f.write("node%i [label = \""%i)
    for j in range(0, node.keyCount):
        f.write("<f%i> |%i| "%(j, node.keys[j]))
    f.write("<f%i>\"];\n" % len(node.keys))

    for j in range(0, node.keyCount+1):
        make_graphviz(node.children[j], (i + 1) * 3 + j, f)

    if node.isLeaf == False:
        for j in range(0, node.keyCount+1):
            value = (i + 1) * 3 + j
            f.write("\"node%i\":f%i -> \"node%i\"\n" % (i, j, value))

def make_graph(tree, filename):
    height = 0
    node = tree.root
    while node != None:
        height += 1
        node = node.children[0]

    f = open(filename, 'w')
    f.write("digraph BTree {\n")
    f.write("node [shape = record,height=.%i];\n" % (height - 1))
    make_graphviz(tree.root, 0, f)
    f.write("}\n")

# Pomocna funkce pro vypis 2-3 stromu pomoci vypisu inorder
def inorderPrintTree(tree):
    if tree.root is None:
        return "None"
    else:
        return inorderPrint(tree.root)

def inorderPrint(n):
    output = ""
    if n is None:
        return output

    if n.isLeaf:
        output += "("
        for i in range(0, n.keyCount):
            output += " "
            output += str(n.keys[i])
        output += " )"

        return output
    else:
        output += "("
        for i in range(0, n.keyCount):
            output += inorderPrint(n.children[i])
            output += str(n.keys[i])

        output += inorderPrint(n.children[n.keyCount])
        output += (")")

        return output

# Vytvori uzel 2-3-stromu, priradi jeden klic a oznaci za list.
def createMultiNode(key):
    node = MultiNode()
    node.parent = None
    node.keys[0] = key
    node.keyCount = 1
    node.isLeaf = True

    return node

def make23Tree(nodeList):
    t = MultiTree()
    t.root = make23Node(None, nodeList)
    return t

def make23Node(parent, list):

    if list is None or len(list) == 0:
        return None

    node = createMultiNode(list[0])
    node.parent = parent

    if isinstance(list[1], (int)):
        node.keys[1] = list[1]
        node.keyCount = 2

        node.children[0] = make23Node(node, list[2])
        node.children[1] = make23Node(node, list[3])
        node.children[2] = make23Node(node, list[4])

        if node.children[0] or node.children[1] or node.children[2]:
            node.isLeaf = False
    else:
        node.children[0] = make23Node(node, list[1])
        node.children[1] = make23Node(node, list[2])

        if node.children[0] or node.children[1]:
            node.isLeaf = False

    return node


def testCheckList():

    TESTCOUNT = 5
    failure = False

    treeList = [
        [],
        [1, [], []],
        [8, 9, [], [], []],
        [10, 30, [8, 9, [], [], []], [12, 15, [], [], []], [35, [], []]],
        [12, 30, [8, [5, [], []], [9, [], []]], [15, 28, [14, [], []], [20, [], []], [29, [], []]],
         [35, [32, [], []], [40, [], []]]]
    ]

    queryList = [0, 1, 2, 5, 100]

    expectedResults = [
        [[], [], [], [], []],
        [[], [1], [1], [1], [1]],
        [[], [8], [8, 9], [8, 9], [8, 9]],
        [[], [8], [8, 9], [8, 9, 10, 12, 15], [8, 9, 10, 12, 15, 30, 35]],
        [[], [5], [5, 8], [5, 8, 9, 12, 14], [5, 8, 9, 12, 14, 15, 20, 28, 29, 30, 32, 35, 40]]
    ]

    for i in range(0, TESTCOUNT):
        tree = make23Tree(treeList[i])
        for j in range(0, TESTCOUNT):
            output = []
            firstK(tree, output, queryList[j])

            if output != expectedResults[i][j]:
                failure = True
                print("Kontrola vyhledani prvnich k prvku: NOK")
                print ("Spatna detekce u stromu: \"" + inorderPrintTree(tree) + "\" a k = " + str(queryList[j]))
                sys.stdout.write("Vysledny list vypada takto: ")
                print(output)
                sys.stdout.write("Ale ocekavane hodnoty jsou tyto: ")
                print(expectedResults[i][j])

                file = "ukol1_test" + str(i+1) + ".dot"
                print("Vzor testovaneho stromu vygenerovan do souboru: " + file);
                make_graph(tree, file);
                break
        if failure:
            break

    if failure == False:
        print("Kontrola vyhledani prvnich k prvku: OK")


def testCheck23tree():

    TESTCOUNT = 10
    failure = False

    treeList = [
        [],
        [5, [3, [1, [], []], [4, [], []]], [8, [7, [], []], [10, [], []]]],
        [10, [1, 5, [], [], []], [15, 20, [], [], []]],
        [12, 30, [8, [5, [], []], [9, [], []]], [15, 28, [14, [], []], [20, [], []], [29, [], []]],
         [35, [32, [], []], [40, [], []]]],
        [30, 10, [], [], []],
        [10, 30, [8, 5, [], [], []], [15, [], []], [35, [], []]],
        [10, 30, [8, 14, [], [], []], [15, [], []], [35, [], []]],
        [10, 30, [8, 9, [], [], []], [15, 31, [], [], []], [35, [], []]],
        [10, 30, [8, 9, [], [], []], [15, 28, [], [], []], [29, [], []]],
        [12, 30, [8, [5, [], []], [9, [], []]], [11, 28, [14, [], []], [20, [], []], [29, [], []]],
         [35, [32, [], []], [40, [], []]]]
    ]

    expectedResults = [True, True, True, True, False, False, False, False, False, False]

    failMessages = [
        "Strom je korektni",
        "Strom je korektni",
        "Strom je korektni",
        "Strom je korektni",
        "Strom neni korektni - ma spatne usporadene prvky ve vnitrnim uzlu.",
        "Strom neni korektni - ma spatne usporadene prvky v listu.",
        "Strom neni korektni - nejlevejsi podstrom nema prvky ve spravnem rozsahu.",
        "Strom neni korektni - prostredni podstrom nema prvky ve spravnem rozsahu.",
        "Strom neni korektni - nejpravejsi podstrom nema prvky ve spravnem rozsahu.",
        "Strom neni korektni - prostredni podstrom nema prvky ve spravnem rozsahu (chybi kontrola"
            " prvniho a tretiho patra - spatne je uzel s klicem 11."
    ]

    for i in range(0, TESTCOUNT):
        tree = make23Tree(treeList[i])
        if check23Tree(tree) != expectedResults[i]:
            failure = True
            print("Kontrola stromu: NOK")
            print ("Spatna detekce u stromu: \"" + inorderPrintTree(tree) +
                   "\" - " + failMessages[i])

            file = "ukol3_test" + str(i+1) + ".dot"
            print("Vzor testovaneho stromu vygenerovan do souboru: " + file);
            make_graph(tree, file);
            break

    if failure == False:
        print("Kontrola stromu: OK")

def testCheckDepth():

    TESTCOUNT = 7
    failure = False

    treeList = [
        [],
        [1, [], []],
        [5, [3, [1, [], []], [4, [], []]], [8, [7, [], []], [10, [], []]]],
        [10, 30, [1, 5, [], [], []], [15, 20, [], [], []], [35, 100, [], [], []]],
        [10, 30, [8, [5, [], []], [9, [], []]], [15, [], []], [35, [], []]],
        [10, 30, [8, [], []], [15, [], []], [35, [32, [], []], [40, [], []]]],
        [10, 30, [8, [5, [], []], [9, [], []]], [15, [], []], [35, [32, [], []], [40, [], []]]]
    ]

    expectedResults = [True, True, True, True, False, False, False]

    failMessages = [
        "Strom ma vetve stejne dlouhe",
        "Strom ma vetve stejne dlouhe",
        "Strom ma vetve stejne dlouhe",
        "Strom ma vetve stejne dlouhe",
        "Strom ma delsi nejlevejsi vetev",
        "Strom ma delsi nejpravejsi vetev",
        "Strom ma kratsi prostredni vetev.",
    ]

    for i in range(0, TESTCOUNT):
        tree = make23Tree(treeList[i])
        if checkDepth(tree) != expectedResults[i]:
            failure = True
            print("Kontrola hloubky: NOK")
            print ("Spatna detekce u stromu: \"" + inorderPrintTree(tree) +
                   "\" - " + failMessages[i])

            file = "ukol2_test" + str(i+1) + ".dot"
            print("Vzor testovaneho stromu vygenerovan do souboru: " + file);
            make_graph(tree, file);
            break

    if failure == False:
        print("Kontrola hloubky: OK")

def testFindSuccNode():

    TESTCOUNT = 5
    failure = False

    treeList = [
        [],
        [1, [], []],
        [8, 9, [], [], []],
        [10, 30, [8, 9, [], [], []], [12, 15, [], [], []], [35, [], []]],
        [12, 30, [8, [5, [], []], [9, [], []]], [15, 28, [14, [], []], [20, [], []], [29, [], []]],
         [35, [32, [], []], [40, [], []]]]
    ]

    queryList = [0, 8, 11, 36, 41]

    expectedResults = [
        [None, None, None, None, None],
        [[1], None, None, None, None],
        [[8, 9], [8, 9], None, None, None],
        [[8, 9], [8, 9], [12, 15], None, None],
        [[5], [9], [12, 30], [40], None]
    ]

    for i in range(0, TESTCOUNT):
        tree = make23Tree(treeList[i])
        for j in range(0, TESTCOUNT):
            result = findSuccNode(tree, queryList[j])

            # kontrola vraceni jineho typu nez typu Multinode
            if result is not None and not isinstance(result, MultiNode):
                failure = True
                print("Kontrola Hledani naslednika: NOK")
                sys.stdout.write("Pro strom ")
                print(inorderPrintTree(tree))
                sys.stdout.write("Nebyl vracen uzel stromu (nebo None), ale hodnota typu ")
                print(type(result))
                break

            if getMultinodeAsList(result) != expectedResults[i][j]:
                failure = True
                print("Kontrola Hledani naslednika: NOK")
                sys.stdout.write("Pro strom: \"")
                sys.stdout.write(inorderPrintTree(tree))
                sys.stdout.write("\" a hodnotu: ")
                print(queryList[j])
                sys.stdout.write("Byl nalezen uzel: ")
                print(getMultinodeAsList(result))
                sys.stdout.write("Ale ocekava se tento: ")
                print(expectedResults[i][j])

                file = "ukol4_test" + str(i+1) + ".dot"
                print("Vzor testovaneho stromu vygenerovan do souboru: " + file);
                make_graph(tree, file);
                break
        if failure:
            break

    if failure == False:
        print("Kontrola hledani naslednika: OK")

def getMultinodeAsList(node):
    if node is None:
        return None
    if node.keyCount == 2:
        return [node.keys[0], node.keys[1]]
    elif node.keyCount == 1:
        return [node.keys[0]]
    else: # nemelo by vubec nastat
        return None

def makeListFromNode(node):
    if node is None:
        return None
    if node.keyCount == 2:
        return [node.keys[0], node.keys[1]]
    elif node.keyCount == 1:
        return [node.keys[0]]


if __name__ == '__main__':
    main()
