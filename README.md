# Blood Donation Camp Management System

A simple Django+MySQL web application to manage blood donation camps. Users can register, search for blood, and admins can manage blood inventory.

## 📋 Features

- **User Registration & Login** - Create accounts and log in
- **Search Blood** - Find available blood by zone and type
- **Donor Profiles** - Manage your blood donor information
- **Blood Inventory** - Track blood stock by zone and blood type
- **Admin Dashboard** - Add/remove blood, manage users
- **Zone-based System** - Blood management for North and South zones

---

## 🛠️ What You Need (Prerequisites)

### Required Software

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Choose "Add Python to PATH" during installation

2. **MySQL Database** (Choose ONE option)
   - **Option A: XAMPP** (Easiest for beginners)
     - Download from: https://www.apachefriends.org/
     - Includes MySQL, Apache, and other tools
   
   - **Option B: MySQL Server Only**
     - Download from: https://dev.mysql.com/downloads/mysql/
     - For advanced users

3. **Git** (Optional, to download the project)
   - Download from: https://git-scm.com/

---

## 📥 Step 1: Download the Project

### Using Git (Recommended)
```bash
git clone <repository-url>
cd Blood-Donation-Camp
```

### Or Download as ZIP
1. Go to the GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal/PowerShell in the extracted folder

---

## 🔧 Step 2: Set Up MySQL Database

### Option A: Using XAMPP (Easiest)

**Windows:**
1. Install XAMPP from https://www.apachefriends.org/
2. Open XAMPP Control Panel
3. Click **Start** next to MySQL
4. Wait for it to show "Running" (green highlight)

**Mac/Linux:**
1. Install XAMPP
2. Open XAMPP and start MySQL from the dashboard

### Option B: Using MySQL Server Directly

**Windows:**
1. Install MySQL from https://dev.mysql.com/downloads/mysql/
2. During installation, set password to: `root` (or remember your password)
3. Make sure MySQL service is running

**Mac:**
```bash
brew install mysql
brew services start mysql
```

**Linux:**
```bash
sudo apt-get install mysql-server
sudo service mysql start
```

### Create the Database

Open a terminal/PowerShell and run:
```bash
mysql -u root -p
```

If using XAMPP, password is usually empty (just press Enter)

Then type:
```sql
CREATE DATABASE bloodbank;
EXIT;
```

---

## 🚀 Step 3: Install Python Dependencies

before you pip install make sure you to copy paste this line inside 'requirements.txt' file: 
'Django==4.2.8
mysqlclient==2.2.6
python-dotenv==1.0.0'
Open terminal/PowerShell in the project folder and run:

```bash
pip install -r requirements.txt
```

This will install:
- Django (web framework)
- mysqlclient (MySQL connection)
- python-dotenv (environment variables)

---

## 📝 Step 4: Create Configuration File

1. In the project folder, rename `.env.example` to `.env`
2. Open `.env` file and make sure it has these values:

```
DEBUG=True
SECRET_KEY=django-insecure-n4-on5fsw(1_lzj6ucp5@ltu^m0sko&#+iewemcwoa95)+oyq&
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=bloodbank
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

**Note:** If you set a custom MySQL password, replace the empty `DB_PASSWORD=` with your password

---

## 🗄️ Step 5: Set Up Database Tables

In terminal/PowerShell, run:

```bash
python manage.py migrate
```

This creates all necessary tables in the database.

---

## 👤 Step 6: Create Admin Account

Run this command:

```bash
python manage.py create_admin
```

This creates the admin account with:
- **Email:** admin@email.com
- **Password:** 123456

---

## 📊 Step 7: Create Sample Data (Optional)

To test the system with sample blood donors and inventory:

```bash
python manage.py create_sample_donors
python manage.py create_sample_blood_bank
```

This creates:
- 40 sample blood donors (5 for each blood type)
- Blood inventory for North and South zones

---

## ▶️ Step 8: Run the Application

Run this command:

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

**Note:** Port 8000 is Django's default. If port 8000 is already in use on your computer, use:
```bash
python manage.py runserver 8001
```
Then access the app at `http://127.0.0.1:8001/` instead.

