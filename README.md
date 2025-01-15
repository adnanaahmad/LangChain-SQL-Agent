# SQL Agent using LangChain

Follow these steps to set up and run the project:

## Prerequisites

Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

## Steps

### 1. Set Up a Virtual Environment

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```

### 2. Activate the Virtual Environment

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should see the virtual environment's name (e.g., `venv`) in your terminal prompt.

### 3. Install Dependencies

Install the required dependencies for the project by running:
```bash
pip install -r requirements.txt
```

### 4. Run the Database Setup Script

Run the script to set up the database:
```bash
python db_setup.py
```

### 5. Run the Main Agent Script

Start the application by running:
```bash
python agent.py
```

## Notes
- Make sure the database setup script (`db_setup.py`) is successful before running the agent script (`agent.py`).
- Keep the virtual environment activated while working on the project.
- If you encounter any issues, double-check the prerequisites and ensure all dependencies are installed.

