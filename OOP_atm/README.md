# 🏧 OOP ATM System

A simple command-line ATM application built with **Python** using **Object-Oriented Programming (OOP)** principles.

This project simulates the basic operations of an Automated Teller Machine (ATM), allowing users to register, log in securely with a PIN, and perform common banking operations.

---

## ✨ Features

- 👤 User Registration
- 🔐 Secure PIN Login
- 💰 Deposit Money
- 💸 Withdraw Money
- 🔄 Transfer Funds
- 📊 Check Account Balance
- 📝 Transaction History
- 💾 Persistent User Storage using text files
- 📂 Modular project structure

---

## 📁 Project Structure

```
OOP_ATM/
│
├── main.py              # Application entry point
├── auth.py              # Registration and login
├── bank_account.py      # BankAccount class
├── storage.py           # Save and load users
├── users_atm.txt        # User database
└── README.md
```

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (Classes & Objects)
- File Handling
- Exception Handling
- Datetime Module
- Modular Programming

---

## 🧠 OOP Concepts Practiced

This project demonstrates several core Object-Oriented Programming concepts, including:

- Classes
- Objects
- Constructors (`__init__`)
- Instance Attributes
- Instance Methods
- Encapsulation
- Modular Design

---

## 📌 How It Works

### Register

A new user provides:

- Username
- PIN
- Initial Balance

The information is stored in `users_atm.txt`.

---

### Login

Existing users enter:

- Username
- PIN

If authentication succeeds, they gain access to the ATM menu.

---

### ATM Menu

```
1. Deposit
2. Withdraw
3. Transfer
4. Check Balance
5. Transaction History
6. Display Owner
7. Exit
```

---

## 📂 Data Storage

User accounts are stored in a text file in the following format:

```
username,pin,balance
```

Example:

```
ekene,1234,5000
john,4321,2500

---

## 📖 Learning Goals

This project was built to practice:

- Writing clean Python code
- Organizing programs into multiple modules
- Designing reusable classes
- Building command-line applications
- Applying Object-Oriented Programming principles
- Working with persistent data using files

---

## 🔮 Future Improvements

Planned features include:

- Save transaction history to file
- Multiple bank accounts
- Change PIN
- Delete account
- Account lock after multiple failed login attempts
- Password hashing for improved security
- Beneficiary management
- Transfer between registered users
- Admin dashboard
- SQLite database integration
- Graphical User Interface (Tkinter or CustomTkinter)

---

## 👨‍💻 Author

**Ekene Godswill**

Aspiring Software Engineer | Ethical Hacker | Builder

GitHub: https://github.com/Godswill-Ekene

---

## 📜 License

This project is created for educational purposes and personal learning.