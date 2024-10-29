def derivative_w (x, y, w, b):
    sum_all = 0
    for x_i, y_i in zip(x, y):
        sum_all += (w * x_i + b - y_i) * x_i
    der = 2 * sum_all / len(x)
    return der


def derivative_b (x, y, w, b):
    sum_all = 0
    for x_i, y_i in zip(x, y):
        sum_all += w * x_i + b - y_i
    der = 2 * sum_all / len(x)
    return der


def cost_function(x, y, w, b):
    sum_all = 0
    for x_i, y_i in zip(x, y):
        sum_all += (w * x_i + b - y_i) ** 2
    cost_function = sum_all / len(x)
    return cost_function


learning_rate_w = 0.00001
learning_rate_b = 0.001

limit = 100

x = []
y = []

temp_w = 0
temp_b = 0

points_number = int(input("Enter the number of points.\n"))

for i in range(1, points_number + 1):
    points_input = input("Enter the x & y coordinates of the point {0}.\n".format(i))
    points_input = points_input.split(" ")
    x.append(int(points_input[0]))
    y.append(int(points_input[1]))

w = 0
b = 0

for _ in range(limit):
    temp_w = w - learning_rate_w * derivative_w(x, y, w, b)
    temp_b = b - learning_rate_b * derivative_b(x, y, w, b)
    w = temp_w
    b = temp_b
    # print("w:", w, "| b:", b, "| cost function:", cost_function(x, y, w, b))

print("w:", w)
print("b:", b)
print("cost function:", cost_function(x, y, w, b))

