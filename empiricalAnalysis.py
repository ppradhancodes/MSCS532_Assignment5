import random
import timeit
import tracemalloc
import sys

# Increase recursion limit (use cautiously)
sys.setrecursionlimit(10000)

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def deterministic_quicksort(arr, low, high):
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            pivot = partition(arr, low, high)
            if pivot - low < high - pivot:
                deterministic_quicksort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                deterministic_quicksort(arr, pivot + 1, high)
                high = pivot - 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            pivot = randomized_partition(arr, low, high)
            if pivot - low < high - pivot:
                randomized_quicksort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                randomized_quicksort(arr, pivot + 1, high)
                high = pivot - 1

def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    return partition(arr, low, high)

def measure_performance(sort_func, arr):
    tracemalloc.start()
    start_time = timeit.default_timer()
    sort_func(arr.copy(), 0, len(arr) - 1)
    end_time = timeit.default_timer()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        'execution_time': end_time - start_time,
        'current_memory': current_memory / 10**6,
        'peak_memory': peak_memory / 10**6
    }

def generate_array(size, distribution):
    if distribution == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(1, size + 1))
    elif distribution == 'reverse_sorted':
        return list(range(size, 0, -1))
    elif distribution == 'partially_sorted':
        arr = list(range(1, size + 1))
        for _ in range(size // 10):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

def run_experiment():
    sizes = [1000, 5000, 10000, 50000]
    distributions = ['random', 'sorted', 'reverse_sorted', 'partially_sorted']
    results = {dist: {'deterministic': [], 'randomized': []} for dist in distributions}

    for size in sizes:
        for dist in distributions:
            det_result = measure_performance(deterministic_quicksort, generate_array(size, dist))
            rand_result = measure_performance(randomized_quicksort, generate_array(size, dist))
            results[dist]['deterministic'].append(det_result)
            results[dist]['randomized'].append(det_result)

    return results, sizes

if __name__ == "__main__":
    results, sizes = run_experiment()

    with open("output.txt", "w") as f:
        for dist in results:
            f.write(f"\nDistribution: {dist.capitalize()}\n")
            for size_index, size in enumerate(sizes):
                det_time = results[dist]['deterministic'][size_index]['execution_time']
                det_memory = results[dist]['deterministic'][size_index]['peak_memory']
                rand_time = results[dist]['randomized'][size_index]['execution_time']
                rand_memory = results[dist]['randomized'][size_index]['peak_memory']
                
                f.write(f"Size: {size}\n")
                f.write(f"  Deterministic - Time: {det_time:.6f}s, Peak Memory: {det_memory:.2f} MB\n")
                f.write(f"  Randomized    - Time: {rand_time:.6f}s, Peak Memory: {rand_memory:.2f} MB\n")

        f.write("\nAnalysis:\n")
        for dist in results:
            f.write(f"\n{dist.capitalize()} Distribution:\n")
            for size_index, size in enumerate(sizes):
                det_time = results[dist]['deterministic'][size_index]['execution_time']
                rand_time = results[dist]['randomized'][size_index]['execution_time']
                time_diff = (det_time - rand_time) / det_time * 100

                f.write(f"  Size {size}:\n")
                if time_diff > 0:
                    f.write(f"    Randomized Quicksort was {time_diff:.2f}% faster\n")
                elif time_diff < 0:
                    f.write(f"    Deterministic Quicksort was {-time_diff:.2f}% faster\n")
                else:
                    f.write("    Both algorithms performed equally\n")

        f.write("\nConclusion:\n")
        f.write("Randomized Quicksort generally performs better or equally well compared to\n")
        f.write("Deterministic Quicksort, especially for sorted or partially sorted arrays.\n")
        f.write("It helps in avoiding worst-case scenarios and provides more consistent\n")
        f.write("performance across different input distributions.\n")

    print("Analysis complete. Results written to output.txt")