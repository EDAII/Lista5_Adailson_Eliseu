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
    return values

results_insert = {'RB': [], 'AVL': []}
result_insert = {'RB': 0, 'AVL': 0}
results_search = {'RB': [], 'AVL': []}
result_search = {'RB': 0, 'AVL': 0}
results_remove = {'RB': [], 'AVL': []}
result_remove = {'RB': 0, 'AVL': 0}

while(number):
    start = 0
    end = 0
    value = 0
    values.clear
    value_sought = 0
    diff = 0
    i = 0
    print("Escolha uma das opções:\n"
        +"1- Comparativo inserção AVL x Red-Black (insere valores randômicos para n nós)\n"
        +"2- Comparativo de busca (busca valor randômico em valores para n nós)\n"
        +"3- Comparativo de remoção\n"
        +"0- Para sair\n")
    number = int(input())
    if number == 1 or number == 2 or number == 3:
        print("Digite a quantidade de nós:")
        n = int(input())
        values = get_values(n)
        if number == 1:
            print("Digite quantas iterações você deseja inserir para %d nós:" % n)
            b = int(input())
        elif number == 2:
            print("Digite quantas iterações você deseja buscar para %d nós:" % n)
            b = int(input())
        else:
            print("Digite quantas iterações você deseja remover para %d nós:" % n)
            b = int(input())
        # if number == 1 or number == 3:
        for key in result_insert.keys():
            if key == 'AVL': 
                avl = AVL_Tree()
                root = None
                if number == 1:
                    start = time.time()
                    for i in range(0,b):
                        for value in values:
                            root = avl.insert(root, value)
                elif number == 2:
                    for value in values:
                        root = avl.insert(root, value)                    
                    value_sought = random.choice(values)
                    start = time.time()
                    for i in range(0,b):
                        avl.find_node(root, value_sought)    
                else:
                    for value in values:
                        root = avl.insert(root, value)
                    start = time.time()
                    for i in range(0,b):
                        for value in values:
                            root = avl.delete(root, value)

            elif key == 'RB':
                if number == 1:
                    start = time.time()
                    for i in range(0,b):
                        for value in values:
                            rbt.add(value)
                    root = rbt.root
                elif number == 2:
                    for value in values:
                        rbt.add(value)                    
                    value_sought = random.choice(values)
                    start = time.time()
                    for i in range(0,b):
                        rbt.find_node(value_sought)
                else:
                    start = time.time()
                    for value in values:
                        rbt.add(value)
                    root = rbt.root
                    for i in range(0,b):
                        for value in values:
                            rbt.remove(value)

            end = time.time()
            diff = float(end - start)
            diff = diff * 1000
            
            if number == 1:
                result_insert[key] = diff
                results_insert[key].append(diff)
            elif number == 2:
                result_search[key] = diff
                results_search[key].append(diff)
            else:
                result_remove[key] = diff
                results_remove[key].append(diff)

        if number == 1:
            comparation_graph(results_insert, n)
        elif number == 2:
            comparation_graph(results_search, n)    
        else:
            comparation_graph(results_remove, n) 

    print("Aperte enter para continuar!")
    input()
    os.system('clear')