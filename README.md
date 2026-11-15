# SauceDemo UI Test Automation

A beginner QA Automation project built using Python, Playwright and pytest.

This project automates user interface testing on the SauceDemo practice shopping website.

## Project Overview

The purpose of this project is to test important functionalities of an online shopping application, including user login and shopping cart operations.

## Test Cases

### 1. Login Tests

- Verify successful login with valid credentials.
- Verify login failure with an incorrect password.
- Verify validation when the username is empty.
- Verify validation when the password is empty.
- Verify that a locked-out user cannot log in.

### 2. Shopping Cart Tests

- Verify that one product can be added to the cart.
- Verify that two products can be added to the cart.
- Verify that a product can be removed from the cart.

## Technologies Used

- Python
- Playwright
- pytest
- Git
- GitHub

## Project Structure

```text
qa-automation/
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_cart.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone this repository.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Install Playwright browsers:

```bash
playwright install
```

## Running the Tests

Run all tests:

```bash
pytest
```

Run tests with the browser visible:

```bash
pytest --headed
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

## Author

Computer Science Student | Aspiring QA Automation Engineer

