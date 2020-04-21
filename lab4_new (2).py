import numpy as np
import scipy.stats
from datetime import datetime
start_time = datetime.now()

def getSum(*args):
    summa = 0
    try:
        if args[0] == "y":
            if len(args) == 1:
                summa = sum(my_list)
            else:
                for j in range(N):
                    sum_i_temp = 1
                    for i in range(len(args) - 1):
                        sum_i_temp *= x_matrix[j][args[i + 1] - 1]
                    sum_i_temp *= my_list[j]
                    summa += sum_i_temp

        elif len(args) == 1:
            args = args[0] - 1
            for obj in x_matrix:
                summa += obj[args]
        else:
            for obj in x_matrix:
                sum_i_temp = 1
                for i in range(len(args)):
                    sum_i_temp *= obj[
                        args[i] - 1]
                summa += sum_i_temp

    except:
        print("def error")
    return summa


X1_MIN, X1_MAX = -30, 0  # начальные условия
X2_MIN, X2_MAX = 10, 60
X3_MIN, X3_MAX = 10, 35
m = 3
N = 8

mx_max = (X1_MAX + X2_MAX + X3_MAX) / 3
mx_min = (X1_MIN + X2_MIN + X3_MIN) / 3
Y_MAX = mx_max + 200
Y_MIN = mx_min + 200

y_list = np.random.randint(Y_MIN, Y_MAX, (N, m))

x_matrix = [
    [X1_MIN, X2_MIN, X3_MIN],
    [X1_MIN, X2_MIN, X3_MAX],
    [X1_MIN, X2_MAX, X3_MIN],
    [X1_MIN, X2_MAX, X3_MAX],
    [X1_MAX, X2_MIN, X3_MIN],
    [X1_MAX, X2_MIN, X3_MAX],
    [X1_MAX, X2_MAX, X3_MIN],
    [X1_MAX, X2_MAX, X3_MAX]
]

