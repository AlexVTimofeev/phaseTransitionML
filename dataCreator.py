import os
import numpy as np

import parametrs

# Зададим пределы температуры и давления
min_T, max_T = .05, 2.
min_p, max_p = 0.001, 1 # Логарифмический масштаб

# Зададим шаг разбивки по температуре и по давлению
step_T = 0.1
step_p = 2 # Логарифмический масштаб

def range_log(start = 10**-5,finish = 100,step=10):
    """
    Generator object
    Works as range, but instead of add uses multiplies
    """
    now = start
    while now < finish:
        yield now
        now *= step


def main():
# Сохраняет не туда, куда надо
    for p in range_log(min_p,max_p,2):
        os.system('lmp_serial < {}in.lennardjonescrystal -var pressure {:.5f}'.format(parametrs.unprocessedDataPath,p))
        for T in np.arange(min_T,max_T,step_T):
                os.system('lmp_serial < {}in.restart -var temperature {:.5f} -var pressure {:.5f}'.format(parametrs.unprocessedDataPath,T,p))

if __name__ == '__main__':
    main()