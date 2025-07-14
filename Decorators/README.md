# 📍 Part 1: Functions are Objects in Python

In Python, functions are **first-class objects**. That means:

✅ You can:
- Assign them to variables
- Pass them to other functions
- Return them from functions

### 💡 Why this matters
This concept is the **foundation** for understanding decorators. Decorators are built on the idea of returning and wrapping functions.

### 📂 Related File
[`Functions_are_Objects.ipynb`](./Functions_are_Objects.ipynb)

📌 **Next Part**: [Function Inside Function →](./02_function_inside_function_py.ipynb)
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
````

### ✅ Output

```
Outer function
Inner function
```

---

## 🧭 Use Cases

* Structuring complex logic in **steps**.
* Creating **helper functions** that aren't visible outside.
* **Basis for decorators** (you'll see in later parts).

---

### 📂 Related File

[`02_function_inside_function.ipynb`](./02_function_inside_function.ipynb)

📌 **Next Part**: [Return Function →](./03_return_function.ipynb)

```
## 🟠 Part 3: Returning a Function (Closure)
Shows how to return an inner function, creating a **closure** that remembers outer variables.

✅ [Code](./03_return_function.ipynb)

This part shows how to **return** an inner function from an outer function.  
By returning the inner function, we create a **closure**.  

A **closure** is when the inner function *remembers* variables from its outer function even after the outer function has finished running.

---

### 💻 Example
```python
def outer():
    message = "Hello from outer!"

    def inner():
        print(message)

    return inner

# Create the closure
func = outer()
func()  # Output: Hello from outer!
```
✅ Output:
```python
Hello from outer!
```
📌 **Next Part**: [Basic_decorator_structure →](./04_basic_decorator_structure.ipynb)
