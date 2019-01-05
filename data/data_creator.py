import os
import numpy as np

# Зададим пределы температуры и давления
min_T, max_T = 0.1, 0.3
min_p, max_p = 1, 5 # Логарифмический масштаб

# Зададим шаг разбивки по температуре и по давлению
step_T = 0.2
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
    #os.system('lmp_serial < in.lennardjonesfluid')
    
    for p in range_log(min_p,max_p,2):
        os.system('lmp_serial < in.lennardjonescrystal -var pressure {:.1f}'.format(p))
        for T in np.arange(min_T,max_T,step_T):
                os.system('lmp_serial < in.restart -var temperature {:.1f} -var pressure {:.1f}'.format(T,p))

if __name__ == '__main__':
    main()
