# 📍 Part 1: Functions are Objects in Python

In Python, functions are **first-class objects**. That means:

✅ You can:
- Assign them to variables
- Pass them to other functions
- Return them from functions

### 💡 Why this matters
This concept is the **foundation** for understanding decorators. Decorators are built on the idea of returning and wrapping functions.

### 📂 Related File
[`Functions_are_Objects.py`](./Functions_are_Objects.py)

📌 **Next Part**: [Function Inside Function →](./02_function_inside_function.py)
---

# 📍 Part 2: Function Inside Function

In Python, you can **define a function inside another function**.  

✅ Why?  
- To keep helper logic private.  
- To organize code into steps.  
- It's the building block for **closures** and **decorators**.

---

## 💻 Example
```python
def outer():
    def inner():
        print("Inner function")
    inner()

outer()

