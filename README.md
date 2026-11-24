# Day 14 – Coffee Machine

## Project Overview

This project is a command-line Coffee Machine simulation built using Python and Object-Oriented Programming (OOP).

The program simulates a coffee machine that allows users to order different drinks, checks whether enough ingredients are available, processes payments, calculates change, and prepares the selected coffee.

The machine offers three drinks:

- Latte
- Espresso
- Cappuccino

The project is divided into multiple Python files, with separate classes responsible for managing the menu, resources, and payments.

This project is part of my **100 Days of Python** learning journey.

## Features

- **Multiple Drinks:** Offers Latte, Espresso, and Cappuccino.
- **Resource Management:** Tracks the available quantity of water, milk, and coffee.
- **Resource Checking:** Checks whether enough ingredients are available before preparing a drink.
- **Coin Processing:** Accepts quarters, dimes, nickels, and pennies.
- **Payment Validation:** Checks whether the inserted money is sufficient.
- **Change Calculation:** Returns the remaining amount after successful payment.
- **Profit Tracking:** Tracks the total money earned by the coffee machine.
- **Coffee Preparation:** Deducts the required ingredients after a successful transaction.
- **Resource Report:** Displays the remaining ingredients.
- **Money Report:** Displays the total profit.
- **Machine Control:** Allows the machine to be turned off using the `off` command.

## Available Coffee Menu

| Drink | Water | Milk | Coffee | Price |
|---|---:|---:|---:|---:|
| Latte | 200 ml | 150 ml | 24 g | $2.50 |
| Espresso | 50 ml | 0 ml | 18 g | $1.50 |
| Cappuccino | 250 ml | 50 ml | 24 g | $3.00 |

## How the Program Works

### 1. Importing Classes

The main program imports classes from three separate Python modules.

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
```

- `Menu` manages the available drinks.
- `MenuItem` represents an individual drink.
- `CoffeeMaker` manages ingredients and coffee preparation.
- `MoneyMachine` handles payments and profit.

### 2. Creating Objects

The program creates objects from the imported classes.

```python
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
```

Each object is responsible for a different part of the coffee machine.

| Object | Responsibility |
|---|---|
| `coffe_maker` | Manages resources and prepares coffee |
| `money_machine` | Processes payments and tracks profit |
| `menu` | Provides available drinks and their details |

### 3. Creating the Main Loop

The program uses a `while` loop to keep the coffee machine running.

```python
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options})")
```

The loop continues until the user enters `off`.

The program also supports a `report` command to display the current resources and profit.

### 4. Managing the Menu

The `Menu` class stores the available drinks.

The `MenuItem` class represents each drink using its name, cost, and ingredients.

For example:

```python
MenuItem(
    name="latte",
    water=200,
    milk=150,
    coffee=24,
    cost=2.5
)
```

Each menu item stores its ingredients inside a dictionary.

The `get_items()` method returns the available drink names, while `find_drink()` searches for a drink based on the user's selection.

### 5. Checking Available Resources

Before preparing coffee, the program checks whether the machine has enough ingredients.

```python
if coffe_maker.is_resource_sufficient(drink):
```

The `is_resource_sufficient()` method compares the required ingredients with the available resources.

If an ingredient is insufficient, the machine displays a message and does not continue with the payment process.

### 6. Processing Payments

If enough resources are available, the program asks the user to insert coins.

```python
if money_machine.make_payment(drink.cost):
```

The `MoneyMachine` class handles the payment process.

It uses the following coin values:

| Coin | Value |
|---|---:|
| Quarter | $0.25 |
| Dime | $0.10 |
| Nickel | $0.05 |
| Penny | $0.01 |

The `process_coins()` method calculates the total amount inserted.

The `make_payment()` method then checks whether the received amount is enough to cover the drink's cost.

- If the payment is sufficient, the machine calculates the change and updates its profit.
- If the payment is insufficient, the transaction is rejected and the money is refunded.

### 7. Preparing Coffee

After successful payment, the program prepares the selected drink.

```python
coffe_maker.make_coffee(drink)
```

The `make_coffee()` method deducts the required ingredients from the machine's resources.

It then displays a message confirming that the coffee is ready.

### 8. Generating Reports

The machine supports a `report` command.

```python
coffe_maker.report()
money_machine.report()
```

The resource report displays the remaining water, milk, and coffee.

The money report displays the total profit earned by the machine.

### 9. Turning Off the Machine

The user can enter `off` to stop the program.

```python
if choice == "off":
    is_on = False
```

The Boolean variable `is_on` controls the main loop.

## Example Output

The following is an illustrative example based on the project logic.

```text
What would you like (latte/espresso/cappuccino/): latte

Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0

Here is $0.0 in change.
Here is your latte ☕️. Enjoy!

What would you like (latte/espresso/cappuccino/): report

Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like (latte/espresso/cappuccino/): off
```

## Object-Oriented Programming Concepts Used

| Concept | How It Is Used |
|---|---|
| Classes | Defines `CoffeeMaker`, `Menu`, `MenuItem`, and `MoneyMachine` |
| Objects | Creates separate objects to operate the coffee machine |
| Constructors | Uses `__init__()` to initialize object attributes |
| Instance Attributes | Stores resources, menu items, and profit |
| Methods | Defines actions such as `report()`, `make_coffee()`, and `make_payment()` |
| Encapsulation | Groups related data and methods inside classes |
| Object Interaction | Allows the main program to use methods from different objects |
| Dictionaries | Stores ingredients and coin values |
| Lists | Stores available menu items |
| Loops | Repeats the coffee machine's operations |
| Conditional Statements | Checks commands, resources, and payment status |
| Modules | Separates classes into different Python files |

## Project Structure

```text
Day-14-Coffee-Machine/
│
├── main.py              # Main program and order handling
├── coffee_maker.py      # Resource management and coffee preparation
├── menu.py              # Menu items, ingredients, and prices
├── money_machine.py     # Coin processing and payment management
└── README.md            # Project documentation
```

## How to Run the Project

### Prerequisites

- Python 3 installed on your system.
- VS Code, PyCharm, or another Python code editor.

### Steps

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd Day-14-Coffee-Machine
```

**3. Run the program**

```bash
python main.py
```

## What I Learned

Through this project, I practised:

- Understanding classes and objects in Python.
- Creating constructors using `__init__()`.
- Working with instance attributes and methods.
- Organizing a program into multiple Python modules.
- Making different objects interact with each other.
- Managing resources using dictionaries.
- Checking conditions before performing operations.
- Processing payments and calculating change.
- Understanding how Object-Oriented Programming helps organize larger applications.

## Learning Journey

**100 Days of Python – Day 14**

This project helped me understand how Object-Oriented Programming can be used to organize a larger Python application into separate classes, objects, and modules.