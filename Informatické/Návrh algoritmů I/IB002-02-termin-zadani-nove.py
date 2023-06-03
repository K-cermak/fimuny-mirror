#!/usr/bin/python3
from collections import deque
from operator import eq
from math import log
import random
import ast

# Zadani: V tomto prikladu budeme pracovat s orientovanymi grafy bez ohodnoceni
# hran.

# Doporuceni: Pokud si behem pruchodu grafem potrebujete pamatovat nejakou
# informaci pro kazdy vrchol, muzete s vyhodou vyuzit pole 'tmp' nachystane v
# tride Graph - tedy pro graf g pouzivejte pole g.tmp. (Vsimnete si, ze pole ma
# automaticky spravnou delku.)  NEZAPOMENTE si pred pouzitim pole smazat, treba
# pomoci pripravene funkce 'eraseTmp(g)'.


class Graph:

    """Trida reprezentujici orientovany graf bez ohodnoceni hran. Graf je
reprezentovan matici sousednosti. Vrcholy grafu odpovidaji cislum 0, 1, ...,
size-1. Orientovana hrana (u,v) je v grafu prave tehdy, kdyz matrix[u][v] je
rovno 1 (v opacnem pripade matrix[u][v] == 0). Graf nemusi byt souvisly!

    Atributy:
        size    pocet vrcholu v grafu
        matrix  matice sousednosti
        tmp     pomocne pole, s jednim prvkem pro kazdy vrchol
    """

    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for i in range(size)]
        self.tmp = [None] * size


def eraseTmp(g):
    """Smaze pomocne pole (tj. nastavi vsechny polozky na None)."""
    g.tmp = [None] * g.size


# Ukol 1. (10 bodu)

# Implementujte funkci twoPath(g), ktera pro zadany vstupni graf 'g' vrati
# graf 'h' takovy, ze:
#
# 1) 'h' ma stejny pocet vrcholu jako 'g', a
# 2) v grafu 'h' existuje orientovana hrana (u,v) prave tehdy, kdyz v grafu 'g'
#    existuje orientovana cesta z 'u' do 'v' delky 2. (V neohodnocenem grafu je
#    delka cesty rovna poctu hran.)
#
# POZOR: Tato cesta nemusi byt jednoducha!

def twoPath(g):
    """
    vstup: 'g' orientovany neohodnoceny graf typu Graph
    vystup: 'h' orientovany graf typu Graph splnujici zadani ukolu
    casova slozitost: O(n^3), kde 'n' je pocet vrcholu grafu 'g'
    """
    return None  # TODO


# Ukol 2. (10 bodu)

# Implementujte funkci sumReachable(g, v), ktera spocita soucet cisel vsech
# vrcholu 'w' takovych, ze v grafu 'g' vede orientovana cesta (libovolne delky)
# z 'v' do 'w'.
#
# Priklad: V nasledujicim grafu vrati sumReachable(g, 4) hodnotu 12 = 4 + 3 + 5
# a sumReachable(g, 0) hodnotu 11 = 0 + 1 + 2 + 3 + 5.
#
# 0 ---> 1 ---> 2 ---> 3 <--- 4 ---> 5
#         \                          ^
#          -------------------------/
#

def sumReachable(g, v):
    """
    vstup: 'g' orientovany neohodnoceny graf typu Graph a jeho vrchol 'v'
    vystup: soucet cisel uzlu 'w' takovych, ze v 'g' existuje
            orientovana cesta z 'v' do 'w'
    casova slozitost: O(n^2), kde 'n' je pocet vrcholu grafu 'g'
    """
    return None  # TODO


# Ukol 3. (15 bodu)

# Implementujte funkci shortestPathsTree(g, v), ktera zkonstruuje strom
# nejkratsich cest z vrcholu 'v' v grafu 'g'.  Vystupem je strom typu Tree
# definovany nize.