while 1:  # цикл на проверку однородности дисперсии
    def y_add_el():  # функция увеличения m
        for obj in y_list:
            obj.append(np.random.randint(y_min, y_max))


    my_list = []
    mx1 = 0
    mx2 = 0
    mx3 = 0

    for obj in y_list:  # создание списка my
        my_list.append(sum(obj) / len(obj))

    for obj in x_matrix:
        mx1 += obj[0]
        mx2 += obj[1]
        mx3 += obj[2]

    mx1 /= 8
    mx2 /= 8
    mx3 /= 8
    my = sum(my_list) / 8

    """Coefficients"""
    m0 = [N, getSum(1), getSum(2), getSum(3), getSum(1, 2), getSum(1, 3), getSum(2, 3), getSum(1, 2, 3)]
    m1 = [getSum(1), getSum(1, 1), getSum(1, 2), getSum(1, 3), getSum(1, 1, 2), getSum(1, 1, 3),
          getSum(1, 2, 3), getSum(1, 1, 2, 3)]
    m2 = [getSum(2), getSum(1, 2), getSum(2, 2), getSum(2, 3), getSum(1, 2, 2), getSum(1, 2, 3),
          getSum(2, 2, 3), getSum(1, 2, 2, 3)]
    m3 = [getSum(3), getSum(1, 3), getSum(2, 3), getSum(3, 3), getSum(1, 2, 3), getSum(1, 3, 3),
          getSum(2, 3, 3), getSum(1, 2, 3, 3)]
    m4 = [getSum(1, 2), getSum(1, 1, 2), getSum(1, 2, 2), getSum(1, 2, 3), getSum(1, 1, 2, 2),
          getSum(1, 1, 2, 3), getSum(1, 2, 2, 3), getSum(1, 1, 2, 2, 3)]
    m5 = [getSum(1, 3), getSum(1, 1, 3), getSum(1, 2, 3), getSum(1, 3, 3), getSum(1, 1, 2, 3),
          getSum(1, 1, 3, 3), getSum(1, 2, 3, 3), getSum(1, 1, 2, 3, 3)]
    m6 = [getSum(2, 3), getSum(1, 2, 3), getSum(2, 2, 3), getSum(2, 3, 3), getSum(1, 2, 2, 3),
          getSum(1, 2, 3, 3), getSum(2, 2, 3, 3), getSum(1, 2, 2, 3, 3)]
    m7 = [getSum(1, 2, 3), getSum(1, 1, 2, 3), getSum(1, 2, 2, 3), getSum(1, 2, 3, 3), getSum(1, 1, 2, 2, 3),
          getSum(1, 1, 2, 3, 3), getSum(1, 2, 2, 3, 3), getSum(1, 1, 2, 2, 3, 3)]

    k0, k1, k2, k3, k4, k5, k6, k7 = getSum("y"), getSum("y", 1), getSum("y", 2), getSum("y", 3), \
                                     getSum("y", 1, 2), getSum("y", 1, 3), getSum("y", 2, 3), getSum("y", 1, 2, 3)
    denominator = np.linalg.det([
        m0,
        m1,
        m2,
        m3,
        m4,
        m5,
        m6,
        m7
    ])

    numerator_b0 = np.linalg.det([
        [k0, m0[1], m0[2], m0[3], m0[4], m0[5], m0[6], m0[7]],
        [k1, m1[1], m1[2], m1[3], m1[4], m1[5], m1[6], m1[7]],
        [k2, m2[1], m2[2], m2[3], m2[4], m2[5], m2[6], m2[7]],
        [k3, m3[1], m3[2], m3[3], m3[4], m3[5], m3[6], m3[7]],
        [k4, m4[1], m4[2], m4[3], m4[4], m4[5], m4[6], m4[7]],
        [k5, m5[1], m5[2], m5[3], m5[4], m5[5], m5[6], m5[7]],
        [k6, m6[1], m6[2], m6[3], m6[4], m6[5], m6[6], m6[7]],
        [k7, m7[1], m7[2], m7[3], m7[4], m7[5], m7[6], m7[7]]
    ])

    numerator_b1 = np.linalg.det([
        [m0[0], k0, m0[2], m0[3], m0[4], m0[5], m0[6], m0[7]],
        [m1[0], k1, m1[2], m1[3], m1[4], m1[5], m1[6], m1[7]],
        [m2[0], k2, m2[2], m2[3], m2[4], m2[5], m2[6], m2[7]],
        [m3[0], k3, m3[2], m3[3], m3[4], m3[5], m3[6], m3[7]],
        [m4[0], k4, m4[2], m4[3], m4[4], m4[5], m4[6], m4[7]],
        [m5[0], k5, m5[2], m5[3], m5[4], m5[5], m5[6], m5[7]],
        [m6[0], k6, m6[2], m6[3], m6[4], m6[5], m6[6], m6[7]],
        [m7[0], k7, m7[2], m7[3], m7[4], m7[5], m7[6], m7[7]]
    ])

    numerator_b2 = np.linalg.det([
        [m0[0], m0[1], k0, m0[3], m0[4], m0[5], m0[6], m0[7]],
        [m1[0], m1[1], k1, m1[3], m1[4], m1[5], m1[6], m1[7]],
        [m2[0], m2[1], k2, m2[3], m2[4], m2[5], m2[6], m2[7]],
        [m3[0], m3[1], k3, m3[3], m3[4], m3[5], m3[6], m3[7]],
        [m4[0], m4[1], k4, m4[3], m4[4], m4[5], m4[6], m4[7]],
        [m5[0], m5[1], k5, m5[3], m5[4], m5[5], m5[6], m5[7]],
        [m6[0], m6[1], k6, m6[3], m6[4], m6[5], m6[6], m6[7]],
        [m7[0], m7[1], k7, m7[3], m7[4], m7[5], m7[6], m7[7]]
    ])

    numerator_b3 = np.linalg.det([
        [m0[0], m0[1], m0[2], k0, m0[4], m0[5], m0[6], m0[7]],
        [m1[0], m1[1], m1[2], k1, m1[4], m1[5], m1[6], m1[7]],
        [m2[0], m2[1], m2[2], k2, m2[4], m2[5], m2[6], m2[7]],
        [m3[0], m3[1], m3[2], k3, m3[4], m3[5], m3[6], m3[7]],
        [m4[0], m4[1], m4[2], k4, m4[4], m4[5], m4[6], m4[7]],
        [m5[0], m5[1], m5[2], k5, m5[4], m5[5], m5[6], m5[7]],
        [m6[0], m6[1], m6[2], k6, m6[4], m6[5], m6[6], m6[7]],
        [m7[0], m7[1], m7[2], k7, m7[4], m7[5], m7[6], m7[7]]
    ])

    numerator_b12 = np.linalg.det([
        [m0[0], m0[1], m0[2], m0[3], k0, m0[5], m0[6], m0[7]],
        [m1[0], m1[1], m1[2], m1[3], k1, m1[5], m1[6], m1[7]],
        [m2[0], m2[1], m2[2], m2[3], k2, m2[5], m2[6], m2[7]],
        [m3[0], m3[1], m3[2], m3[3], k3, m3[5], m3[6], m3[7]],
        [m4[0], m4[1], m4[2], m4[3], k4, m4[5], m4[6], m4[7]],
        [m5[0], m5[1], m5[2], m5[3], k5, m5[5], m5[6], m5[7]],
        [m6[0], m6[1], m6[2], m6[3], k6, m6[5], m6[6], m6[7]],
        [m7[0], m7[1], m7[2], m7[3], k7, m7[5], m7[6], m7[7]]
    ])

    numerator_b13 = np.linalg.det([
        [m0[0], m0[1], m0[2], m0[3], m0[4], k0, m0[6], m0[7]],
        [m1[0], m1[1], m1[2], m1[3], m1[4], k1, m1[6], m1[7]],
        [m2[0], m2[1], m2[2], m2[3], m2[4], k2, m2[6], m2[7]],
        [m3[0], m3[1], m3[2], m3[3], m3[4], k3, m3[6], m3[7]],
        [m4[0], m4[1], m4[2], m4[3], m4[4], k4, m4[6], m4[7]],
        [m5[0], m5[1], m5[2], m5[3], m5[4], k5, m5[6], m5[7]],
        [m6[0], m6[1], m6[2], m6[3], m6[4], k6, m6[6], m6[7]],
        [m7[0], m7[1], m7[2], m7[3], m7[4], k7, m7[6], m7[7]]
    ])

    numerator_b23 = np.linalg.det([
        [m0[0], m0[1], m0[2], m0[3], m0[4], m0[5], k0, m0[7]],
        [m1[0], m1[1], m1[2], m1[3], m1[4], m1[5], k1, m1[7]],
        [m2[0], m2[1], m2[2], m2[3], m2[4], m2[5], k2, m2[7]],
        [m3[0], m3[1], m3[2], m3[3], m3[4], m3[5], k3, m3[7]],
        [m4[0], m4[1], m4[2], m4[3], m4[4], m4[5], k4, m4[7]],
        [m5[0], m5[1], m5[2], m5[3], m5[4], m5[5], k5, m5[7]],
        [m6[0], m6[1], m6[2], m6[3], m6[4], m6[5], k6, m6[7]],
        [m7[0], m7[1], m7[2], m7[3], m7[4], m7[5], k7, m7[7]]
    ])

    numerator_b123 = np.linalg.det([
        [m0[0], m0[1], m0[2], m0[3], m0[4], m0[5], m0[6], k0],
        [m1[0], m1[1], m1[2], m1[3], m1[4], m1[5], m1[6], k1],
        [m2[0], m2[1], m2[2], m2[3], m2[4], m2[5], m2[6], k2],
        [m3[0], m3[1], m3[2], m3[3], m3[4], m3[5], m3[6], k3],
        [m4[0], m4[1], m4[2], m4[3], m4[4], m4[5], m4[6], k4],
        [m5[0], m5[1], m5[2], m5[3], m5[4], m5[5], m5[6], k5],
        [m6[0], m6[1], m6[2], m6[3], m6[4], m6[5], m6[6], k6],
        [m7[0], m7[1], m7[2], m7[3], m7[4], m7[5], m7[6], k7]
    ])

    b0 = numerator_b0 / denominator
    b1 = numerator_b1 / denominator
    b2 = numerator_b2 / denominator
    b3 = numerator_b3 / denominator
    b12 = numerator_b12 / denominator
    b13 = numerator_b13 / denominator
    b123 = numerator_b123 / denominator

    print("b\u2080:", "%.2f" % b0, " b\u2081:", "%.2f" % b1, " b\u2082:", "%.2f" % b2, " b\u2083:", "%.2f" % b3,
          " b\u2081\u2082:", "%.2f" % b12,
          " b\u2081\u2083:", "%.2f" % b13, " b\u2081\u2082\u2083:", "%.2f" % b123)

    print(
        f"Рівняння регресії: y = {b0:.2f}{b1:+.2f}*x\u2081{b2:+.2f}*x\u2082{b3:+.2f}*x\u2083{b12:+.2f}*x\u2081\u2082{b13:+.2f}*x\u2081\u2083{b123:+.2f}*x\u2081\u2082\u2083")

    # find dispersion
    S2 = []
    for i in range(len(y_list)):
        S2.append(((y_list[i][0] - my_list[i]) ** 2 + (y_list[i][1] - my_list[i]) ** 2 + (
                y_list[i][2] - my_list[i]) ** 2) / 3)

    """KOHREN"""
    Gp = max(S2) / sum(S2)

    m = len(y_list[0])
    f1 = m - 1
    f2 = N  # N=8
    q = 0.05

    Gt = [None, 0.68, 0.516, 0.438, 0.391, 0.3595, 0.3365, 0.3185, 0.3043, 0.2926, 0.2829, 0.2462, 0.2022, 0.1616,
          0.1250]
    print("Gt:", Gt[f1])

    if Gp < Gt[f1]:
        print("Дисперсія однорідна")
        break
    else:
        print("Дисперсія не однорідна")
        m += 1
        y_add_el()

