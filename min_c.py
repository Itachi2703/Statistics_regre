counter = 0
counter_list = []
list_y = []
with open("profits.csv", "r") as f:
    lines = f.readlines()
    lines.pop(0)
    for i in lines:
        counter = counter + 1
        counter_list.append(counter)
        line = i.split(",")
        list_y.append(int(line[0]))
print("My counter is " + str(counter))
# b

x_y = []
x_2 = []
n_counter = -1
for i in list_y:
    n_counter = n_counter + 1
    x_2.append(counter_list[n_counter]**2)
    x_y.append(i * counter_list[n_counter])


x_2_sum = sum(x_2)
x_y_sum = sum(x_y)
list_y_sum = sum(list_y)
counter_list_sum = sum(counter_list)

# F1
f1 = counter * x_y_sum
f2 = counter_list_sum * list_y_sum
f3 = counter * x_2_sum
f4 = counter_list_sum**2

b_1 = f1 - f2
b_2 = f3 - f4
# b
# b
b = b_1 / b_2

# a
# a
# a
f1_a = b * counter_list_sum
f1_a_1 = list_y_sum - f1_a
# res a 
# res a
a = f1_a_1 / counter


# y
# y
# y
# y
new = counter + 1
y_new = b*counter
y = a + y_new
print("My forecast is:   " + str(y))




