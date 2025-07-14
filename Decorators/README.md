# 🐍 Python Decorators: From Basic to Advance
 
Welcome! This repo is my learning journey through understanding Python decorators, broken into 10 clear, simple steps. 
---

## 📚 Table of Contents

| Part | Topic                          | Link                                              |
| ---- | ------------------------------ | ------------------------------------------------- |
| 1️⃣   | Functions Are Objects          | [01_functions_are_objects.ipynb](./01_functions_are_objects.ipynb) |
| 2️⃣   | Function Inside Function       | [02_function_inside_function.ipynb(./02_function_inside_function.ipynb) |
| 3️⃣   | Returning a Function           | [03_return_function.ipynb](./03_return_function.ipynb) |
| 4️⃣   | Basic Decorator Structure      | [04_basic_decorator_structure.ipynb](./04_basic_decorator_structure.ipynb) |
| 5️⃣   | Decorator @ Syntax             | [05_decorator_syntax.ipynb](./05_decorator_syntax.ipynb) |
| 6️⃣   | Decorators with Arguments      | [06_decorator_with_arguments.ipynb](./06_decorator_with_arguments.ipynb) |
| 7️⃣   | Real-life Example: Logging     | [07_logging_decorator.ipynb](./07_logging_decorator.ipynb) |
| 8️⃣   | Preserving Metadata with Wraps | [08_functools_wraps.ipynb](./08_functools_wraps.ipynb) |
| 9️⃣   | Decorators with Parameters     | [09_decorator_factory.ipynb](./09_decorator_factory.ipynb) |
| 🔟   | Advanced: Class-based Decorators| [10_class_based_decorator.ipynb](./10_class_based_decorator.ipynb) |

---

## 📌 About This Series

This repository is designed to help you understand Python decorators from scratch:

✅ Part 1–3: **Fundamentals of functions** (assign, pass, return, nested)  
✅ Part 4–6: **Basic to intermediate decorators**  
✅ Part 7–10: **Advanced patterns and best practices**  

---

## 📦 How to Use

1️⃣ Clone the repo  
```bash
git clone https://github.com/AshnaXhaikh/Learning-Journey/Decorators.git
cd decorators
```
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
