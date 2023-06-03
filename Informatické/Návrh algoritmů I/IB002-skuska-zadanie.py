#!/usr/bin/python3
import ast
import random
from collections import deque

# Zadani:
# V tomto prikladu budeme pracovat s maximovou haldou.


class MaxHeap:
    """Trida reprezetujici maximovou haldu.

    Atributy:
        size    pocet prvku v halde
        array   pole prvku haldy
    """
    def __init__(self):
        self.size = 0
        self.array = None

# Pro praci s touto tridou reprezentujici maximovou haldu muzete s vyhodou
# pouzit funkce parent_index(), left_index(), right_index(), swap(), parent(),
# left(), right(), ktere jste implementovali v zakladnim domacim ukolu cv06.


# Ukol 1. (10 bodu)
# Implementujte funkci heap2Tree(heap), ktera prevede zadanou maximovou haldu
# typu MaxHeap na strom reprezentujici predstavu haldy ve stromove strukture.
# Vystupem je tedy trida typu Tree definovana nize.
#
# Napr. vystupem pro haldu [12, 3, 9, 1, 2, 4] bude strom
#          (12)
#        /      \
#      (3)      (9)
#     /   \     /
#   (1)   (2) (4)


class Tree:
    """Trida Tree slouzi k reprezentaci stromu.

    Atributy:
        root    odkaz na korenovy uzel typu Node
    """
    def __init__(self):
        self.root = None


