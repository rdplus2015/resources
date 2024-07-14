
# PostgreSQL Setup and Commands Cheat Sheet

## Installation

Ubuntu includes PostgreSQL by default. To install PostgreSQL on Ubuntu, use the apt (or other apt-driving) command:
```bash
sudo apt install postgresql
```

## Start and Stop PostgreSQL Server Using the \`systemctl\` Command

### Check the Status of PostgreSQL
```bash
sudo systemctl status postgresql
```

### Start the PostgreSQL Server
```bash
sudo systemctl start postgresql
```

### Stop the PostgreSQL Server
```bash
sudo systemctl stop postgresql
```

## Connection

### Switch to the \`postgres\` User on Linux
```bash
sudo su - postgres
```

### Connect to PostgreSQL
```sh
psql
```

### List Users
```sh
\du
```

### List Roles
```sh
\dr
```

### Connect to a Database
```sh
\c dbname
```

### List Tables in the Current Database
```sh
\dt
```

### Create a User with Encrypted Password
```sql
CREATE USER docuser WITH ENCRYPTED PASSWORD 'Pwd1010';
```

### Set Role Attributes
```sql
ALTER ROLE docuser SET client_encoding TO 'utf8';
ALTER ROLE docuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE docuser SET timezone TO 'UTC';
```

### Grant All Privileges on Database
```sql
GRANT ALL PRIVILEGES ON DATABASE mblog TO docuser;
```

### List All Databases
```sh
\l
```

### Connect to a Specific Database
```sh
\c [dbname]
```

### List All Tables
```sh
\dt
```

### Describe a Specific Table
```sh
\d [tablename]
```

### Grant Privileges
```sql
GRANT SELECT, INSERT ON [tablename] TO [username];
```

### Revoke Privileges
```sql
REVOKE SELECT ON [tablename] FROM [username];
```

### Quit PostgreSQL Command Line Interface
```sh
\q
```

## Integrating PostgreSQL with Django

1. **Install psycopg2**:
   ```bash
   pip install psycopg2
   ```

2. **Update Django settings** in \`settings.py\`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'mydatabaseuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',  # Set to 'localhost' or the IP address of your database server
           'PORT': '',           # Set to an empty string for the default port
       }
   }
   ```

3. **Create the database and user**:
   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER mydatabaseuser WITH PASSWORD 'mypassword';
   ALTER ROLE mydatabaseuser SET client_encoding TO 'utf8';
   ALTER ROLE mydatabaseuser SET default_transaction_isolation TO 'read committed';
   ALTER ROLE mydatabaseuser SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO mydatabaseuser;
   ```

4. **Run Django Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```