# Priklad: Vpravo jsou dva z moznych stromu pro graf vlevo a vrchol 0.
#
#  0 ---> 1 ---> 6                      0                      0
#  |      |      ^                     / \                    / \
#  |      |      |                    2   1                  1   2
#  v      v      |                   /     \                / \
#  2 ---> 3 ---> 4 <--- 5           3       6              3   6
#                                  /                      /
#                                 4                      4

class Tree:

    """Trida Tree slouzi k reprezentaci stromu.

    Atributy:
        root    odkaz na korenovy uzel typu Node
    """

    def __init__(self, root=None):
        self.root = root


class Node:

    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key      klic daneho uzlu (cele cislo)
        children seznam potomku
    """

    def __init__(self, key):
        self.key = key
        self.children = []


def shortestPathsTree(g, v):
    """
    vstup: 'g' orientovany neohodnoceny graf typu Graph a jeho vrchol 'v'
    vystup: strom typu Tree, ktery je stromem nejkratsich cest z 'v'
    casova slozitost: O(n^2), kde 'n' je pocet vrcholu grafu 'g'
    """
    return None  # TODO


# Ukol 4. (15 bodu)

# Implementujte funkci topoSort(g), ktera pro dany vstupni orientovany
# acyklicky graf 'g' vrati topologicke usporadani vsech jeho vrcholu.
#
# Jinymi slovy, vystupem je seznam 'a' delky g.size obsahujici vsechny vrcholy
# grafu a splnujici nasledujici vlastnost pro kazdou orientovanou hranu (u,v):
#
# - necht i je index takovy, ze a[i] = u
# - necht j je index takovy, ze a[j] = v
# - pak i <= j
#
# (hrany tedy mohou vest jen 'zleva doprava')
#
# Priklad:
#
#  0 ---> 1 ---> 6
#  |      |      ^
#  |      |      |
#  v      v      |
#  2 ---> 3 ---> 4 ---> 5
#
# Korektnim vystupem je treba posloupnost [0,1,2,3,4,5,6].  (Dalsi mozne
# korektni vystupy jsou napr. [0,2,1,3,4,6,5] nebo [0,1,2,3,4,6,5]).
#
# Napoveda: Pokud spustite DFS z libovolneho vrcholu, a ukladate si vrcholy
# podle casu jejich ukonceni, vysledna posloupnost bude po obraceni topologicky
# usporadana. Nicmene nemusi obsahovat vsechny vrcholy grafu.


def topoSort(g):
    """
    vstup: 'g' orientovany neohodnoceny acyklicky graf typu Graph
    vystup: topologicky usporadany seznam vrcholu grafu 'g'
    casova slozitost: O(n^2), kde 'n' je pocet vrcholu grafu 'g'
    """
    return []  # TODO


"""
Soubory .dot z testu vykreslite napr. na http://www.webgraphviz.com/.
"""

########################################################################
#               Nasleduje kod testu, NEMODIFIKUJTE JEJ                 #
########################################################################


def makeTree(tree, fileName):
    """
    Zde mate k dispozici funkci `makeTree`, ktera vam z `tree` na vstupu
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

    def checkChild(node, child):
        if child is None:
            makeNode("{}{}".format(id(node)), "Nil\", color=\"white")
            makeEdge(id(node), "{}{}".format(id(node)))
        else:
            makeEdge(id(node), id(child))
            makeGraphviz(child, f)

    def makeGraphviz(node, f):
        if node is None:
            return
        makeNode(id(node), node.key)
        for child in node.children:
            checkChild(node, child)

    with open(fileName, 'w') as f:
        f.write("digraph Tree {\n")
        f.write("node [color=lightblue2, style=filled, ordering=\"out\"];\n")
        if (tree is not None) and (tree.root is not None):
            makeGraphviz(tree.root, f)
        f.write("}\n")


