def sum_of_squares (arr):
    i = 0
    sum_of_squares = 0
    while i < len(arr):
        sum_of_squares += (arr[i] ** 2)
        i += 1
    return sum_of_squares

def sum_of_xy (arr1, arr2):
    i = 0
    sum_of_xy = 0
    while i < len(arr1):
        sum_of_xy += arr1[i] * arr2[i]
        i += 1
    return sum_of_xy

n = int(input("Enter the number of points.\n"))
xs = []
ys = []

for i in range(0, n):
    in_put = input("Enter the x & y coordinates of the point {0}.\n".format(i))
    in_put = in_put.split(" ")
    xs.append(int(in_put[0]))
    ys.append(int(in_put[1]))
    
k = (n * sum_of_xy(xs, ys) - sum(xs) * sum(ys)) / (n * sum_of_squares(xs) - sum(xs) ** 2)
b = (sum(ys) - k * sum(xs)) / n
print(k)
print(b)
