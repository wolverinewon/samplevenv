# plots_demo.py
"""
Demo script showing various matplotlib plots
"""

import numpy as np
import matplotlib.pyplot as plt

# Create some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)
categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]

def line_plot():
    plt.figure()
    plt.plot(x, y, label="sin(x)")
    plt.plot(x, y2, label="cos(x)", linestyle="--")
    plt.title("Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()

def scatter_plot():
    plt.figure()
    plt.scatter(x, y, c="red", marker="o", label="sin(x)")
    plt.title("Scatter Plot")
    plt.legend()
    plt.show()

def bar_chart():
    plt.figure()
    plt.bar(categories, values, color="skyblue")
    plt.title("Bar Chart")
    plt.show()

def histogram():
    data = np.random.randn(1000)
    plt.figure()
    plt.hist(data, bins=30, color="orange", edgecolor="black")
    plt.title("Histogram")
    plt.show()

def pie_chart():
    plt.figure()
    plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=90)
    plt.title("Pie Chart")
    plt.show()

if __name__ == "__main__":
    line_plot()
    scatter_plot()
    bar_chart()
    histogram()
    pie_chart()
