from .basics import fabs


def bubble_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    a = list(arr)
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    a = list(arr)
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr):
    a = list(arr)
    n = len(a)

    def heapify(a, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a


def counting_sort(arr, max_val=None):
    a = list(arr)
    if not a:
        return a
    if max_val is None:
        max_val = max(a)
    count = [0] * (max_val + 1)
    for x in a:
        count[x] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result


def radix_sort(arr):
    a = list(arr)
    if not a:
        return a
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a:
            buckets[(x // exp) % 10].append(x)
        a = [x for bucket in buckets for x in bucket]
        exp *= 10
    return a


def shell_sort(arr):
    a = list(arr)
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


def bucket_sort(arr, num_buckets=10):
    if not arr:
        return []
    lo, hi = min(arr), max(arr)
    if lo == hi:
        return list(arr)
    bucket_range = (hi - lo) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    for x in arr:
        idx = int((x - lo) / bucket_range)
        if idx == num_buckets:
            idx -= 1
        buckets[idx].append(x)
    return [x for bucket in buckets for x in insertion_sort(bucket)]


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_leftmost(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo if lo < len(arr) and arr[lo] == target else -1


def binary_search_rightmost(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1 if lo > 0 and arr[lo - 1] == target else -1


def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[hi] == arr[lo]:
            if arr[lo] == target:
                return lo
            break
        pos = lo + int((target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


def exponential_search(arr, target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr[i // 2: min(i, len(arr))], target)


def ternary_search(f, lo, hi, tol=1e-9):
    while hi - lo > tol:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            lo = m1
        else:
            hi = m2
    return (lo + hi) / 2


def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost,
            )
    return dp[m][n]


def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                best = max(best, dp[i][j])
    return best


def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
    return dp[amount] if dp[amount] != float("inf") else -1


def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def max_subarray(arr):
    max_sum = arr[0]
    cur_sum = arr[0]
    for x in arr[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum


def max_subarray_indices(arr):
    max_sum = arr[0]
    cur_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > cur_sum + arr[i]:
            cur_sum = arr[i]
            temp_start = i
        else:
            cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = temp_start
            end = i
    return start, end, max_sum


def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return seen[complement], i
        seen[x] = i
    return None


def three_sum(arr, target):
    arr = sorted(arr)
    results = []
    for i in range(len(arr) - 2):
        lo, hi = i + 1, len(arr) - 1
        while lo < hi:
            s = arr[i] + arr[lo] + arr[hi]
            if s == target:
                results.append((arr[i], arr[lo], arr[hi]))
                lo += 1
                hi -= 1
            elif s < target:
                lo += 1
            else:
                hi -= 1
    return results


def flatten(nested):
    result = []
    stack = [nested]
    while stack:
        item = stack.pop()
        if isinstance(item, (list, tuple)):
            for sub in reversed(item):
                stack.append(sub)
        else:
            result.append(item)
    return result


def rotate_list(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    return arr[k:] + arr[:k]


def chunk_list(arr, size):
    return [arr[i:i + size] for i in range(0, len(arr), size)]


def sliding_window_max(arr, k):
    if not arr or k <= 0:
        return []
    result = []
    deque = []
    for i, x in enumerate(arr):
        while deque and deque[0] < i - k + 1:
            deque.pop(0)
        while deque and arr[deque[-1]] < x:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            result.append(arr[deque[0]])
    return result


def sliding_window_sum(arr, k):
    if len(arr) < k:
        return []
    window = sum(arr[:k])
    result = [window]
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        result.append(window)
    return result


def running_average(arr):
    result = []
    total = 0.0
    for i, x in enumerate(arr):
        total += x
        result.append(total / (i + 1))
    return result


def cumulative_sum(arr):
    result = []
    total = 0
    for x in arr:
        total += x
        result.append(total)
    return result


def cumulative_product(arr):
    result = []
    total = 1
    for x in arr:
        total *= x
        result.append(total)
    return result


def moving_average(arr, window):
    if window > len(arr):
        return []
    return [sum(arr[i:i + window]) / window for i in range(len(arr) - window + 1)]


def zip_with(f, a, b):
    return [f(x, y) for x, y in zip(a, b)]


def difference_array(arr):
    return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]


def second_difference_array(arr):
    return difference_array(difference_array(arr))