class Node:
    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu (cele cislo)
        left    odkaz na leveho potomka (None, pokud neexistuje)
        right   odkaz na praveho potomka (None, pokud neexistuje)
    """
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def heap2Tree(heap):
    """
    vstup: 'heap' korektni maximova halda typu MaxHeap
    vystup: strom typu Tree reprezentujici haldu 'heap'
    casova slozitost: O(n), kde 'n' je pocet prvku haldy 'heap'
    """
    return None  # TODO


# Ukol 2. (10 bodu)
# Implementujte funkci isLSHeap(heap), ktera overi, zda je na vstupu zadana
# halda (typu MaxHeap) korektni maximovou Left-Smaller haldou.
#
# Maximova halda je Left-Smaller, pokud je korektni maximovou haldou a navic
# pro kazdy jeji prvek se dvema potomky plati, ze levy potomek je mensi nebo
# roven pravemu.
#
# Je Left-Smaller halda | Neni Left-Smaller halda
#                       |
#       (3)             |           (3)
#      /   \            |          /   \
#    (1)   (2)          |        (2)   (1)
#
# Pro jistotu jeste doplnme, ze prazdna i jednoprvkova halda jsou korektni
# maximove Left-Smaller haldy.

def isLSHeap(heap):
    """
    vstup: 'heap' typu MaxHeap
    vystup: True, pokud je 'heap' korektni maximovou Left-Smaller haldou
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet prvku haldy 'heap'
    """
    return False  # TODO


# Ukol 3. (15 bodu)
# Implementujte funkci minsOfSubtrees(heap), ktera vypocita pro kazdou polozku
# maximove haldy, jaky je minimalni prvek v 'podstromu' tohoto prvku.
# Vstupem je korektni maximova halda. Vystupem je pole stejne delky jako halda,
# kde na kazde pozici je vlozena minimalni hodnota v podstromu odpovidajicim
# teto pozici.
# Napr. pro maximovou haldu [12, 4, 9, 2, 3, 6, 5, 1] vrati
# [1, 1, 5, 1, 3, 6, 5, 1], protoze ve stromove reprezentaci vypada halda jako
#           (12)          a minima v podstromech jsou tedy         (1)
#         /      \                                               /      \
#       (4)      (9)                                           (1)      (5)
#      /   \     /  \                                         /   \     /  \
#    (2)   (3) (6)  (5)                                     (1)   (3) (6)  (5)
#   /                                                      /
# (1)                                                    (1)

def minsOfSubtrees(heap):
    """
    vstup: 'heap' korektni maximova halda typu MaxHeap
    vystup: Pythonove pole typu list s podstromovymi minimy
    casova slozitost: O(n), kde 'n' je pocet prvku haldy 'heap'
    """
    return [None] * heap.size  # TODO


# Ukol 4. (15 bodu)
# Implementujte funkci fixLSHeap(heap), ktera zadanou maximovou haldu 'heap'
# prepracuje tak, aby (obsahovala stejna cisla a) byla korektni maximovou
# Left-Smaller haldou. Funkce bude menit primo haldu zadanou v argumentu,
# proto nebude vracet zadnou navratovou hodnotu.
#
# Napoveda:
# Pro algoritmus s linearni casouvou slozitosti je potreba postupovat takto:
#  - rekurzivne resime od 'korene' k 'listum' haldy
#  - pro kazdou polozku:
#    - zkontrolujeme, jestli potomci splnuji LS vlastnost, pokud ne:
#      - prohodime hodnoty v left a right
#      - tim se muze pokazit vlastnost haldy v levem podstrome, proto
#        probublame problematickou hodnotu z korene leveho podstromu tak
#        hluboko, ze uz nebude porusovat vlastnost haldy (pri tomto bublani
#        opravujeme jen vlastnost haldy, LS vlastnost neresime)
#  - mame tedy korektni maximovou haldu, ktera navic splnuje LS vlastnost od
#    teto pozice nahoru
#  - pokracujeme v rekurzi vlevo a vpravo

def fixLSHeap(heap):
    """
    vstup: 'heap' korektni maximova halda typu MaxHeap
    vystup: nic, opravili jsme 'heap' na korektni maximovou Left-Smaller haldu
    casova slozitost: O(n), kde 'n' je pocet prvku haldy 'heap'
    """
    pass  # TODO


"""
Soubory .dot z testu vykreslite napr. na http://www.webgraphviz.com/.
"""

########################################################################
#               Nasleduje kod testu, NEMODIFIKUJTE JEJ                 #
########################################################################


def makeGraph(tree, fileName):
    """
    Zde mate k dispozici funkci `makeGraph`, ktera vam z `tree` na vstupu
    vygeneruje do souboru `fileName` reprezentaci stromu pro graphviz.
    Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
    coz se hodi predevsim pro ladeni.
    Pro zobrazeni graphvizu muzete vyuzit:
    http://www.webgraphviz.com/
    """

    def makeNode(id, label):
        f.write("{} [label=\"{}\"]\n".format(id, label))

    def makeEdge(n1, n2):
        f.write("{} -> {}\n".format(n1, n2))

    def checkChild(node, child, label):
        if child is None:
            makeNode("{}{}".format(label, id(node)), "Nil\", color=\"white")
            makeEdge(id(node), "{}{}".format(label, id(node)))
        else:
            makeEdge(id(node), id(child))
            makeGraphviz(child, f)

    def makeGraphviz(node, f):
        if node is None:
            return
        makeNode(id(node), node.key)
        checkChild(node, node.left, 'L')
        checkChild(node, node.right, 'R')

    with open(fileName, 'w') as f:
        f.write("digraph Tree {\n")
        f.write("node [color=lightblue2, style=filled, ordering=\"out\"];\n")
        if (tree is not None) and (tree.root is not None):
            makeGraphviz(tree.root, f)
        f.write("}\n")


def ib002_comp_trees(t1, t2):
    if (t1 is None) and (t2 is None):
        return True
    if (t1 is None) or (t2 is None):
        return False
    return (t1.key == t2.key) and ib002_comp_trees(t1.left, t2.left) \
        and ib002_comp_trees(t1.right, t2.right)


def ib002_random_maxdata(size=10):
    arr = [None] * size
    ib_maxval = size*10
    for i in range(len(arr)):
        arr[i] = random.randint(ib_maxval-30, ib_maxval)
        ib_maxval = arr[i//2]
    return arr


def ib002_lt(teq):
    q = deque()
    index = 1
    ssee = Tree()
    if not teq or teq[0] is None:
        return ssee
    ssee.root = Node(teq[0])
    q.append(ssee.root)

    while len(q):
        node = q.popleft()
        if len(teq) > index:
            node.left = None if teq[index] is None else Node(teq[index])
            if node.left:
                q.append(node.left)
            index += 1
        if len(teq) > index:
            node.right = None if teq[index] is None else Node(teq[index])
            if node.right:
                q.append(node.right)
            index += 1
    return ssee


def ib002_test_heap2Tree():
    error_count = 0
    print("\n**heap2Tree testing")
    for line in tree_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            return
        heap = MaxHeap()
        seq = list(ast.literal_eval(line))
        trs = ib002_lt(seq)
        heap.size = len(seq)
        heap.array = seq
        tree_stud = heap2Tree(heap)
        if tree_stud is None:
            error_count += 1
            filename_corr = "Er_heap2Tree_" + str(error_count) + "corr.dot"
            makeGraph(trs, filename_corr)
            print("FAIL, pro haldu {} melo vratit strom v souboru {}, "
                  "ale vratilo None"
                  "".format(seq, filename_corr))
        elif not(ib002_comp_trees(trs.root, tree_stud.root)):
            error_count += 1
            filename_corr = "Er_heap2Tree_" + str(error_count) + "corr.dot"
            makeGraph(trs, filename_corr)
            filename_stud = "Er_heap2Tree_" + str(error_count) + "your.dot"
            makeGraph(tree_stud, filename_stud)
            print("FAIL, pro haldu {} melo vratit strom v souboru {}, "
                  "ale vratilo strom v souboru {}"
                  "".format(seq, filename_corr, filename_stud))
    for i in range(200):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        heap = MaxHeap()
        seq = ib002_random_maxdata(random.randint(0, 30))
        trs = ib002_lt(seq)
        heap.size = len(seq)
        heap.array = seq
        tree_stud = heap2Tree(heap)
        if tree_stud is None:
            error_count += 1
            filename_corr = "Er_heap2Tree_" + str(error_count) + "corr.dot"
            makeGraph(trs, filename_corr)
            print("FAIL, pro haldu {} melo vratit strom v souboru {}, "
                  "ale vratilo None"
                  "".format(seq, filename_corr, filename_stud))
        elif not(ib002_comp_trees(trs.root, tree_stud.root)):
            error_count += 1
            filename_corr = "Er_heap2Tree_" + str(error_count) + "corr.dot"
            makeGraph(trs, filename_corr)
            filename_stud = "Er_heap2Tree_" + str(error_count) + "your.dot"
            makeGraph(tree_stud, filename_stud)
            print("FAIL, pro haldu {} melo vratit strom v souboru {}, "
                  "ale vratilo strom v souboru {}"
                  "".format(seq, filename_corr, filename_stud))
    if error_count == 0:
        print("heap2Tree OK")


tree_data = """[5, 2, 1]
[]
[1]
[5, 4, 2, 3, 1]
[5, 4, 2, 3]
[2013]
[12, 3, 9, 1, 2, 4]
[23, 13, 9, 8, 6, 7, 5]"""


def ib002_bool_(s):
    return s == "True"


def ib002_is_LS(is_ls):
    if is_ls:
        return "ma byt maximova LS halda"
    else:
        return "nema byt maximova LS halda"


def ib002_test_isLSHeap():
    error_count = 0
    print("\n**isLSHeap testing")
    for line in LS_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        heap = MaxHeap()
        seq, res = line.rstrip().split('; ')
        seq = list(ast.literal_eval(seq))
        heap.size = len(seq)
        heap.array = seq
        res = ib002_bool_(res)
        if isLSHeap(heap) != res:
            error_count += 1
            print("FAIL, {} {}".format(seq, ib002_is_LS(res)))
    if error_count == 0:
        print("isLSHeap OK")


LS_data = """[5, 2, 1]; False
[1, 3, 2]; False
[1]; True
[1, 1, 1]; True
[5, 4, 2, 3, 1]; False
[5, 3, 4, 1, 2]; True
[5, 3, 4, 2, 1]; False
[5, 4, 2, 3]; False
[5, 3, 4, 2]; True
[2013]; True
[]; True
[12, 3, 9, 1, 2, 4]; True
[12, 3, 9, 1, 1, 4]; True
[23, 13, 9, 8, 6, 7, 5]; False
[59, 49, 46, 34, 32, 17]; False
[71, 55, 56, 47, 47, 42, 43, 27, 29]; True
[129, 119, 112, 109, 98, 103, 89, 79, 103, 96, 81, 100, 93]; False
[29, 23, 1, 22, -1]; False
[39, 21, 21, 12, 11, 8]; False
[7, -9, -2]; True
[88, 68, 81, 49, 52, 72, 55, 34, 28, 49, 51]; False
[5]; True
[105, 88, 82, 73, 86, 78, 58, 56, 43, 62, 84]; False
[73, 45, 46, 22, 42, 22, 30, 21, 18, 28]; False
[48, 20, 32, 14, 6, 25, 16]; False
[17, -13, -2, -18]; True
[24, 1, 1, -6]; True
[69, 50, 66, 27, 23, 45, 43]; False
[121, 118, 93, 101, 107, 88, 76, 87, 100, 87, 97, 59, 87, 71, 64]; False
[0]; True
[75, 49, 47, 34, 45, 45, 43, 14, 8, 15]; False
[121, 95, 97, 78, 72, 92, 84, 49, 55, 66, 47, 87, 87]; False
[-15]; True
[116, 106, 100, 96, 102, 99, 99, 84, 69, 82, 72, 78, 95]; False"""


def ib002_test_minsOfSubtrees():
    error_count = 0
    print("\n**minsOfSubtrees testing")
    for line in Min_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        heap = MaxHeap()
        seq, res = line.rstrip().split('; ')
        seq = list(ast.literal_eval(seq))
        res = list(ast.literal_eval(res))
        heap.size = len(seq)
        heap.array = seq
        old_seq = list(seq)
        stud_seq = minsOfSubtrees(heap)
        if old_seq != heap.array:
            error_count += 1
            print("FAIL, zmenilo se pole v zadane halde {} na {}"
                  "".format(old_seq, seq))
        elif len(old_seq) != heap.size:
            error_count += 1
            print("FAIL, zmenilo se .size v zadane halde {} z {} na {}"
                  "".format(old_seq, len(old_seq), heap.size))
        elif stud_seq != res:
            error_count += 1
            print("FAIL, pro {} vracite {} misto {}"
                  "".format(old_seq, stud_seq, res))
    if error_count == 0:
        print("minsOfSubtrees OK")


Min_data = """[5, 2, 1]; [1, 2, 1]
[]; []
[1]; [1]
[1, 1, 1]; [1, 1, 1]
[5, 4, 2, 3, 1]; [1, 1, 2, 3, 1]
[5, 3, 2, 3, 1]; [1, 1, 2, 3, 1]
[5, 4, 2, 3]; [2, 3, 2, 3]
[2013]; [2013]
[2013, 2011]; [2011, 2011]
[23, 21, 6, 3, -7]; [-7, -7, 6, 3, -7]
[23, 15, -6, 3]; [-6, 3, -6, 3]
[15, -5, -13]; [-13, -5, -13]
[12, 3, 9, 1, 2, 4]; [1, 1, 4, 1, 2, 4]
[12, 4, 9, 2, 3, 6, 5, 1]; [1, 1, 5, 1, 3, 6, 5, 1]
[23, 13, 9, 8, 6, 7, 5]; [5, 6, 5, 8, 6, 7, 5]
[11, 11, 8, 9, 9, 8, 7, 6, 8, 7, 7, 6]; [6, 6, 6, 6, 7, 6, 7, 6, 8, 7, 7, 6]
[86, 75, 86, 65, 51, 62, 61, 51, 45, 3]; [3, 3, 61, 45, 3, 62, 61, 51, 45, 3]
[11, 11, 11, 10, 9, 10, 9, 7, 9, 7, 7, 8]; [7, 7, 8, 7, 7, 8, 9, 7, 9, 7, 7, 8]
[83, 65, 71, 45, 59, 63, 67, 5, 45, 40]; [5, 5, 63, 5, 40, 63, 67, 5, 45, 40]
[60, 53, 39, 24, 34, 35]; [24, 24, 35, 24, 34, 35]
[60, 57, 59, 53, 30, 49, 32, 48]; [30, 30, 32, 48, 30, 49, 32, 48]"""


def ib002_is_mh(h):
    for i in range(1, h.size):
        if h.array[i] > h.array[(i-1)//2]:
            print(i)
            return False
    return True


def ib002_test_fixLSHeap():
    error_count = 0
    print("\n**fixLSHeap testing")
    print("Pouziva vas vlastni isLSHeap()!\n")
    for i in range(200):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        heap = MaxHeap()
        seq = ib002_random_maxdata(random.randint(0, i//10 + 4))
        heap.size = len(seq)
        heap.array = seq
        old_seq = list(seq)
        sort_seq = list(seq)
        sort_seq.sort()
        fixLSHeap(heap)
        sort_stud = list(heap.array)
        sort_stud.sort()
        if sort_stud != sort_seq:
            error_count += 1
            print("FAIL, halda {} se zmenila na {}, "
                  "ktera neobsahuje stejne prvky"
                  "".format(old_seq, heap.array))
        elif len(old_seq) != heap.size:
            error_count += 1
            print("FAIL, zmenilo se .size v zadane halde {} z {} na {}"
                  "".format(old_seq, len(old_seq), heap.size))
        elif not ib002_is_mh(heap):
            error_count += 1
            print("FAIL, halda {} se zmenila na {}, "
                  "coz neni maximova halda"
                  "".format(old_seq, heap.array))
        elif not isLSHeap(heap):
            error_count += 1
            print("FAIL, halda {} se zmenila na {}, "
                  "coz neni dle Vaseho testu LS halda"
                  "".format(old_seq, heap.array))
    if error_count == 0:
        print("fixLSHeap OK")


# Hlavni funkce volana automaticky po spusteni programu.
# Pokud chcete krome dodanych testu spustit vlastni testy, dopiste je sem.
# Odevzdavejte reseni s puvodni verzi teto funkce.

if __name__ == '__main__':
    ib002_test_heap2Tree()
    ib002_test_isLSHeap()
    ib002_test_minsOfSubtrees()
    ib002_test_fixLSHeap()