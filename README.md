# Bloodbank Management System
***
A Blood Bank Management System
---

---

Steps to run the project:
1. Clone the project.
---
2. If using Conda:
    Prerequisites:
  * Conda
  * MySQL Server
  * Any latest Web Browser

  1. Open Conda Command Prompt.
  2. cd into BMS\BMS\
  3. Create the project env and install dependencies: ``` conda env create -f dbms2.yml ```
  4. Activate the env: ```activate dbms2```
  
3. If using Pip:
    Prerequisites:
  * Pip,Python 3.7+
  * MySQL Server
  * Any latest Web Browser

  1. Open cmd.
  2. cd into BMS\
  3. Create a env called 'bbms': ``` python3 -m venv dbms2 ```
  4. Activate the env: ``` source dbms2/bin/activate ```
  5. cd into BMS\
  6. Install the dependencies: ``` pip install -r requirements.txt ```
---
4. After the steps of either #2 or #3:
  1. Login to the MySQL shell.
  2. Create a new database user with this exact code given: ``` GRANT ALL PRIVILEGES ON *.* TO 'dbmsuser'@'localhost' IDENTIFIED BY 'dbmspassword'; ```
  3. Log out of MySQL by typing: ``` \q ```
  4. Log in as the new database user you just created: ``` mysql -u dbmsuser -p ```
  5. Type the new database user’s password and press Enter.
  6. Create a new database named 'bms': ``` CREATE DATABASE bms; ```
  
5. Now, in the conda shell or cmd:
  1. cd into BMS\BMS\.
  2. Run: ``` python manage.py makemigrations ```
  3. Run: ``` python manage.py migrate ```
  4. Run: ``` python manage.py createsuperuser ```
  5. Enter the username and password of new django superuser. 
  6. Run: ``` python manage.py runserver ```
  
6. Now, open your preferred web browser:
  1. Go to http://127.0.0.1:8000
  2. Click the login button at the top.
  3. The login page appears. It is the unified login page for both Admin and Doctors. Entering the Admin credentials will take you to the Admin portal while entering the doctor credentials will take one to the Doctor portal.
  4. Enter the Django superuser credentials(#5.5) to login as the Admin and use is to add/edit/delete hospitals, approve newly registered Doctors, approve Donations and Blood Requests, edit/delete existing Doctors, see the details of all Donors, Patients and current Blood Stock.
  5. Or click the SignUp button in the homepage and register a new Doctor. 
  6. Login as a Doctor to add/edit/delete your Donors and Patients, apply for donation, request for blood, track, cancel your requests.
