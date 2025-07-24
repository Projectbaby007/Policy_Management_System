# product.py
import uuid

class Product:
    """
    Represents an insurance product offered by the company.
    Manages product creation, updates, and suspension.
    """
    def __init__(self, name: str, description: str, price: float, coverage_details: str):
        """
        Initializes a new Product object.

        Args:
            name (str): The name of the product (e.g., "Life Insurance").
            description (str): A brief description of the product.
            price (float): The annual or monthly price of the product.
            coverage_details (str): Detailed information about what the product covers.
        """
        self.id = str(uuid.uuid4()) # Unique ID for the product
        self.name = name
        self.description = description
        self.price = price
        self.coverage_details = coverage_details
        self.status = "pending_creation" # Initial status
        print(f"Product '{self.name}' object created with ID: {self.id}")

    def create_product(self):
        """
        Sets the product status to 'active' after creation.
        """
        if self.status == "pending_creation":
            self.status = "active"
            print(f"Product '{self.name}' (ID: {self.id}) has been created and is now active.")
        else:
            print(f"Product '{self.name}' (ID: {self.id}) is already {self.status}.")

    def update_product(self, **kwargs):
        """
        Updates one or more attributes of the product.

        Args:
            **kwargs: Keyword arguments where the key is the attribute name
                      and the value is the new value.
                      Allowed attributes: 'name', 'description', 'price', 'coverage_details'.
        """
        allowed_attributes = ['name', 'description', 'price', 'coverage_details']
        updated_count = 0
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
                print(f"Product '{self.name}' (ID: {self.id}): Updated '{key}' to '{value}'.")
                updated_count += 1
            else:
                print(f"Warning: Attribute '{key}' is not a valid product attribute for update.")
        if updated_count == 0:
            print(f"No valid attributes were updated for product '{self.name}' (ID: {self.id}).")

    def suspend_product(self):
        """
        Suspends the product, changing its status to 'suspended'.
        Suspended products cannot be purchased but existing policies remain.
        """
        if self.status == "active":
            self.status = "suspended"
            print(f"Product '{self.name}' (ID: {self.id}) has been suspended.")
        elif self.status == "suspended":
            print(f"Product '{self.name}' (ID: {self.id}) is already suspended.")
        else:
            print(f"Cannot suspend product '{self.name}' (ID: {self.id}) from status: {self.status}.")

    def reactivate_product(self):
        """
        Reactivates a suspended product, changing its status back to 'active'.
        """
        if self.status == "suspended":
            self.status = "active"
            print(f"Product '{self.name}' (ID: {self.id}) has been reactivated and is now active.")
        elif self.status == "active":
            print(f"Product '{self.name}' (ID: {self.id}) is already active.")
        else:
            print(f"Cannot reactivate product '{self.name}' (ID: {self.id}) from status: {self.status}.")

    def get_details(self) -> dict:
        """
        Returns a dictionary containing the product's details.

        Returns:
            dict: A dictionary with product information.
        """
        return {
            "ID": self.id,
            "Name": self.name,
            "Description": self.description,
            "Price": f"${self.price:.2f}",
            "Coverage Details": self.coverage_details,
            "Status": self.status
        }

# Example of how to use the Product class (for testing purposes)
if __name__ == "__main__":
    print("--- Product Class Demonstration ---")
    prod1 = Product("Auto Shield", "Comprehensive car insurance", 500.00, "Covers collision, theft, and third-party liability.")
    prod1.create_product()
    prod1.update_product(price=550.00, description="Enhanced comprehensive car insurance.")
    prod1.suspend_product()
    prod1.reactivate_product()

    details = prod1.get_details()
    for key, value in details.items():
        print(f"{key}: {value}")
    print("-" * 40)
