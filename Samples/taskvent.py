import zmq
import random
import time

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print "Presione enter cuando los workers estan disponibles"

_=raw_input()

print "Enviando acciones a los clientes"

sink.send('0')

random.seed()

total_msc = 0

for task in range(100):
    work = random.randint(1,100)
    total_msc += work
    sender.send(str(work))

print "total de costo esperado %s ms" % total_msc

time.sleep(1)
