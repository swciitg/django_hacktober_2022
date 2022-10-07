# Getting started
1. Create a [Virtual Environment](#how-to-create-a-virtual-environment)
2. cd to project_folder and install requirements - `pip install -r ./requirements.txt`
3. Start **django server** -  `python manage.py runserver`

### Django best practices
- Model naming
> Models represent a single object or entity so model names should be a singular noun.
- Follow coding style recommeded by [pep8](https://peps.python.org/pep-0008/)
- Using [Virtual Environments](#how-to-create-a-virtual-environment)
- Updating `requirements.txt` file, after installing any new package 

> References: [django-best-practices](https://django-best-practices.readthedocs.io/en/latest/), [GfG article - django Best Practices](https://www.geeksforgeeks.org/best-practices-for-professional-developer-django-framework/) 

### Django commands
- [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/custom-django-management-commands/)
- [https://www.askpython.com](https://www.askpython.com/django/django-commands)
### How to create a virtual environment?
> Why? To avoid installing Python packages globally which could break system tools or other projects

- install `virtualenv`
```bash
# windows
pip install virtualenv

# Linux
pip3 install virtualenv
```

- Create virtual environment
```bash
virtualenv <env-name>
# OR
python -m venv <env-name>
```

- Activate environment
```bash
# Windows
./<env-name>/Scripts/activate

# Linux/Mac
source ./<env-name>/bin/activate
```

- Install requirements
```bash
# Windows
pip install -r ./requirements.txt

# Linux/Mac
pip3 install -r ./requirements.txt
```
- List all installed packages in current environment
```bash
pip list
# OR 
pip freeze

# to store packages in requirements.txt
pip freeze > requirements.txt
```