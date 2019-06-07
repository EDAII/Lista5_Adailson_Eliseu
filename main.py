from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from red_black_tree.rbt import RedBlackTree
from avl_tree.avl import AVL_Tree
import os, random, time

number = 1
values = []
n=0
try:
    rbt = RedBlackTree()
except:
    print('Exception occurred')

def comparation_graph(results_insert,n):
    plt.ylabel('Tempo para %d nós (em milisegundos)' % (n))
    
    for key in results_insert.keys():
        plt.bar(key, results_insert[key])

    plt.show()

def print_tree(node):
    if node.value == None :
        return
    print_tree(node.right)
    print(node)
    print_tree(node.left)

def get_values(n):
    i=0
    values = []
    for i in range(0,n*2,2):
        values.append(i)
    # print(values)
    return values

results_insert = {'RB': [], 'AVL': []}
result_insert = {'RB': 0, 'AVL': 0}
results_search = {'RB': [], 'AVL': []}
result_search = {'RB': 0, 'AVL': 0}

while(number):
    start = 0
    end = 0
    value = 0
    values.clear
    value_sought = 0
    diff = 0
    print("Escolha uma das opções:\n1- Comparativo inserção (insere valores randômicos para n nós)\n2- Comparativo de busca (busca valor randômico em valores para n nós) \n0- Para sair\n")
    number = int(input())
    if number == 1 or number == 2:
        print("Digite a quantidade de nós:")
        n = int(input())
        values = get_values(n)
        if number == 1:
            for key in result_insert.keys():
                if key == 'AVL': 
                    avl = AVL_Tree()
                    root = None
                    start = time.time()
                    for value in values:
                        root = avl.insert(root, value)

                elif key == 'RB':
                    start = time.time()
                    for value in values:
                        rbt.add(value)
                    root = rbt.root
                
                end = time.time()
                diff = float(end - start)
                diff = diff * 1000
                
                result_insert[key] = diff
                results_insert[key].append(diff)
            
            comparation_graph(results_insert, n)
        else:
            for key in result_insert.keys():
                if key == 'AVL':
                    avl = AVL_Tree()
                    root = None
                    for value in values:
                        root = avl.insert(root, value)                    
                    value_sought = random.choice(values)
                    start = time.time()
                    avl.find_node(root, value_sought)

                elif key == 'RB':
                    for value in values:
                        rbt.add(value)                    
                    value_sought = random.choice(values)
                    start = time.time()
                    rbt.find_node(value_sought)

                end = time.time()
                diff = float(end - start)
                diff = diff * 1000
                
                result_search[key] = diff
                results_search[key].append(diff)

            root = rbt.root
            comparation_graph(results_search, n)

    print("Aperte enter para continuar!")
    input()
    os.system('clear')