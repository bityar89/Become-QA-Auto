# FirstStepsInAutomation

Educational project for QA automation using **Python**, **Selenium**, and **Pytest**.  
This project demonstrates how to structure automated UI tests, use fixtures, and interact with a local database.

## 💻 Prerequisites

- Python 3.11+
- Google Chrome (or another supported browser)
- ChromeDriver (compatible with your browser version)

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

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```


 
3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Run tests:
```bash
pytest -v  
```

## 🛠 Technologies

- Python 3.11.4  
- Selenium 4.35.0  
- Pytest 8.4.1  

## 📌 Notes

- Add a `.gitignore` file to exclude `__pycache__/`, virtual environments, `.idea/`, `.vscode/`, and other unnecessary items.  
- GitHub Actions can be configured later to run tests automatically on each push.

📖 Usage Tips
- Organize your tests by feature or page in the `tests/` folder.
- Use fixtures in `conftest.py` for reusable setup like browser initialization.
- Keep helper functions in `modules/` to avoid duplication.

🤝 Contributing
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Write tests and make changes
4. Submit a pull request

## 🔗 Useful Links

- [Python Documentation](https://docs.python.org/3/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)

