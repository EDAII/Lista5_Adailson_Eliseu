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

def comparation_graph(results,n):
    plt.ylabel('Tempo para %d nós (em milisegundos)' % (n))
    
    for key in results.keys():
        plt.bar(key, results[key])

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
    random.shuffle(values)
    print(values)
    return values

results = {'RB': [], 'AVL': []}
result = {'RB': 0, 'AVL': []}
start = 0
while(number):
    print("Escolha uma das opções:\n1- Inserir valores randômicos para n nós.\n0- Para sair\n")
    number = int(input())
    if number == 1:
        print("Digite a quantidade de nós:")
        n = int(input())
        values = get_values(n)
        for key in result.keys():
            if key == 'AVL':
                start = time.time()
                avl = AVL_Tree()
                root = None
                for value in values:
                    root = avl.insert(root, value)

            elif key == 'RBT':
                start = time.time()
                for value in values:
                    rbt.add(value)
            
            end = time.time()
            diff = float(end - start)
            diff = diff * 1000
            
            result[key] = diff
            results[key].append(diff)

        root = rbt.root
        print('O tempo de inseção de %d nós foi de %f segundos ' % (n, diff))
        for key in result.keys():
            results[key].append(diff)
            if key == 'RBT':
                print_tree(root)
        comparation_graph(results, n)

    print("Aperte enter para continuar!")
    input()
    os.system('clear')