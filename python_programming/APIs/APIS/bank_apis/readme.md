
---
# learning with Awfera
# 🚀 Bank APIs – FastAPI Practice Project 

I created this **Bank API project** to practice and understand the **basics of FastAPI**, including:

* ✅ GET, POST, PUT, PATCH methods
* ✅ Routers for modular design
* ✅ Tags for automatic docs grouping

This is **not production code** — it’s meant as a simple educational example for myself and others learning FastAPI.

---

## 📁 Project Structure

```
/bank_apis
    main.py                          ✅ App entry point
    /readme.md                     ✅ Overview of the project
    /routers
        accounts.py                  ✅ Routes for account operations
        loans.py                     ✅ Routes for loan management
        withdrawals.py               ✅ Routes for withdrawals
        readme.md                    ✅ Notes about these routes
        __init__.py                  ✅ Makes routers a Python package
```

---

## ✅ Features Included

✨ **GET / POST / PUT / PATCH / DELETE**

* Practice of all main HTTP methods to handle banking operations.

✨ **Routers**

* Split routes into logical modules: accounts, loans, withdrawals.

✨ **Tags**

* Used to group endpoints in auto-generated docs (Swagger UI).

---

## ✅ Quick Start

1️⃣ Install dependencies:

```bash
pip install fastapi uvicorn
```

2️⃣ Run the server:

```bash
uvicorn bank_apis.main:app --reload
```

3️⃣ Open interactive docs:

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## ✅ Purpose

> This repo is for my own **basic understanding** of FastAPI. It’s a sandbox for:
>
> * Learning API design with clear routes
> * Experimenting with request validation
> * Structuring FastAPI projects with routers and tags

---

## 📌 Note

This project is purely for **educational purposes**. Feel free to fork it and adapt for your own learning!

---

