# Repetimos el mismo ejercicio que en el caso anterior pero ahora lo que queremos es trabajar con memoria compartida.
# Aparte del proceso principal main, ahora queremos crear dos procesos y que ellos trabajen los dos sobre
# la misma función que calcula las raíces cuadradas de los elementos de la lista.
# Mostrar para cada proceso nuevo creado, su pid y no esperar a hacer el join
# para ver el orden en el que se ejecutan.
# Mostrar también el resultado del valor de la lista y
# la suma de sus elementos para cada uno de los procesos ejecutados.

import multiprocessing
import os

from math import sqrt

root_sum = 0
result = []


def root_list(number_list,result,root_sum):

    for idx, num in enumerate(number_list):
        result[idx]=sqrt(num)
    root_sum.value = sum(result)
    print('process id:', os.getpid())
    print('Result {}'.format(result[:]))
    print('Sum {}'.format(root_sum.value))


if __name__ == '__main__':
    mylist = [2,4, 9, 16, 25, 36, 49, 64, 81, 100]

    result = multiprocessing.Array('f', len(mylist))

    root_sum = multiprocessing.Value('f')
    p2 = multiprocessing.Process(target=root_list, args=(mylist, result, root_sum,))
    p1 = multiprocessing.Process(target=root_list, args=(mylist, result, root_sum,))

    print('ID process runnig main: {}'.format(os.getpid()))


    p1.start()
    p2.start()
    print('ID of process p1: {}'.format(p1.pid))
    print('ID of process p2: {}'.format(p2.pid))

    root_list(mylist, result, root_sum)

    print('Process p1 is alive {} antes del join '.format(p1.is_alive()))
    print('Process p2 is alive {} antes del join '.format(p2.is_alive()))
  #  p1.join()
  #  p2.join()
  #  print('Process p1 is alive {} después del join '.format(p1.is_alive()))
  #  print('Process p2 is alive {} después del join '.format(p2.is_alive()))