# (1) carregamento das bibiotecas
import numpy as np
import matplotlib.pyplot as plt




# (2)entrada de dados
dados =[2,3,4,5,5,5,5,6,7,8,
        8,8,9,10,10,12,12,14,14,14,
        16,20,23,25,28,30,32,35,38]




#(3) processamentos de dados
tamanho = len (dados) #calculo o tamanhi dos dados )



#deter
k = 1+ 3.32 * np.log10(tamanho)   #aplica a formula de sturges
k_final = np.round(k )


#calculo do tamanho de cada classe
t = max(dados) - min (dados)    #acha a variaçao dos dados
x = t/k_final                   #acha o tamanho final das classes



#costrucao da abella de distribuiçao
tabela = np.histogram(dados,bins=int(k_final))


#(40 apresentaçao de resultados
print("quantidade de amostras:",tamanho)
print("Numero de classes k = ", k)
print("Numero final de classes:", k_final)
print("tamanho das classes:",x)

print(tabela)

plt.hist(dados, bins=int(k_final))
plt.title("Histograma dos tempos de banho")
plt.ylabel("Qtd de pessoas")
plt.xlabel("classe de tempo de banho")
plt.show()