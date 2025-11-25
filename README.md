# 📘 Profit and Loss Appropriation Account

## 📌 Description

**Profit and Loss Appropriation Account** is used by **Partnership Firms** to allocate and distribute:

* Net Profit among partners and reserves, or
* Net Loss among partners

This project automates the process using:

* **Python** (frontend + calculations)
* **MySQL** (backend storage)

It supports: <br>
✔ Inserting records <br>
✔ Displaying records <br>
✔ Updating records <br>
✔ Deleting records <br>
✔ Generating the Profit & Loss Appropriation calculations based on user inputs

---

# 🚀 Features

### 🔹 1. **Basic Details Input**

Prompts the user for firm details:

* Firm name
* Accounting year
* Number of partners
* Profit-sharing ratio
* Capital, drawings, interest calculations

### 🔹 2. **MySQL Database Integration**

The program:

* Creates database `project`
* Creates table `account`
* Inserts user-input data
* Retrieves and displays data in formatted tables (using `tabulate`)

### 🔹 3. **CRUD Operations**

| Operation | Description                         |
| --------- | ----------------------------------- |
| Insert    | Adds new partner-appropriation data |
| Display   | Shows data using Python + MySQL     |
| Update    | Modifies existing records           |
| Delete    | Removes selected records            |

---

# 🛠️ Requirements

To run this project, users must have:

### ✔ Python (3.x recommended)

Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### ✔ MySQL Server

Download from: [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)

### ✔ Required Python Modules

Install using pip:

```
pip install mysql-connector-python
pip install tabulate
```

---

# 📦 Installation & Setup

1. **Clone the repository**

   ```
   git clone https://github.com/JaysreeSS/profitnloss_appropriation_account.git
   cd profitnloss_appropriation_account
   ```

2. **Install required Python packages**

   ```
   pip install -r requirements.txt
   ```

   (Or install manually using the commands listed above.)

3. **Ensure MySQL is running on your system**

4. **Create/verify MySQL user**
   Your script uses:

   ```
   host='localhost'
   username='root'
   password='password'
   ```

   Make sure your MySQL root account uses the same credentials.
   (You may modify them in the script if needed.)

5. **Run the program**

   ```
   python main.py
   ```
