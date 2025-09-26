# Sigup and login Project

This is a basic Fullstack project built with a Python Flask backend and HTML/CSS/JavaScript for frontend.

## Technologies Used

-   **Backend**: Python(Flask)
-   **Frontend**: HTML, JavaScript,Css
-   **Database**: MySQL(Railway hosting server)
-   **Database Driver**: PyMySQL

## Setup Instructions

### 1. Backend Setup

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Database Setup

1.  **Make sure you have MySQL installed and running.**

2.  **Connect to MySQL and run the schema script:**
    -   You can use a MySQL client or the command line.
    -   Execute the contents of `mysql_schema.sql` to create the database and tables.
    ```sql
    CREATE DATABASE IF NOT EXISTS flask_app;

    USE flask_app;

    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        address VARCHAR(255) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        mobile VARCHAR(20) NOT NULL,
        password VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS files (
        id INT AUTO_INCREMENT PRIMARY KEY,
        filename VARCHAR(255) NOT NULL,
        filetype VARCHAR(50) NOT NULL,
        upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    ```

3.  **Configure the database connection:**
    -   Open `backend/config.py`.
    -   Update the `SQLALCHEMY_DATABASE_URI` to match your MySQL setup. The format is `mysql+pymysql://<user>:<password>@<host>/<database>`.
    -   Example: `SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flask_app'`

### 3. Running the Application

1.  **Run the Flask backend:**
    -   Make sure you are in the `backend` directory with the virtual environment activated.
    ```bash
    python app.py
    ```

2.  **Access the frontend:**
    -   Open your web browser and go to `http://127.0.0.1:5000/signup`.

### 4. Connecting to a Hosted Database (e.g., Railway)

If you are deploying this application to a hosting platform like Railway, you will need to connect it to a hosted database. Here’s how to configure it:

1.  **Create a MySQL Database on Your Hosting Platform:**
    -   In your hosting provider's dashboard (e.g., Railway), create a new MySQL database service.

2.  **Get the Database Connection URL:**
    -   Your hosting provider will give you a database connection URL (often called `DATABASE_URL`). It will look something like this:
        `mysql://<user>:<password>@<host>:<port>/<database>`

3.  **Set the Environment Variable:**
    -   In your hosting platform's settings for your application, create an environment variable named `DATABASE_URL` and paste the connection URL as its value.
    -   The application is already configured to read this environment variable, so it will automatically connect to your hosted database when deployed.

4.  **Update `config.py` for Production (Recommended):**
    -   The `config.py` file is designed to use the `DATABASE_URL` from the environment. To make it more robust for platforms like Railway, you can ensure it correctly formats the URL for SQLAlchemy.

    -   Modify your `backend/config.py` to look like this:
        ```python
        import os

        class Config:
            SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-secret-key'
            
            # Get the database URL from the environment
            DATABASE_URL = os.environ.get('DATABASE_URL')
            
            # If the URL is from a hosting provider, replace 'mysql://' with 'mysql+pymysql://'
            if DATABASE_URL and DATABASE_URL.startswith("mysql://"):
                DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)
            
            # Set the SQLAlchemy database URI
            SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'mysql+pymysql://root:password@localhost/flask_app'
            
            SQLALCHEMY_TRACK_MODIFICATIONS = False
            UPLOAD_FOLDER = 'uploads'
            ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
        ```
    -   This change ensures that your application will work seamlessly both locally and when deployed, without needing to change the code.

## Project Structure

```
project-root/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── uploads/
│   └── requirements.txt
│
├── frontend/
│   ├── signup.html
│   ├── login.html
│   ├── dashboard.html
│   └── static/
│       └── sample.pdf
│
├── mysql_schema.sql
└── README.md
```


