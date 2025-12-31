# DSA Practice 🧠

This repository contains topic-wise solutions to **LeetCode DSA problems** solved in Python.  
Each solution includes the relevant problem approach and logic.

---

## 📚 Array Problems

### 🟦 Easy
| Problem | LeetCode # | File |
|---------|------------|------|
| Two Sum | 1 | `two_sum.py` |
| Contains Duplicate | 217 | `contains_duplicate.py` |
| Best Time to Buy and Sell Stock | 121 | `max_profit.py` |
| Move Zeroes | 283 | `move_zeroes.py` |
| Max Subarray | 53 | `maximum_subarray.py` |

### 🟨 Medium
| Problem | LeetCode # | File |
|---------|------------|------|
| Remove Duplicates from Sorted Array | 26 | `remove_duplicates_sorted_array.py` |

---

## 🧩 String Problems

### 🟩 Easy
| Problem | LeetCode # | File |
|---------|------------|------|
| Valid Anagram | 242 | `valid_anagram.py` |

---

## 📈 Technique-wise

### Two Pointers / Sliding Window
- `max_profit.py` — maximize profit by tracking min price and selling — **O(n)**, **O(1)**
- `move_zeroes.py` — shift non-zeros forward — **O(n)**, **O(1)**

### Sorting / Comparison
- `contains_duplicate.py` — sort and compare adjacent — **O(n log n)**, **O(1)**
- `valid_anagram.py` — sort strings and compare — **O(n log n)**, **O(n)**

### Kadane’s / DP
- `maximum_subarray.py` — sliding window / Kadane’s for best subarray sum — **O(n)**, **O(1)**

### In-Place Overwrite
- `remove_duplicates_sorted_array.py` — two-pointer in sorted array — **O(n)**, **O(1)**

---

## 🛠 How to Run
1. Clone the repo  
2. Install requirements (if any)  
3. Run each script using Python:
   ```bash
   python3 maximum_subarray.py
