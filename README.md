# ST-SMS-Backend using Django REST API

Django REST Framework for Select Therapy Institute Student Management System

**To clone the repo for dev purpose, please do the following (with empty database, sometime down the line, I will also export the db data file to be imported):**

## Requirements:

1. Python Version 3.9.6
2. Postgresql Version 12

---

### **Download and install Python3.9 ( linux-RH based ) [Python3.9.6 Source](https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tar.xz)**

**Using Linux**

_Please note that in this example we are using RPM based install (Fedora to be more exact), if using a different distro, please look up installation commands and dependency packages specific to that distro._

1. `$ sudo yum -y update`
2. `$ cd /tmp && wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tar.xz`
3. `$ sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel`
4. `$ tar xf /tmp/Python-3.9.6.tar.xz`
5. `$ cd Python-3.9.6`
6. `$ sudo ./configure --enable-optimizations`
7. `$ sudo make altinstall`
8. `$ cd ../ && rm Python-3.9.6.tar.xz`
9. `$ python3.9 -V` (should output Ptyhon 3.9.6)

#### **Download and install Python3.9 [Win Installer](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)**

#### **Download and install Python3.9 [Mac Installer](https://www.python.org/ftp/python/3.9.6/python-3.9.6-macosx10.9.pkg)**

---

### **Download and install postgresql12 and management software**

1. `sudo dnf update -y`
2. `$ sudo dnf install https://download.postgresql.org/pub/repos/yum/reporpms/F-33-x86_64/pgdg-fedora-repo-latest.noarch.rpm`
3. `$ sudo dnf install postgresql12-server postgresql12`
4. `$ /usr/pg-sql-12/bin/postgresql-12-setup initdb`
5. `$ sudo systemctl start postgresql-12`
6. `$ sudo vim /var/lib/pgsql/12/data/pg_hba.conf`
7. Start pgadmin4 and connect to localhost:5432 where postgresql-12 is running, add a new database named **dev** (if database file available, skip adding the database dev and just import .sql file instead)

```Bash
# change auth method from ident to md5

# Accept from anywhere on port 5432
host all all 0.0.0.0/0 md5

```

8. `$ sudo systemctl restart postgresql-12`
9. `$ sudo su - postgres`
10. `$ psql -c "alter user postgres with password '[your-password, ie: dev]'"`
11. `$ sudo yum -y install epel-release`
12. `$ sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm`
13. `sudo yum -y update`
14. `$ sudo yum -y install pgadmin4`
15. `$ sudo dnf install https://download.postgresql.org/pub/repos/yum/reporpms/F-33-x86_64/pgdg-fedora-repo-latest.noarch.rpm`
16. `$ sudo dnf -y install pgadmin4-desktop`

#### **Download and install postgresql12 and management software [Win Installer](https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=48)**

#### **Download and install postgresql12 and management software [Mac Installer](https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=47)**

15. Once installed, please log into pgadmin4, and create database name: dev

---

### **Clone from Github**

1. `$ cd ~/ && mkdir ST-SMS && cd ST-SMS`
2. `$ git clone https://github.com/0x5929/ST-SMS-Backend.git`

_Note:_ If having trouble to pull/clone, please see : [clone using personal token](https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to)

---

### **Start virtual environment and install dependencies**

1. `$ cd ST-SMS-Backend`
2. `$ python3.9 -m venv virtual-env`
3. `$ source virtual-env/bin/activate`
4. `$ pip -V` (should output 3.9)
5. `$ pip install -r requirements.txt`

_Note:_ If having trouble to install postgres db connector, try: `$ PATH="<postgres-installation-path>/bin/:$PATH" pip install -r requirements.txt`

for my fedora system, the path is : `/usr/pgsql-12/bin/`
---

### **Add in the st-sms-creds.json file**
1. This file is used for Google API access, needs to be there or SMS endpoints will fail
2. This file is only stored locally in repo owner's drive, for security reasons
3. For a new project, one can create such file by following the first eight steps in this [guide](https://robocorp.com/docs/development-guide/google-sheets/interacting-with-google-sheets)
4. *Explanation* To elaborate on point 1, this file is used to access Google API, more specifically to mirror data from postgres db to Google Sheets (For school, BPPE compliance reasons)


### **Edit `core/settings/.env-template` file**

1. Using your fav text editor to edit `/ST-SMS-Backend/core/settings/.env-template` file
2. Rename the file to `.<dev|test|prod>-env` so it can be picked up by django
  - In dev environment, `manage.py` picks up the settings config
  - In prod environment, `wgsi.py` or `agsi.py` will point towards the setting file desired. 

_Note:_ To generate a new secret key: `$ python manage.py shell`

```Python

>>> from django.core.management.utils import get_random_secret_key
>>> a = get_random_secret_key()
>>> a
>>> a
'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
>>>
```

---

### **Migrate and add superuser; then start server (If starting with a blank Database)**

1. `$ python manage.py makemigrations --dry-run`
2. `$ python manage.py makemigrations`
3. `$ python manage.py migrate`
4. `$ python manage.py createsuperuser`
5. `$ python manage.py loaddata fixtures/all-inital-data.json`
6. `$ python manage.py runserver`

_Note:_ If encountered errors where library images not found. You may need to symbolic link libraries from `/postgresql/installation/path/lib/<lib-missing>` to `/usr/local/lib`. More info, see: [psycopg2-image-not-found](https://stackoverflow.com/questions/16407995/psycopg2-image-not-found)

---


### **Import existing data from Google Sheets**
1. dump data from google using by calling the following API (needs to have superuser access)

  - `curl -X POST -H "Content-Type: application/json"  -d "{\"email\": \"root@localhost\", \"password\": \"you-password\"}" http://127.0.0.1:8000/auth/login/`

  - Remember to add the authentication token from the response in the next request
  - `curl -H "Authorization Bearer {access_token}" http://127.0.0.1:8000/api/sms/google_sheet_datadump/?ssid=<spreadsheet id>&sid=<sheet id>&school_name=<school name value, ie: STI>`

2. Save the JSON response into a file
3. `$ python manage.py loaddata <dump-file.json>`
4.  `$ python manage.py makemigrations --dry-run` under normal circumstances, there are no migration changes

**note that these steps should be done in both dev and prod environments to have a ready Database**

---


*If server started in dev by `$ python manage.py runserver`, it will live on http://localhost:8000*

*If server started in prod, make sure check `wsgi.py` file so it points to prod settings, refer to hosting agent.*

Change 11