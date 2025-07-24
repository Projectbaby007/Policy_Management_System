# policyholder.py
import uuid
from datetime import datetime

class Policyholder:
    """
    Represents a policyholder in the insurance system.
    Manages policyholder registration, suspension, and reactivation.
    """
    def __init__(self, name: str, address: str, contact_info: str):
        """
        Initializes a new Policyholder object.

        Args:
            name (str): The full name of the policyholder.
            address (str): The physical address of the policyholder.
            contact_info (str): Contact information (e.g., phone, email).
        """
        self.id = str(uuid.uuid4()) # Unique ID for the policyholder
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.status = "pending_registration" # Initial status
        self.registered_date = None
        self.products = [] # List of product IDs associated with this policyholder
        self.payments = [] # List of payment IDs associated with this policyholder
        print(f"Policyholder '{self.name}' object created with ID: {self.id}")

    def register(self):
        """
        Registers the policyholder, setting their status to 'active'
        and recording the registration date.
        """
        if self.status == "pending_registration":
            self.status = "active"
            self.registered_date = datetime.now()
            print(f"Policyholder '{self.name}' (ID: {self.id}) has been registered and is now active.")
        else:
            print(f"Policyholder '{self.name}' (ID: {self.id}) is already {self.status}.")

    def suspend(self):
        """
        Suspends the policyholder, changing their status to 'suspended'.
        """
        if self.status == "active":
            self.status = "suspended"
            print(f"Policyholder '{self.name}' (ID: {self.id}) has been suspended.")
        elif self.status == "suspended":
            print(f"Policyholder '{self.name}' (ID: {self.id}) is already suspended.")
        else:
            print(f"Cannot suspend policyholder '{self.name}' (ID: {self.id}) from status: {self.status}.")

    def reactivate(self):
        """
        Reactivates a suspended policyholder, changing their status back to 'active'.
        """
        if self.status == "suspended":
            self.status = "active"
            print(f"Policyholder '{self.name}' (ID: {self.id}) has been reactivated and is now active.")
        elif self.status == "active":
            print(f"Policyholder '{self.name}' (ID: {self.id}) is already active.")
        else:
            print(f"Cannot reactivate policyholder '{self.name}' (ID: {self.id}) from status: {self.status}.")

    def add_product(self, product_id: str):
        """
        Associates a product with this policyholder.

        Args:
            product_id (str): The ID of the product to associate.
        """
        if product_id not in self.products:
            self.products.append(product_id)
            print(f"Product '{product_id}' added to policyholder '{self.name}'.")
        else:
            print(f"Product '{product_id}' is already associated with policyholder '{self.name}'.")

    def add_payment(self, payment_id: str):
        """
        Associates a payment with this policyholder.

        Args:
            payment_id (str): The ID of the payment to associate.
        """
        if payment_id not in self.payments:
            self.payments.append(payment_id)
            print(f"Payment '{payment_id}' recorded for policyholder '{self.name}'.")
        else:
            print(f"Payment '{payment_id}' was already recorded for policyholder '{self.name}'.")

    def get_details(self) -> dict:
        """
        Returns a dictionary containing the policyholder's details.

        Returns:
            dict: A dictionary with policyholder information.
        """
        return {
            "ID": self.id,
            "Name": self.name,
            "Address": self.address,
            "Contact Info": self.contact_info,
            "Status": self.status,
            "Registered Date": self.registered_date.strftime("%Y-%m-%d %H:%M:%S") if self.registered_date else "N/A",
            "Associated Products": self.products,
            "Associated Payments": self.payments
        }

# Example of how to use the Policyholder class (for testing purposes)
if __name__ == "__main__":
    print("--- Policyholder Class Demonstration ---")
    ph1 = Policyholder("Alice Wonderland", "123 Rabbit Hole, Fictional City", "alice@example.com")
    ph1.register()
    ph1.suspend()
    ph1.reactivate()
    ph1.add_product("PROD-001")
    ph1.add_payment("PAY-001")
    
    details = ph1.get_details()
    for key, value in details.items():
        print(f"{key}: {value}")
    print("-" * 40)
