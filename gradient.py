import numpy as np
# import matplotlib.pyplot as plt

# Fungsi kuadrat yang akan dioptimalkan
def fungsi_kuadrat(x):
    return x**2 - 4*x + 4

# Turunan fungsi kuadrat terhadap x
def turunan_fungsi(x):
    return 2*x - 4

def gradient_descent(learning_rate, initial_x, num_iterations):
    print("iterasi ke ",num_iterations)
    x = initial_x
    x_history = [x]

    for _ in range(num_iterations):
        gradient = turunan_fungsi(x)
        x = x - learning_rate * gradient
        x_history.append(x)

    return x_history

# Parameter untuk gradient descent
learning_rate = 0.1
initial_x = 0.0
num_iterations = 10

# Menjalankan gradient descent
history = gradient_descent(learning_rate, initial_x, num_iterations)

# Plot fungsi kinerja dan perubahan nilai x
x_values = np.linspace(-2, 6, 100)
y_values = fungsi_kuadrat(x_values)

print(x_values)
print(y_values)
# plt.plot(x_values, y_values, label='f(x) = x^2 - 4x + 4')
# plt.scatter(history, [fungsi_kuadrat(x) for x in history], color='red', label='Iterasi Gradient Descent')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.show()