x_matrix_normal = [
    [1, -1, -1, -1],
    [1, -1, -1, 1],
    [1, -1, 1, -1],
    [1, -1, 1, 1],
    [1, 1, -1, -1],
    [1, 1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 1, 1],
]

"""STUDENT"""


def getBeta(i):
    summa = 0
    for j in range(N):
        summa += my_list[j] * x_matrix_normal[j][i]
    summa /= N
    return summa


S2B = sum(S2) / N
S2beta = S2B / (N * m)
Sbeta = np.sqrt(S2beta)

beta0 = getBeta(0)
beta1 = getBeta(1)
beta2 = getBeta(2)
beta3 = getBeta(3)

t_criterion = []
t_criterion.append(abs(beta0) / Sbeta, )
t_criterion.append(abs(beta1) / Sbeta)
t_criterion.append(abs(beta2) / Sbeta)
t_criterion.append(abs(beta3) / Sbeta)

t0 = abs(beta0) / Sbeta
t1 = abs(beta1) / Sbeta
t2 = abs(beta2) / Sbeta
t3 = abs(beta3) / Sbeta

f3 = f1 * f2

t_tab = scipy.stats.t.ppf((1 + (1 - q)) / 2, f3)
print("t табличне:", t_tab)
if t0 < t_tab:
    b0 = 0
    print("t\u2080:", t0, " t0<t_tab; b0=0")
