from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []
    
    window = deque()
    result = []
    
    for i, num in enumerate(nums):
        while window and window[0] < i - k + 1:
            window.popleft()
        
        while window and nums[window[-1]] < num:
            window.pop()
        
        window.append(i)
        
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result
```

Kodni ishlatish uchun misol:
```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # [3, 3, 5, 5, 6, 7]
