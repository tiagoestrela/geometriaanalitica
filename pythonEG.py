#Importação das bibliotecas
import numpy as np
import sys
#ler o número de variáveis
n=int(input("Entre com o número de variáveis"))
#fazendo um array de tamanho nxn+1 inicializando
# a matriz nula para armazenar a matriz aumentada.
a=np.zeros((n,n+1))
#fazendo um array de tamanho n para armazenar a solução
x=np.zeros(n)
#Ler  os coeficientes da matriz aumentada
print ("Entre com os coeficientes da matriz aumentada:")
for i in range(n):
                for j in range(n+1):
                                a[i][j]=input("a[" +str(i)+"]["+str(j)+"]")
#Aplicar a eliminação
for i in range(n):
                if a[i][i]==0.0:
                                sys.exit("Dividiu por zero")
                else:
                                for j in range(i+1,n):
                                                razão=a[j][i]/a[i][i]
                                                for k in range (n+1):

                                                                a[j][k]=a[j][k]-razão*a[i][k]
#Retrosubstituição
x[n-1]=a[n-1][n]/a[n-1][n-1]
#para n=3 o x[2] é o nosso z
# temos que voltar para achar o y
# e o x
for i in range(n-2,-1,-1):
                x[i]=a[i][n]
                for j in range(i+1,n):
                                x[i]=x[i]-a[i][j]*x[j]
                                
                x[i]=x[i]/a[i][i]
#exibir solução
                print("\n solução desejada ")
                for i in range(n):
                                print("X%d=%0.2f "%(i,x[i]), "end=\t")










                                                
