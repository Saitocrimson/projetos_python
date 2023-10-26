import numpy as np

def menu():
    print("1-Array simples\n2-Array em Tupla\n3-Array em Matriz\n4-Função ndim e ndmin\n5-Operações de Array\n6-Sair")
    
def escolha(n):
    if n==1:
        arr = np.array([1, 2, 3, 4, 5])
        print(arr)
        return 0
    elif n==2:
        arr2 = np.array((1, 2, 3, 4, 5))
        print(arr2)
        return 0
    elif n==3:
        arr3 = np.array([[1, 2, 3,4], [5, 6, 7,8]])
        print(arr3)
        print("Para achar algum numero e so escrever matriz[linha,coluna], ex:arr[1,0]->", arr3[1,0])
        return 0
    elif n==4:
        a = np.array(42)
        b = np.array([1, 2, 3, 4, 5])
        c = np.array([[1, 2, 3], [4, 5, 6]])
        d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
        print('numeros de dimensões, usa a função ndim, ex array.ndim : ')
        print(a,"->",a.ndim,"\n")
        print(b,"->",b.ndim,"\n")
        print(c,"->",c.ndim,"\n")
        print(d,"->",d.ndim,"\n")
        print('cria o números de dimensões, usa a função ndmin no final da função np.array como parametro: ')
        print("ex:exemplo=np.array([1, 2,3,4], ndmin=7 ")
        arr4 = np.array([1, 2, 3, 4], ndmin=7)
        print(arr4)
        return 0
    elif n==5:
        print("Para separar uma parte do array ->array[inicia a parte que quer cortar, final da parte]")
        arr = np.array([1, 2, 3, 4, 5])
        print(arr)
        print("ex:array[2:3]")
        print(arr[2:3])
        print("ex:array[1:2:3]")
        print(arr[1:2:3])
        print("final->array[-1]")
        print(arr[-1])
        print("pega uma parte e continua, ex:array[2:]")
        print(arr[2:])
        print("pega uma parte e termina, ex:array[:2]")
        print(arr[:2])
        arr2 = np.array(['apple', 'banana', 'cherry'])
        print("Usa o dtype para saber o tipo:", arr2.dtype, arr.dtype)
        print("Conversão->arr.astype('i' ou 'S' ou 'f' ou 'u' ou 'U')")
        arr = np.array([1.1, 2.1, 3.1])
        print(arr)
        newarr = arr.astype('i')
        print(newarr)
        print("FLOAT->INT",newarr.dtype)
        newarr = arr.astype(bool)
        print(newarr)
        print("FLOAT->BOLLEAN",newarr.dtype)
        return 0
    elif n==6:
        return 1
    
    else:
        print("escolha algo viavel")
        return 0

        
while True:
    menu()
    n=int(input("Digite a opção;"))
    print("\n\n")
    if escolha(n)==1:
        break
    print("\n\n")
        
   





