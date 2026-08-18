# Playwright With Python E-Commerce Test Automation Project

[![E2E Tests](https://github.com/Bob160/saucedemo-autotest/actions/workflows/playwright.yml/badge.svg)](https://github.com/Bob160/saucedemo-autotest/actions)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)](https://playwright.dev/python/)
[![Framework](https://img.shields.io/badge/Design%20Pattern-Page%20Object%20Model-orange.svg)]()

A modular End-to-End (E2E) UI test automation framework built with **Python**, **Playwright**, and **Pytest**, managed using **uv** and fully integrated with **GitHub Actions** CI/CD. This suite automates key user journeys—including authentication, cart manipulation, and checkout flows—on the [Sauce Demo](https://www.saucedemo.com) e-commerce application.

---

## Key Architecture & Features

* **Page Object Model (POM):** Decouples test logic from page-specific locators and UI interactions for maintainability.
* **CI/CD Pipeline:** Automated build execution via GitHub Actions on every push and pull request.
* **Automated Failure Artifacts:** Hooks capture full-page screenshots and output execution reports stored in `reports/`.
* **Implicit Synchronization:** Leverages Playwright’s native auto-waiting mechanisms to eliminate flaky hardcoded sleeps.
* **Modular Fixtures:** Reusable Pytest fixtures handle browser lifecycle, page context initialization, and dependency injection.
* **Modern Tooling:** Uses `uv` for fast dependency locking (`uv.lock`) alongside standard `pyproject.toml` and `pytest.ini` configurations.

---
# Project Overview

This automation project was developed to  demonstrate:

* UI test automation
* Playwright with Python
* Browser automation
* End-to-end testing
* Page Object Model architecture
* Real-world application test scenarios

The demo application used for testing is:

https://www.saucedemo.com

---

## Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Automation Engine** | Playwright for Python |
| **Test Runner** | Pytest |
| **Dependency Manager** | `uv`|
| **CI/CD Pipeline** | GitHub Actions |
| **Design Pattern** | Page Object Model (POM) |
| **Target Application** | Sauce Demo (`https://www.saucedemo.com`) |

---

## Project Structure

```text
saucedemo-tests/
├── .github/
│   └── workflows/          # GitHub Actions workflow specifications
├── pages/                  # Page Object classes (Locators & Actions)
│   ├── add_to_cart.py
│   ├── checkout.py
│   ├── continue_shopping.py
│   ├── fill_checkout_form.py
│   ├── login_page.py
│   ├── remove_from_cart.py
│   └── view_cart.py
├── reports/                # Test execution outputs and failure screenshots
├── tests/                  # Pytest test modules
│   ├── __init__.py
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│   ├── test_continue_shopping.py
│   ├── test_fill_checkout_form.py
│   ├── test_login_test.py
│   ├── test_remove_from_cart.py
│   └── test_view_cart.py
├── .env                    # Local environment variables
├── .gitignore
├── .python-version
├── config.py               # Global configuration setup
├── conftest.py             # Pytest fixtures and screenshot execution hooks
├── pyproject.toml          # Project dependencies and tool settings
├── pytest.ini              # Pytest CLI flags and defaults
├── uv.lock                 # Locked dependency versioning file
└── README.md
```
---

# Test Scenarios Covered

## Authentication Tests

* Successful login
* Invalid login
* Empty username
* Empty password

## Inventory Tests

* Verify inventory page loads
* Add product to cart

## Cart Tests

* Verify item added to cart
* Verify cart contents

## Checkout Tests

* Complete checkout process
* Verify successful order placement

---


## CI/CD Pipeline

*Triggers: Automatically executes on push and pull_request events targeting main branches.

*Artifacts: Generates video and HTML test execution reports and embeds failure screenshots, downloadable from the GitHub Actions run summary.

# Installation

##Prerequisites
*Python 3.10+

*uv (recommended) or standard pip

## Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## Navigate to Project Directory

```bash
cd ecommerce_playwright
```

## Install Dependencies

Using uv
```bash
uv sync
uv run playwright install
```

## Install Playwright Browsers

```bash
playwright install
```

---

# Running the Tests

Run all tests:

```bash
uv run pytest tests
```

Run a particular tests:

```bash
uv run pytest tests/[file]
```

---

# Sample Test Credentials

```text
Username: standard_user
Password: secret_sauce
```

---

# Future Improvements

Planned enhancements include:

* Data-driven testing
* Parallel test execution
* Cross-browser testing

---

# Author

Efio-esien Efiom

QA Engineer | Software Tester

---

# Useful Resources

Playwright Documentation:
https://playwright.dev/python/docs/intro

Python Documentation:
https://www.python.org/doc/

Sauce Demo Website:
https://www.saucedemo.com

