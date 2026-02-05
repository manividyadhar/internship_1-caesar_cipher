# 🔐 Caesar Cipher Encryption Tool

A Python-based implementation of the Caesar Cipher encryption technique. This project demonstrates encryption, decryption, and brute-force analysis while reinforcing fundamental cybersecurity concepts.

---

## 📌 Project Overview

The Caesar Cipher shifts alphabet characters by a fixed number of positions. This tool supports encryption, decryption, and brute-force decryption while preserving letter case and leaving symbols unchanged.

**Created as part of:** Cybersecurity Internship Project  
**Author:** Manividyadhar  
**Date:** November 2025  

---

## ✨ Features

- Encrypt text using a custom shift value  
- Decrypt text using a known shift value  
- Brute-force decryption for all 26 possible shifts  
- Preserves uppercase and lowercase letters  
- Symbols and numbers remain unchanged  
- Menu-based command-line interface  
- Input validation and error handling  

---

## 🛠 Technologies Used

- Programming Language: Python 3  
- Code Editor: Visual Studio Code  
- Version Control: Git and GitHub  

---

## 📥 Installation

### Prerequisites

- Python 3 installed  
- Git installed  

### Steps

Clone the repository:

git clone https://github.com/manividyadhar/internship_1-caesar_cipher.git
Navigate into the project directory:

cd internship_1-caesar_cipher


Run the program:

python caesar_cipher.py

🚀 Usage
Menu Options
1. Encrypt a message
2. Decrypt a message
3. Brute force decrypt
4. Exit

🧪 Examples
Encryption Example

Input:

Message: Hello World
Shift: 5


Output:

Encrypted Message: Mjqqt Btwqi

Decryption Example

Input:

Message: Mjqqt Btwqi
Shift: 5


Output:

Decrypted Message: Hello World

⚙️ How It Works

Each letter is converted to its numeric position

The shift value is applied

Modulo 26 ensures characters remain within alphabet range

Encryption Formula:

E(x) = (x + shift) mod 26


Decryption Formula:

D(x) = (x - shift) mod 26

🎓 Learning Outcomes

Cryptography fundamentals

Python string manipulation

Modular arithmetic

Command-line application development

Secure coding practices

👤 Author Information

Name: Manividyadhar
Email: manividyadhar143@gmail.com

GitHub: https://github.com/manividyadhar

LinkedIn: https://www.linkedin.com/in/manividyadhar/
