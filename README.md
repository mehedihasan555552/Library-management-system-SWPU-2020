# Library Management System

A comprehensive Django application designed to manage library operations with distinct roles for administrators and operators, enabling full Create, Read, Update, Delete (CRUD) functionalities on library inventory and user data.

## Features

- **Role-Based Access Control**: Differentiates between admin and operator roles, each with specific permissions and access levels.
- **CRUD Operations**: Allows administrators and operators to perform Create, Read, Update, and Delete operations on books, users, and transactions.
- **User Management**: Admins can manage user accounts, assign roles, and monitor activity.
- **Inventory Management**: Operators can add, update, and remove books from the library inventory.
- **Transaction Tracking**: Keeps records of book checkouts, returns, and overdue items.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default), configurable to PostgreSQL or MySQL
- **Authentication**: Django's built-in authentication system
- **Admin Interface**: Django Admin Panel for backend management

## Getting Started

### Prerequisites

- Python 3.6+
- Django 3.2+
- SQLite (default) or PostgreSQL/MySQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mehedihasan555552/Library-management-system-SWPU-2020.git
   cd Library-management-system-SWPU-2020
