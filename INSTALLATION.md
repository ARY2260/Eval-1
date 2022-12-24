## Eval

# Installation Instructions For Website

1. Make sure you have Git, Python, and pip installed on your machine. If you don't have these tools installed, you can follow the instructions at the following links:

- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- Python: https://realpython.com/installing-python/
- pip: https://pip.pypa.io/en/stable/installing/

2. Clone the repository:

```bash
git clone https://github.com/MistaAsh/Eval.git
```

3. Navigate to the src directory:
```bash
cd Eval/src
```

4. Install the required Python packages:
```bash
pip install -r requirements.txt
```

5. Navigate to the chAI directory:
```bash
cd Eval/src/chAI
```

6. Migrate the database
```bash
python manage.py migrate
```

6. Run the server
```bash
python manage.py runserver
```

The server will now be running at http://localhost:8000/.
