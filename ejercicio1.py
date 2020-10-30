import multiprocessing
import os

from math import sqrt

root_sum = 0
result = []


def root_list(number_list):
    global root_sum, result
    for idx, num in enumerate(number_list):
        result.append(sqrt(num))
        root_sum += result[idx]

    print('Result {}'.format(result[:]))
    print('Sum {}'.format(root_sum))


if __name__ == '__main__':
    mylist = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print('ID process runnig main: {}'.format(os.getpid()))

    p1 = multiprocessing.Process(target=root_list, args=(mylist,))

    p1.start()
    print('ID of process p1: {}'.format(p1.pid))
    print()
    root_list(mylist)
    print('Process p1 is alive {} antes del join '.format(p1.is_alive()))
    p1.join()

    print('Process p1 is alive {} después del join '.format(p1.is_alive()))
