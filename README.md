# Caesar Cipher Encryption Tool 🔐

A Python implementation of the Caesar Cipher algorithm for educational purposes in cybersecurity.

## 📋 Project Overview

This project implements the Caesar Cipher, one of the simplest and oldest encryption techniques. It shifts each letter in the plaintext by a fixed number of positions down the alphabet.

**Created as part of:** Cybersecurity Internship Project  
**Author:** Bhavesh Pooniwala  
**Date:** November 2025

## ✨ Features

- ✅ Encrypt messages with custom shift values
- ✅ Decrypt messages when shift value is known
- ✅ Brute force decryption (tries all 26 possible shifts)
- ✅ Preserves case (uppercase/lowercase)
- ✅ Keeps special characters unchanged
- ✅ User-friendly command-line interface
- ✅ Input validation and error handling

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Development Environment:** Visual Studio Code
- **Version Control:** Git & GitHub

## 📦 Installation

### Prerequisites
- Python 3.x installed on your system
- Git (optional, for cloning)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/caesar-cipher.git
cd caesar-cipher
```

2. Or download directly:
- Download `caesar_cipher.py`
- Save it to your desired location

## 🚀 Usage

1. Run the program:
```bash
python caesar_cipher.py
```

2. Choose an option from the menu:
   - **1** - Encrypt a message
   - **2** - Decrypt a message
   - **3** - Brute force decrypt (try all shifts)
   - **4** - Exit

### Examples

**Encryption:**
```
Enter your message: Hello World
Enter shift value: 5
Encrypted Message: Mjqqt Btwqi
```

**Decryption:**
```
Enter your message: Mjqqt Btwqi
Enter shift value: 5
Decrypted Message: Hello World
```

**Brute Force:**
```
Enter your message: Mjqqt
[Shows all 26 possible decryptions]
```

## 🔍 How It Works

The Caesar Cipher works by shifting each letter by a fixed number of positions:

1. **Encryption:** Each letter is replaced by a letter some fixed number of positions down the alphabet
2. **Decryption:** Shift back by the same number of positions
3. **Formula:** 
   - Encryption: `E(x) = (x + shift) mod 26`
   - Decryption: `D(x) = (x - shift) mod 26`

### Example with shift = 3:
```
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

## 📚 Learning Outcomes

This project demonstrates understanding of:
- Basic cryptography concepts
- String manipulation in Python
- ASCII character encoding
- Modular arithmetic
- User input validation
- Function documentation
- Code organization

## 🤝 Contributing

This is an internship learning project. Suggestions and feedback are welcome!

## 📧 Contact

**[Your Name]**  
- Email: pooniwalabhavesh7680@gmail.com
- LinkedIn: https://www.linkedin.com/in/bhavesh-pooniwala
- GitHub: https://github.com/Bhaveshpooniwala1