def makeGraph(graph, fileName):
    """
    Zde mate k dispozici funkci `makeGraph`, ktera vam z `graph` na vstupu
    vygeneruje do souboru `fileName` reprezentaci grafu pro graphviz.
    Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
    coz se hodi predevsim pro ladeni.
    Pro zobrazeni graphvizu muzete vyuzit:
    http://www.webgraphviz.com/
    """

    def makeGraphviz(matrix, f):
        n = len(matrix)
        for i in range(n):
            f.write("{} [label=\"{}\"]\n".format(i, i))
            for j in range(n):
                if matrix[i][j] == 1:
                    f.write("{} -> {}\n".format(i, j))

    with open(fileName, 'w') as f:
        f.write("digraph {\n")
        f.write("node [color=lightblue2, style=filled, ordering=\"out\"];\n")
        makeGraphviz(graph.matrix, f)
        f.write("}\n")


# empty
g00 = (0, [])
# a vertex
g01 = (1, [])
# 2 vertices
g02 = (2, [])
# an edge
g03 = (2, [(0, 1)])
# C1
g04 = (1, [(0, 0)])
# a bidirectional edge, C2
g05 = (2, [(0, 1), (1, 0)])
# C3
g06 = (3, [(0, 1), (1, 2), (2, 0)])
# bidirectional C3
g07 = (3, [(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)])
# C4
g08 = (4, [(0, 1), (1, 2), (2, 3), (3, 0)])
# C7
g09 = (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0)])
# C4+C3
g10 = (7, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 4)])
# two cycles reachable from a single source
g11 = (8, [(0, 1), (1, 2), (2, 3), (3, 0),
       (4, 5), (5, 6), (6, 4), (7, 3), (7, 6)])
# small tree
g12 = (3, [(0, 1), (0, 2)])
# reverse small tree
g13 = (3, [(1, 0), (2, 0)])
# bigger tree
g14 = (7, [(0, 0), (0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])
# 3-part forest
g15 = (6, [(0, 1), (2, 3), (2, 4)])
# P6
g16 = (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
# bidirectional P4
g17 = (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 3), (3, 2), (2, 1), (1, 0)])
# isolated vertex + isolated loop
g18 = (2, [(1, 1)])


test_sources = [g00, g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11,
                g12, g13, g14, g15, g16, g17, g18]
tests = []
dag_sources = [g00, g01, g02, g03, g12, g13, g14, g15, g16]
dags = []


def ib002_build_test_set():
    global tests
    num = len(test_sources)
    tests = [None] * num
    for i in range(num):
        (n, edges) = test_sources[i]
        g = Graph(n)
        for (u, v) in edges:
            g.matrix[u][v] = 1
        tests[i] = g
    global dags
    num = len(dag_sources)
    dags = [None] * num
    for i in range(num):
        (n, edges) = dag_sources[i]
        g = Graph(n)
        for (u, v) in edges:
            g.matrix[u][v] = 1
        dags[i] = g


def ib002_gen_dag(n):
    g = Graph(n)
    num = int(log(n, 2))
    for i in range(n):
        for x in range(num):
            j = random.randint(i + 1, 2 * n)
            if j < n:
                g.matrix[i][j] = 1
    return g


def ib002_gen_rooted_dag(n):
    def no_ancestors(v):
        for u in range(g.size):
            if g.matrix[u][v] == 1:
                return False
        return True
    g = Graph(n)
    num = int(log(n, 2))
    for i in range(1, n):
        for x in range(num):
            j = random.randint(i + 1, 2 * n)
            if j < n:
                g.matrix[i][j] = 1
    for j in range(1, n):
        if no_ancestors(j):
            g.matrix[0][j] = 1
    return g


def ib002_permute_graph(g):
    n = g.size
    h = Graph(n)
    p = list(range(n))
    random.shuffle(p)
    for u in range(n):
        for v in range(n):
            h.matrix[p[u]][p[v]] = g.matrix[u][v]
    return h


