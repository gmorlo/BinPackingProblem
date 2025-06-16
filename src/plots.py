import matplotlib.pyplot as plt
import random

def plot_bins(bins, title):


    fig, ax = plt.subplots(figsize=(10, 6))
    y_offset = 0
    colors = list(plt.cm.tab20.colors)
    random.shuffle(colors)

    for bin in bins:
        start = 0
        for i, item in enumerate(bin.item_list):
            ax.broken_barh([(start, item)], (y_offset, 0.5),
                           facecolors=colors[i % len(colors)],
                           edgecolor='black')
            start += item
        y_offset += 1

    ax.set_title(title)
    ax.set_xlabel("Bin Capacity")
    ax.set_ylabel("Bins")
    plt.show()

def plot_convergence_curve(score_history, title="Convergence Curve"):
    plt.figure(figsize=(10, 5))
    plt.plot(score_history, marker='o', linestyle='-', color='blue')
    plt.xlabel("Iteracja")
    plt.ylabel("Score")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
