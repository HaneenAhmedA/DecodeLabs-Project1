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

<img width="1919" height="1020" alt="Screenshot 2026-05-25 002338" src="https://github.com/user-attachments/assets/8d05f4c4-c6c3-445b-b3af-f214c12f7313" />

<img width="457" height="530" alt="Screenshot 2026-05-25 004452" src="https://github.com/user-attachments/assets/a0280733-6cd0-4cee-847b-524d57d63b8c" />

<img width="456" height="541" alt="Screenshot 2026-05-25 004503" src="https://github.com/user-attachments/assets/cf662dcf-3db6-4227-a68d-865979ade4b3" />

<img width="457" height="535" alt="Screenshot 2026-05-25 004518" src="https://github.com/user-attachments/assets/2c7fa63b-4b45-4c31-a57c-eda006000c35" />

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
