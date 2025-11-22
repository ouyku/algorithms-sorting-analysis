#visualization script for benchmarking results using matplotlib
#creates charts showing running times for all implementations
#this script reads the csv file created by benchmark.py and makes graphs

import csv
import matplotlib.pyplot as plt
def main():
#main function that loads the csv, makes charts, and shows them

    filename = 'benchmark_results.csv'
    sizes = []
    array_mergesort = []
    array_quicksort = []
    linkedlist_mergesort = []
    linkedlist_quicksort = []

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sizes.append(int(row['size']))
                array_mergesort.append(float(row['array_mergesort']))
                array_quicksort.append(float(row['array_quicksort']))
                linkedlist_mergesort.append(float(row['linkedlist_mergesort']))
                linkedlist_quicksort.append(float(row['linkedlist_quicksort']))
    except FileNotFoundError:
        print(f"error: {filename} not found. run benchmark.py first.")
        return

    #make a 2x2 grid of charts
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('sorting algorithm performance', fontsize=16, fontweight='bold')
    #chart 1: merge sort array vs linked list
    axes[0, 0].plot(sizes, array_mergesort, 'o-', label='array', linewidth=2, markersize=6)
    axes[0, 0].plot(sizes, linkedlist_mergesort, 's-', label='linked list', linewidth=2, markersize=6)
    axes[0, 0].set_title('merge sort: array vs linked list')
    axes[0, 0].set_xlabel('input size (2^n)')
    axes[0, 0].set_ylabel('time (ms)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xscale('log', base=2)
    axes[0, 0].set_yscale('log')

    #chart 2: quick sort array vs linked list
    axes[0, 1].plot(sizes, array_quicksort, 'o-', label='array', linewidth=2, markersize=6)
    axes[0, 1].plot(sizes, linkedlist_quicksort, 's-', label='linked list', linewidth=2, markersize=6)
    axes[0, 1].set_title('quick sort: array vs linked list')
    axes[0, 1].set_xlabel('input size (2^n)')
    axes[0, 1].set_ylabel('time (ms)')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xscale('log', base=2)
    axes[0, 1].set_yscale('log')

    #chart 3: all four together
    axes[1, 0].plot(sizes, array_mergesort, 'o-', label='array merge', linewidth=2, markersize=6)
    axes[1, 0].plot(sizes, array_quicksort, 's-', label='array quick', linewidth=2, markersize=6)
    axes[1, 0].plot(sizes, linkedlist_mergesort, '^-', label='list merge', linewidth=2, markersize=6)
    axes[1, 0].plot(sizes, linkedlist_quicksort, 'v-', label='list quick', linewidth=2, markersize=6)
    axes[1, 0].set_title('all four implementations')
    axes[1, 0].set_xlabel('input size (2^n)')
    axes[1, 0].set_ylabel('time (ms)')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xscale('log', base=2)
    axes[1, 0].set_yscale('log')

    #chart 4: array merge vs array quick
    axes[1, 1].plot(sizes, array_mergesort, 'o-', label='merge sort', linewidth=2, markersize=6)
    axes[1, 1].plot(sizes, array_quicksort, 's-', label='quick sort', linewidth=2, markersize=6)
    axes[1, 1].set_title('array merge vs quick')
    axes[1, 1].set_xlabel('input size (2^n)')
    axes[1, 1].set_ylabel('time (ms)')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xscale('log', base=2)
    axes[1, 1].set_yscale('log')

    #tight layout and save
    plt.tight_layout()
    plt.savefig('sorting_performance.png', dpi=300, bbox_inches='tight')
    print("charts saved to sorting_performance.png")
    plt.show()
#this runs when you execute: python3 visualize.py
if __name__ == '__main__':
    main()
