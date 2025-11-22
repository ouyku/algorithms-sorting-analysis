#1. builds random arrays of size 2, 4, 8, ..., 4096
#2. runs the four python sorting functions on each size
#3. prints the timing to the screen and saves it to a csv file

import random
import time
import csv

from amergesort import mergesort_array
from aquicksort import quicksort_array
from lmergesort import mergesort_linked_list, Node
from lquicksort import quicksort_linked_list

random.seed(42)  # so results are reproducible

def array_to_linked_list(numbers):
    #helper: turn [3, 1, 2] into Node(3)->Node(1)->Node(2)
    if not numbers:
        return None
    head = Node(numbers[0])
    current = head
    for value in numbers[1:]:
        current.next = Node(value)
        current = current.next
    return head


def random_array(size):
    #helper: create a random array of given size
    return [random.randint(0, 10_000) for _ in range(size)]

def time_sort(sort_function, values, use_linked_list=False):
    #helper: measure how long a sort takes (returns milliseconds)
    if use_linked_list:
        head = array_to_linked_list(values)
        start = time.perf_counter()
        sort_function(head)
        end = time.perf_counter()
    else:
        # use array directly
        copy = values.copy()
        start = time.perf_counter()
        sort_function(copy)
        end = time.perf_counter()
    
    return (end - start) * 1000


def main():
    sizes = [2 ** n for n in range(1, 13)]
    tests = [
        ("array_mergesort", mergesort_array, False),
        ("array_quicksort", quicksort_array, False),
        ("linkedlist_mergesort", mergesort_linked_list, True),
        ("linkedlist_quicksort", quicksort_linked_list, True),
    ]
    results = []

    print("running benchmarks...")
    for size in sizes:
        numbers = random_array(size)
        row = {"size": size}
        print(f"\nsize {size}:")
        for name, func, use_ll in tests:
            ms = time_sort(func, numbers, use_ll)
            row[name] = ms
            print(f"  {name:22} {ms:8.2f} ms")
        results.append(row)

    with open("benchmark_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("\nresults saved to benchmark_results.csv")


if __name__ == "__main__":
    main()
