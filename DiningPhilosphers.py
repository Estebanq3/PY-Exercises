#Codigo adaptado de: Dining-Philosphers Solution using Semaphore. Recuperado de: cppsecrets.com
#https://cppsecrets.com/users/120612197115104981111171149751485164103109971051084699111109/Python-Implementation-of-Dining-Philosphers-Solution-using-Semaphore.php
import threading
import random
import time

class Filosofo(threading.Thread):
    running = True  #Informa si todo el mundo ya ha terminado de comer
    #------------------------------------------------------------------------------
    def __init__(self, indice, tenedor_izquierdo, tenedor_derecho):
        threading.Thread.__init__(self)
        self.indice = indice
        self.tenedor_izquierdo = tenedor_izquierdo
        self.tenedor_derecho = tenedor_derecho
    #------------------------------------------------------------------------------
    def run(self):
        while(self.running):
            #Filosofo durmiendo, posterior despierta y solicita comer
            tiempo_sin_comer = random.randint(15,30)
            time.sleep(tiempo_sin_comer)
            print ('[Solicitud] Filosofo %s solicita comidita.' % (self.indice+1))
            self.comer()
    #------------------------------------------------------------------------------
    def comer(self):
        #Si ambos semaforos, que son los tenedores, estan libres, entonces el filosofo comenzara a comer
        primer_tenedor, segundo_tenedor = self.tenedor_izquierdo, self.tenedor_derecho
        while self.running:
            primer_tenedor.acquire()
            locked = segundo_tenedor.acquire(False) 
            if locked: break
            primer_tenedor.release()
            print ('[RecursoLiberado] Filosofo %s suelta tenedor por no disponibilidad de ambos tenedores.' % (self.indice+1))
            primer_tenedor, segundo_tenedor = segundo_tenedor, primer_tenedor
        else:
            return
        
        self.comiendo()
        #Se liberan ambos tenedores luego de terminar de comer
        segundo_tenedor.release()
        primer_tenedor.release()
    #------------------------------------------------------------------------------
    def comiendo(self):			
        #Comienza a comer, dura ciertos segundos, entre 5 y 30, y deja de comer
        print ('    [Accion] Filosofo %s comienza a comer. '% (self.indice+1))
        tiempo_comiendo = random.randint(5,30)
        time.sleep(tiempo_comiendo)
        print ('    [Accion] Filosofo %s termina de comer, libera tenedores y se va a pensar.' % (self.indice+1))

def main():
    tenedores = [threading.Semaphore() for n in range(5)] #inicializando array de semaforos
    filosofos = [Filosofo(i, tenedores[i%5], tenedores[(i+1)%5])
            for i in range(5)]

    Filosofo.running = True
    for p in filosofos: p.start()
    time.sleep(50)

 
if __name__ == "__main__":
    main()