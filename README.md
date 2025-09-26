# Full-Stack Web Application

This is a full-stack web application with a Python Flask backend and a simple HTML/CSS/JavaScript frontend.

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

