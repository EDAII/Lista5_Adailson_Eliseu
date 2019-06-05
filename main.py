from red_black_tree.rbt import RedBlackTree
import os, random, time
number = 1
values = []
n=0
try:
    tree = RedBlackTree()
except:
    print('Exception occurred')

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

while(number):
    print("Escolha uma das opções:\n1- Inserir valores randômicos para n nós.\n0- Para sair\n")
    number = int(input())
    if number == 1:
        print("Digite a quantidade de nós:")
        n = int(input())
        values = get_values(n)
        start = time.time()
        for value in values:
            tree.add(value)
        end = time.time()
        diff = end - start
        root = tree.root
        print('O tempo de inseção de %d nós foi de %f segundos ' % (n, diff))
        print_tree(root)

    print("Aperte enter para continuar!!!")
    try:
        input()
    except:
        print("Você está no python2 por favor aperte enter de novo")
        raw_input()
    os.system('clear')
