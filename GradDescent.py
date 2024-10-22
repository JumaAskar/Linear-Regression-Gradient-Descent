import random

def derivative_k (arr1, arr2, n, k, b):
    sum_all = 0
    for i in range(len(arr1)):
        sum_all += (k * arr1[i] + b - arr2[i])
    der = 2 * sum_all * arr1[i] / n
    return der

def derivative_b (arr1, arr2, n, k, b):
    sum_all = 0
    for i in range(len(arr1)):
        sum_all += (k * arr1[i] + b - arr2[i])
    der = 2 * sum_all / n
    return der

def MSE (arr1, arr2, n, k, b):
    sum_all = 0
    for i in range(len(arr1)):
        sum_all += (arr1[i] * k + b - arr2[i]) ** 2
    cost_function = sum_all / n
    return cost_function

lr = 0.00005
limit = 5000
n = int(input("Enter the number of points.\n"))
xs = []
ys = []
tem_k = 0
tem_b = 0

for i in range(0, n):
    in_put = input("Enter the x & y coordinates of the point {0}.\n".format(i))
    in_put = in_put.split(" ")
    xs.append(int(in_put[0]))
    ys.append(int(in_put[1]))
    
k = random.randint(0, 15)
b = random.randint(0, 100)
while MSE(xs, ys, n, k, b) > limit:
    tem_k = k - lr * derivative_k(xs, ys, n, k, b)
    tem_b = b - lr * derivative_b(xs, ys, n, k, b)
    k = tem_k
    b = tem_b

print(MSE(xs, ys, n, k, b))
print(k)
print(b)
