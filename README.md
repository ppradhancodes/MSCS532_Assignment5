# Quicksort Algorithm Analysis

This project implements and analyzes both deterministic and randomized versions of the Quicksort algorithm. It compares their performance across various input sizes and distributions.

## Requirements

- Python 3.6 or higher

## How to Run

1. Ensure you have Python installed on your system.
2. Download the `randomizedQuickSort.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `randomizedQuickSort.py`.
5. Run the script using the following command:

6. After execution, the results will be written to a file named `output.txt` in the same directory.

## Summary of Findings

Our analysis of deterministic and randomized Quicksort reveals several key insights:

1. Average Case Performance:
- Both versions typically show O(n log n) time complexity for random inputs.
- This aligns with theoretical expectations of balanced partitioning.

2. Best Case Scenario:
- Randomized Quicksort often outperforms the deterministic version for sorted or nearly sorted inputs.
- This demonstrates the effectiveness of random pivot selection in avoiding worst-case scenarios.

3. Worst Case Performance:
- Deterministic Quicksort shows poor performance (closer to O(n^2)) for sorted or reverse-sorted inputs.
- Randomized version maintains more consistent performance across different input distributions.

4. Large Input Sizes:
- Performance differences become more pronounced with larger inputs.
- Randomized version shows better scalability, especially for non-random distributions.

5. Space Complexity:
- Both versions typically use O(log n) space for the recursion stack.
- In worst-case scenarios, particularly for the deterministic version, this can increase to O(n).

6. Consistency and Robustness:
- Randomized Quicksort demonstrates more consistent performance across various input types.
- It's less susceptible to worst-case scenarios, making it more reliable for general use.

## Conclusion

Randomized Quicksort generally performs better or equally well compared to its deterministic counterpart, especially for sorted or partially sorted arrays. It effectively mitigates worst-case scenarios and provides more consistent performance across different input distributions. This empirical analysis supports the theoretical advantages of randomization in the Quicksort algorithm, particularly in real-world scenarios where input distributions may vary.

For detailed results and analysis, please refer to the `output.txt` file generated after running the script.