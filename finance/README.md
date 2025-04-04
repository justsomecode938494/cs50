# Finance

This directory contains the code and resources for the Finance project. The project is part of the `cs50` repository.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Finance project is a web-based application that allows users to simulate stock trading. Users can buy and sell stocks, view their portfolio, and track their transactions.

## Features
- User registration and authentication
- Buy and sell stocks
- View portfolio and transaction history
- Real-time stock quotes

## Installation
To install and run this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/justsomecode938494/cs50.git
    ```

2. Navigate to the `finance` directory:
    ```sh
    cd cs50/finance
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:
    ```sh
    flask run
    ```

## Usage
To start using the application, follow these steps:

1. Open your web browser and go to the local server URL (e.g., `http://127.0.0.1:5000`).

2. Register for a new account or log in with your existing account.

3. Use the application to buy and sell stocks, view your portfolio, and track your transactions.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch with your feature or bugfix.
3. Commit your changes.
4. Push the branch to your fork.
5. Create a pull request.


