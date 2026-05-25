# 🔐 Project 1 — Password Strength Checker

**DecodeLabs Cybersecurity Internship | Batch 2026**

---

## 📌 About
A Python program that evaluates whether a password is **Weak**, **Medium**, or **Strong** based on security criteria. Built as Project 1 of the DecodeLabs Industrial Training Kit.

---

## ✅ Features
- Checks password length (minimum 8 characters)
- Detects uppercase letters, digits, and symbols
- Classifies strength as Weak / Medium / Strong
- Leaked password detection (common passwords list)
- Timing-safe comparison using `hmac.compare_digest()`
- CLI version + full PyQt5 desktop GUI

---

## 🖥️ GUI Preview
> Live strength bar, color-coded criteria checklist, and Show/Hide password toggle.

![GUI Screenshot](Screenshot%202026-05-25%20002338.png)

---

## 📁 Files
| File | Description |
|------|-------------|
| `password_checker.py` | CLI version |
| `password_checker_gui.py` | PyQt5 GUI version |

---

## ▶️ How to Run

**CLI:**
```bash
python password_checker.py
```

**GUI:**
```bash
pip install PyQt5
python password_checker_gui.py
```

---

## 🧠 Concepts Used
- String handling & conditional logic
- Pythonic `any()` with generator expressions — O(n) linear scan
- `hmac.compare_digest()` for timing-attack prevention
- Entropy & password policy (length, character variety)

---

## 🛠️ Built With
- Python 3
- PyQt5

---

*DecodeLabs Industrial Training Kit — Batch 2026*