---

## 🌐 Access the Application

Open your web browser and go to:

### User Pages
- **Home:** http://127.0.0.1:8000/
- **Register:** http://127.0.0.1:8000/register
- **Login:** http://127.0.0.1:8000/login
- **Search Blood:** http://127.0.0.1:8000/search
- **Blood Details:** http://127.0.0.1:8000/details

### Admin Panel
- **Admin Login:** http://127.0.0.1:8000/admin/
- **Admin Email:** admin@email.com
- **Admin Password:** 123456

**Note:** Replace `8000` with your port number if you used a different port in Step 8. For example, if you ran `python manage.py runserver 8001`, use `http://127.0.0.1:8001/` instead.

---

## 📂 Project Structure

```
Blood-Donation-Camp/
├── bloodbank/              # Main application
│   ├── migrations/         # Database changes
│   ├── models.py          # Database models
│   ├── views.py           # Application logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin panel setup
│   └── management/commands/  # Custom commands
│
├── cse370/                 # Django project settings
│   ├── settings.py        # Configuration
│   ├── urls.py            # Main URLs
│   ├── asgi.py            # ASGI config
│   └── wsgi.py            # WSGI config
│
├── templates/              # HTML files
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── blood_entry.html
│   ├── donate.html
│   ├── search.html
│   ├── blood_details.html
│   ├── user_list.html
│   └── dashboard.html
│
├── manage.py              # Django management
├── requirements.txt       # Python packages
├── .env.example          # Configuration template
├── .gitignore            # Git ignore rules
├── setup.bat             # Windows setup script
├── setup.sh              # Mac/Linux setup script
└── README.md             # This file
```

---

## 🔐 Admin Functions

Log in with admin account to:
- **Blood Entry** - Add blood to inventory
- **Blood Donation** - Remove blood from inventory
- **User List** - View and delete donors
- **Blood Details** - View blood inventory

---

## 🩸 Blood Types

The system supports these blood types:
- A+ (A Positive)
- A- (A Negative)
- B+ (B Positive)
- B- (B Negative)
- O+ (O Positive)
- O- (O Negative)
- AB+ (AB Positive)
- AB- (AB Negative)

---

## 🌍 Zones

The system has 2 zones:
- **North Zone**
- **South Zone**

---

## ❓ Troubleshooting

### MySQL Not Running
**Error:** "Can't connect to server on 'localhost'"

**Solution:**
- **XAMPP Users:** Open XAMPP Control Panel and click Start next to MySQL
- **MySQL Users:** Make sure MySQL service is running

### Port Already in Use
**Error:** "Port 3306 already in use"

**Solution:** Run on different port:
```bash
python manage.py runserver 8001
```

### Database Error
**Error:** "Unknown database 'bloodbank'"

**Solution:** Make sure you created the database:
```bash
mysql -u root -p
CREATE DATABASE bloodbank;
EXIT;
```

### Module Not Found
**Error:** "No module named 'django'"

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🛑 Stop the Server

Press `CTRL + C` in the terminal/PowerShell

---

## 📞 Support

If you face any issues:
1. Check the error message carefully
2. Make sure MySQL is running
3. Verify Python is installed correctly
4. Check if port 3306 (MySQL) and 8000 (Django) are available

---

## 📚 Tech Stack

- **Backend:** Django 4.2.8
- **Database:** MySQL (MariaDB 10.4+)
- **Frontend:** HTML, CSS
- **Language:** Python 3.8+

---

## ✅ Checklist Before Running

- [ ] Python 3.8+ installed
- [ ] MySQL installed and running
- [ ] Project downloaded
- [ ] `.env` file created
- [ ] `pip install -r requirements.txt` completed
- [ ] `python manage.py migrate` completed
- [ ] `python manage.py create_admin` completed
- [ ] Database `bloodbank` created

---

**Enjoy using Blood Donation Camp Management System!** 🩹❤️