def ib002_test_twoPath():
    print("\n**twoPath testing")
    error_count = 0
    for line in TP_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        num, matrix = line.rstrip().split(' ; ')
        g = tests[int(num)]
        g_copy = Graph(g.size)
        g_copy.matrix = [list(g.matrix[i]) for i in range(g.size)]
        hY = twoPath(g)
        if g_copy.size != g.size or g_copy.matrix != g.matrix:
            error_count += 1
            print("FAIL, zmenili jste graf zadany na vstupu!")
        hC = Graph(g.size)
        hC.matrix = ast.literal_eval(matrix)
        if hY is None:
            error_count += 1
            fI = "Er_twoPath_" + str(error_count) + "input.dot"
            fC = "Er_twoPath_" + str(error_count) + "corr.dot"
            makeGraph(g, fI)
            makeGraph(hC, fC)
            print("FAIL, pro graf v souboru {} melo vratit graf v souboru {}, "
                  "ale vratilo None"
                  "".format(fI, fC))
        elif hC.matrix != hY.matrix:
            error_count += 1
            fI = "Er_twoPath_" + str(error_count) + "input.dot"
            fC = "Er_twoPath_" + str(error_count) + "corr.dot"
            fY = "Er_twoPath_" + str(error_count) + "your.dot"
            makeGraph(g, fI)
            makeGraph(hC, fC)
            makeGraph(hY, fY)
            print("FAIL, pro graf v souboru {} melo vratit graf v souboru {}, "
                  "ale vratilo graf v souboru {}"
                  "".format(fI, fC, fY))
    if error_count == 0:
        print("twoPath OK")


TP_data = """0 ; []
1 ; [[0]]
2 ; [[0, 0], [0, 0]]
3 ; [[0, 0], [0, 0]]
4 ; [[1]]
5 ; [[1, 0], [0, 1]]
6 ; [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
7 ; [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
8 ; [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
9 ; [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0],\
[0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0],\
[0, 1, 0, 0, 0, 0, 0]]
10 ; [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0],\
[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0],\
[0, 0, 0, 0, 0, 1, 0]]
11 ; [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],\
[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0],\
[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0]]
12 ; [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
13 ; [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
14 ; [[1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0, 0]]
15 ; [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
16 ; [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0],\
[0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0, 0]]
17 ; [[1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0],\
[0, 0, 1, 0, 1]]
18 ; [[0, 0], [0, 1]]"""


def ib002_test_sumReachable():
    print("\n**sumReachable testing")
    error_count = 0
    for line in SR_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        num, start, vsum = line.rstrip().split(' ; ')
        g = tests[int(num)]
        sY = sumReachable(g, int(start))
        sC = int(vsum)
        if sC != sY:
            error_count += 1
            fI = "Er_sumReachable_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} a vrchol {} vracen vysledek {}, "
                  "ale spravne je {}"
                  "".format(fI, int(start), sY, sC))
    if error_count == 0:
        print("sumReachable OK")


SR_data = """1 ; 0 ; 0
2 ; 0 ; 0
3 ; 0 ; 1
4 ; 0 ; 0
5 ; 0 ; 1
6 ; 0 ; 3
7 ; 0 ; 3
8 ; 0 ; 6
9 ; 0 ; 21
10 ; 0 ; 6
11 ; 0 ; 6
12 ; 0 ; 3
13 ; 0 ; 0
14 ; 0 ; 21
15 ; 0 ; 1
16 ; 0 ; 21
17 ; 0 ; 10
18 ; 1 ; 1"""


def ib002_tree_by_level(node, array, level):
    array[node.key] = level
    for c in node.children:
        ib002_tree_by_level(c, array, level + 1)


def ib002_test_spTree():
    print("\n**shortestPathsTree testing")
    error_count = 0
    for line in SP_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        num, dist = line.rstrip().split(' ; ')
        g = tests[int(num)]
        t = shortestPathsTree(g, 0)
        if t is None:
            error_count += 1
            fI = "Er_shortestPath_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} bylo vraceno None"
                  "".format(fI))
        elif t.root is None:
            error_count += 1
            fI = "Er_shortestPath_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} byl vracen strom s korenem None"
                  "".format(fI))
        else:
            a = [-1] * g.size
            ib002_tree_by_level(t.root, a, 0)
            dY = [(i, x) for i, x in enumerate(a)]
            dY.sort()
            dC = ast.literal_eval(dist)
            if dY != dC:
                error_count += 1
                i = list(map(eq, dY, dC)).index(False)
                fI = "Er_shortestPath_" + str(error_count) + "input.dot"
                fT = "Er_shortestPath_" + str(error_count) + "tree.dot"
                makeGraph(g, fI)
                makeTree(t, fT)
                print("FAIL, pro graf v souboru {} by vrchol {} mel by ve "
                      "vzdalenosti {}, ale ve vracenem strome {} "
                      "ma vzdalenost {}"
                      "".format(fI, dC[i][1], i, fT, dY[i][1]))
    if error_count == 0:
        print("shortestPathsTree OK")


