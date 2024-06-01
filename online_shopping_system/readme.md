# Shopping Cart Management

This Python code provides a simple implementation of a shopping cart management system using object-oriented programming principles. It defines two classes: `User` and `Customer`.

## User Class

The `User` class is a basic class that stores user information such as username and email.

## Customer Class

The `Customer` class inherits from the `User` class and provides additional functionality for managing products in a shopping cart. It has the following methods:

### `add_product(cart_item: List[Dict[str, int | Any]])`

This method allows customers to add products to their shopping cart. It takes a list of dictionaries as input, where each dictionary represents a product with its name and price.

### `remove_product(cart_item: List[Dict[str, int | Any]])`

This method allows customers to remove products from their shopping cart. It takes a list of dictionaries as input, where each dictionary represents a product with its name and price to be removed.

### `view_cart()`

This method returns a JSON-formatted string representing the customer's shopping cart, including the user's name, email, and the products in their cart.

### `save_cart(filename, extension: Optional[str] = ".txt")`

This method saves the customer's shopping cart to a file. The file name and extension can be specified as arguments. If no extension is provided, the default extension is `.txt`.

## Usage

The code includes an example usage of the `Customer` class at the bottom. It demonstrates how to create instances of the `Customer` class, add and remove products from the cart, view the cart contents, and save the cart to a file.

You can modify the example code or create new instances of the `Customer` class to suit your specific requirements.
