# FirstStepsInAutomation

Educational project for QA automation using **Python**, **Selenium**, and **Pytest**.

## 📂 Project structure

- `modules/` — helper modules and business logic  
- `tests/` — UI and other tests  
- `conftest.py` — Pytest configuration (fixtures, driver setup, etc.)  
- `pytest.ini` — Pytest settings  
- `become_qa_auto.db` — local database used in the project  

## 🚀 Installation and run

1. Clone the repository:
   ```bash
   git clone https://github.com/bityar89/FirstStepsInAutomation.git
   cd FirstStepsInAutomation
   ```
   
2. (Optional but recommended) Create a virtual environment:
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
 
3. Install dependencies:
   pip install -r requirements.txt  

4. Run tests:
   pytest -v  

## 🛠 Technologies

- Python 3.11.4  
- Selenium 4.35.0  
- Pytest 8.4.1  

## 📌 Notes

- Add a `.gitignore` file to exclude `__pycache__/`, virtual environments, `.idea/`, `.vscode/`, database files, and other unnecessary items.  
- GitHub Actions can be configured later to run tests automatically on each push.  