SP_data = """1 ; [(0, 0)]
2 ; [(0, 0), (1, -1)]
3 ; [(0, 0), (1, 1)]
4 ; [(0, 0)]
5 ; [(0, 0), (1, 1)]
6 ; [(0, 0), (1, 1), (2, 2)]
7 ; [(0, 0), (1, 1), (2, 1)]
8 ; [(0, 0), (1, 1), (2, 2), (3, 3)]
9 ; [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
10 ; [(0, 0), (1, 1), (2, 2), (3, 3), (4, -1), (5, -1), (6, -1)]
11 ; [(0, 0), (1, 1), (2, 2), (3, 3), (4, -1), (5, -1), (6, -1), (7, -1)]
12 ; [(0, 0), (1, 1), (2, 1)]
13 ; [(0, 0), (1, -1), (2, -1)]
14 ; [(0, 0), (1, 1), (2, 1), (3, 2), (4, 2), (5, 2), (6, 2)]
15 ; [(0, 0), (1, 1), (2, -1), (3, -1), (4, -1), (5, -1)]
16 ; [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
17 ; [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
18 ; [(0, 0), (1, -1)]"""


def ib002_test_topoSort():
    def test_edges():
        for u in range(n):
            for v in range(n):
                if g.matrix[u][v] == 1 and ind[u] > ind[v]:
                    return(u, v)
        return None
    # test propper
    print("\n**topoSort testing")
    error_count = 0
    # preddefinovane testy
    for g in dags:
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        n = g.size
        a = topoSort(g)
        if sorted(a) != list(range(n)):
            error_count += 1
            fI = "Er_topoSort_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} byl vracen seznam {}, "
                  "ktery neobsahuje vsechny vrcholy prave jednou."
                  "".format(fI, a))
            continue
        # test for toposort
        ind = [a.index(x) for x in range(n)]
        if test_edges() is not None:
            error_count += 1
            u, v = test_edges()
            fI = "Er_topoSort_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} byl vracen seznam {}, "
                  "kde hrana ({}, {}) porusuje usporadani."
                  "".format(fI, a, u, v))
    # generovane testy
    for n in range(2, 20):
        if error_count > 4:
            if n > 2:
                print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        g = ib002_permute_graph(ib002_gen_rooted_dag(n))
        a = topoSort(g)
        if sorted(a) != list(range(n)):
            error_count += 1
            fI = "Er_topoSort_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} byl vracen seznam {}, "
                  "ktery neobsahuje vsechny vrcholy prave jednou."
                  "".format(fI, a))
            continue
        # test for toposort
        ind = [a.index(x) for x in range(n)]
        if test_edges() is not None:
            error_count += 1
            u, v = test_edges()
            fI = "Er_topoSort_" + str(error_count) + "input.dot"
            makeGraph(g, fI)
            print("FAIL, pro graf v souboru {} byl vracen seznam {}, "
                  "kde hrana ({}, {}) porusuje usporadani."
                  "".format(fI, a, u, v))
    if error_count == 0:
        print("topoSort OK")


# Hlavni funkce volana automaticky po spusteni programu.
# Pokud chcete krome dodanych testu spustit vlastni testy, dopiste je sem.
# Odevzdavejte reseni s puvodni verzi teto funkce.

if __name__ == '__main__':
    ib002_build_test_set()
    ib002_test_twoPath()
    ib002_test_sumReachable()
    ib002_test_spTree()
    ib002_test_topoSort()
