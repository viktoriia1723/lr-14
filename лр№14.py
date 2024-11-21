import numpy as np
import matplotlib.pyplot as plt

def plot_complex_function():
    """
    Побудова графіка функції Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2))
    """
    x = np.linspace(0.01, 5, 200)  # Уникаємо поділу на 0
    y = 5 * np.cos(10*x) * np.sin(3*x) / np.sqrt(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title('Графік функції Y(x) = 5*cos(10x)*sin(3x)/√x')
    plt.xlabel('x')
    plt.ylabel('Y(x)')
    plt.grid(True)
    plt.show()

plot_complex_function()