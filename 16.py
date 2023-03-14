import unittest

class Pizza:
    def __init__(self, diameter_in_centimeters, toppings, base_cost, cost_in_cents_per_centimeter,
                 base_diameter_in_centimeters):
        self.diameter_in_centimeters = diameter_in_centimeters
        self.toppings = toppings
        self.base_cost = base_cost
        self.cost_in_cents_per_centimeter = cost_in_cents_per_centimeter
        self.base_diameter_in_centimeters = base_diameter_in_centimeters

    def add_topping(self, topping):
        self.toppings.append(topping)

    def get_total_cost(self):
        if self.diameter_in_centimeters <= 0:
            raise ValueError("Diameter must be greater than 0.")
        else:
            cost = self.base_cost + (
                        self.diameter_in_centimeters - self.base_diameter_in_centimeters) * self.cost_in_cents_per_centimeter
            return cost

    def set_diameter_in_centimeters(self, diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be greater than 0.")
        else:
            self.diameter_in_centimeters = diameter

class TestPizza(unittest.TestCase):

    def test_add_topping(self):
        # Arrange
        pizza = Pizza(30, ["cheese"], 10, 1, 30)

        # Act
        pizza.add_topping("mushrooms")

        # Assert
        self.assertEqual(pizza.toppings, ["cheese", "mushrooms"])

    def test_get_total_cost(self):
        # Arrange
        pizza = Pizza(30, ["cheese", "mushrooms"], 10, 1, 30)

        # Act
        total_cost = pizza.get_total_cost()

        # Assert
        self.assertEqual(total_cost, 30)

    def test_set_diameter_in_centimeters(self):
        # Arrange
        pizza = Pizza(30, ["cheese", "mushrooms"], 10, 1, 30)

        # Act
        pizza.set_diameter_in_centimeters(40)

        # Assert
        self.assertEqual(pizza.diameter_in_centimeters, 40)

    def test_set_diameter_in_centimeters_raises_error(self):
        # Arrange
        pizza = Pizza(30, ["cheese", "mushrooms"], 10, 1, 30)

        # Assert
        with self.assertRaises(ValueError):
            # Act
            pizza.set_diameter_in_centimeters(0)
