# FastAPI-Postgresql

# Diabetes-Classification

## Getting Started

### 1. Cloning the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/BioDani/FastAPI-Postgresql.git
 cd FastAPI-Postgresql
```

### 2. Virtual environment

Create a environment

```bash
python3 -m venv .venv --prompt envbackFastAPI
```

Activate the environment

```bash
source .venv/bin/activate
```

Deactivate the environment

```bash
deactivate
```

### 3. Package management

Install packages listed in the file `requirements.txt`.

```bash
python3 -m pip install -r requirements.txt
```

Save installed packages inside the file `requirements.txt`.

```bash
python3 -m pip freeze > requirements.txt   
```

FASTAPI-POSGRESQL
├── app  # Contains the main application files.
│   ├── __init__.py   # this file makes "app" a "Python package"
│   ├── main.py       # Initializes the FastAPI application.
│   ├── dependencies.py # Defines dependencies used by the routers
│   ├── routers
│   │   ├── __init__.py
│   │   ├── items.py  # Defines routes and endpoints related to items.
│   │   └── users.py  # Defines routes and endpoints related to users.
│   ├── crud
│   │   ├── __init__.py
│   │   ├── item.py  # Defines CRUD operations for items.
│   │   └── user.py  # Defines CRUD operations for users.
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── item.py  # Defines schemas for items.
│   │   └── user.py  # Defines schemas for users.
│   ├── models
│   │   ├── __init__.py
│   │   ├── item.py  # Defines database models for items.
│   │   └── user.py  # Defines database models for users.
│   ├── external_services
│   │   ├── __init__.py
│   │   ├── email.py          # Defines functions for sending emails.
│   │   └── notification.py   # Defines functions for sending notifications
│   └── utils
│       ├── __init__.py
│       ├── authentication.py  # Defines functions for authentication.
│       └── validation.py      # Defines functions for validation.
├── tests
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_items.py  # Tests for the items module.
│   └── test_users.py  # Tests for the users module.
├── requirements.txt
├── .gitignore
└── README.md