if t1 < t_tab:
    b1 = 0
    print("t\u2081:", t1, " t\u2081<t_tab; b\u2081=0")
if t2 < t_tab:
    b2 = 0
    print("t\u2082:", t2, " t\u2082<t_tab; b\u2082=0")
if t3 < t_tab:
    b3 = 0
    print("t\u2083:", t3, " t\u2083<t_tab; b\u2083=0")

y_hat = []
for i in range(N):
    y_hat.append(
        b0 + b1 * x_matrix[i][0] + b2 * x_matrix[i][1] + b3 * x_matrix[i][2] + b12 * x_matrix[i][0] * x_matrix[i][1] +
        b13 * x_matrix[i][0] * x_matrix[i][2] + b123 * x_matrix[i][0] * x_matrix[i][1] * x_matrix[i][2])

    print(
        f"y{chr(8321 + i)}^ = {b0:.2f}{b1:+.2f}*x{chr(8321 + i)}\u2081{b2:+.2f}*x{chr(8321 + i)}\u2082{b3:+.2f}*x{chr(8321 + i)}\u2083{b12:+.2f}*x{chr(8321 + i)}\u2081"
        f"*x{chr(8321 + i)}\u2082{b13:+.2f}*x{chr(8321 + i)}\u2081*x{chr(8321 + i)}\u2083{b123:+.2f}*x{chr(8321 + i)}\u2081*x{chr(8321 + i)}\u2082*x{chr(8321 + i)}\u2083 "
        f"= {y_hat[i]:.2f}")

"""FISHER"""

d = 2
f4 = N - d
S2_ad = 0
for i in range(N):
    S2_ad += (m / (N - d) * ((y_hat[i] - my_list[i]) ** 2))

Fp = S2_ad / S2B
Ft = scipy.stats.f.ppf(1 - q, f4, f3)
print("Fp:", Fp)
print("Ft:", Ft)
if Fp > Ft:
    print("Рівняння регресії не адекватно оригіналу при рівні значимості 0,05")
else:
    print("Рівняння регресії адекватно оригіналу при рівні значимості 0,05")

print("час роботи програми =", datetime.now() - start_time)

