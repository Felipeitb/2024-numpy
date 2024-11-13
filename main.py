import numpy as np #abreviar numpy, array = lista dove non ci fanno distinzioni

a1 = np.array([1,2,3])#nao esquecer das parenteses quadradas. ARRAY MINIMAMENTE ESPAZIADO
print("a1",a1)

a2 = np.linspace(0,100,21)#lista de 0 a 100 com espacos de 5
print("a2",a2)

a3 = np.zeros(10)#lista com 10 zeri
print("a3",a3)

a4 = np.ones(40)#lista mesma coisa array com 40 ums
print("a4",a4)

r1 = np.random.rand(2,3)#Np è la nostra libreria, il verde siamo al interno della libreria, random siamo dentro alla libreria, que dentro random tem a funcao( funcao è quando botamos entre parenteses) RAND 
print("r1",r1)#rand cria uma lista do corpo de uma matriz baseada em linhas e colunas, r1 tem 2 colunas e 3 linhas
#tra 0 e 15, faccio *15

#OU
#igual aquela do professor, è tipo minecraft quando vc coloca a seed pra entrar no mundo
np.random.seed(1)
r1 = np.random.rand(2,3)
print("r1",r1)

#OUTRA COISA

r2 = r1.reshape(3,2)
print("r2",r2)