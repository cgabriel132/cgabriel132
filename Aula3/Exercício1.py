import time

data = time.localtime()
data_atual = time.strftime("%d/%m/%Y, %H:%M:%S", data)

print("Today is " + data_atual)

def sqrt():

    t = time.localtime()
    inicio = time.mktime(t)

    print(inicio)

    for n in range(0,50000001):
        n**(1/2)
        #print("Raízes :" + str(n**(1/2)))

    d = time.localtime()
    fim = time.mktime(d)

    print(fim)

    print("Tempo para calcular: " + str(fim-inicio))

sqrt()
