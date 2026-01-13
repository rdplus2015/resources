# PostgreSQL Setup and Commands

## Installation

```bash
sudo apt install postgresql
```

## Start and Stop PostgreSQL Server Using the \`systemctl\` Command

```bash
sudo systemctl status postgresql   # Check the Status of PostgreSQL
sudo systemctl start postgresql    # Start the PostgreSQL Server
sudo systemctl stop postgresql     # Stop the PostgreSQL Server
```

## Connection

```bash
sudo su - postgres  # Switch to the `postgres` User on Linux
psql                # Connect to PostgreSQL (defaultDatabase and user)
psql -U superuser   # Connect to PostgreSQL (defaultDatabase)
psql -U postgres -d myDB # Connect to PostgreSQL with specific user and dataBase
```

## Integrating PostgreSQL with Django

1. **Create the database, user, set role Attributes and grant All Privileges on Database**:

   ```sql
      CREATE DATABASE mydatabase;                                                           -- Create a new Database.
      CREATE USER mydatabaseuser WITH ENCRYPTED PASSWORD 'mypassword';                      -- Create a User with Encrypted Password
      ALTER ROLE mydatabaseuser SET client_encoding TO 'utf8';                              -- Set the client encoding to 'utf8' for the user
      ALTER ROLE mydatabaseuser SET default_transaction_isolation TO 'read committed';      -- Set default transaction isolation
      ALTER ROLE mydatabaseuser SET timezone TO 'UTC';                                      -- Set the timezone to 'UTC' for the user
      GRANT ALL PRIVILEGES ON DATABASE mydatabase TO mydatabaseuser;                        -- Grant All Privileges on Database

      -- CREATE DATABASE <database name> WITH OWNER <user name>;
      -- ALTER DATABASE <database name> OWNER TO <user name>;`
   ```

2. **Install psycopg2**:

   ```bash
   sudo apt-get install libpq-dev # install the PostgreSQL development libraries on the system
   pip install psycopg2  # install in the .env
   pip install psycopg2-binary # This version doesn't require the development libraries
   ```

3. **Update Django settings** in \`settings.py\`:

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

4. **Run Django Migrations**:
   ```bash
   python manage.py migrate
   ```

### Others ccommands

```sh
\du                                 -- List Users
\dr                                 -- List Roles
\l                                  -- List All Databases
\c dbname                           -- Connect to a Database
\dt                                 -- List Tables in the Current Database
\d [tablename]                      -- Describe a Specific Table
python manage.py flush              -- removes all data from the database and resets the primary key sequences for all models.
python manage.py flush --no-input   -- bypasses the interactive confirmation step
```

```sql
CREATE USER superuser WITH PASSWORD 'securepassword' SUPERUSER;  -- Create superuser with password
ALTER USER mydatabaseuser WITH PASSWORD 'newpassword';           -- Change password for an existing user
ALTER ROLE superuser WITH CREATE ROLE;                           -- Grant ability to create roles
ALTER ROLE superuser WITH CREATE DB;                             -- Grant ability to create databases
ALTER ROLE superuser WITH REPLICATION;                           -- Grant replication rights
ALTER ROLE superuser WITH BYPASSRLS;                             -- Grant ability to bypass Row Level Security
REVOKE SELECT ON [tablename] FROM [username];                    -- Revoke Privileges
DROP DATABASE mydatabase;                                        -- Delete a database
DROP USER mydatabaseuser;                                        -- Delete a user
```

### Quit PostgreSQL Command Line Interface

```sh
\q
```

## Edit the pg_hba.conf File for Password Authentication

```bash
sudo nano /etc/postgresql/12/main/pg_hba.conf #(Note: The exact path may vary depending on the PostgreSQL version installed, e.g., 12 or 13.)
```

```sql
local   all             all                                     peer -- Find the local line for authentication and the peer method is the default and is the cause of the error you're seeing.
local   all             all                                     md5 -- Change peer to md5: Modify that line to use password authentication (md5), which will allow the superuser role to connect using a password:
```

```bash
sudo systemctl restart postgresql  # Restart the service
psql -U superuser -d postgre # Try to connect
```

### Notes

- peer: OK for pure local admin
- prod: md5 / scram-sha-256: required for backend in production
