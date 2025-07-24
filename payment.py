# payment.py
import uuid
from datetime import datetime, timedelta

class Payment:
    """
    Represents a payment transaction for a policy.
    Manages payment processing, reminders, and penalties.
    """
    def __init__(self, policyholder_id: str, product_id: str, amount: float, due_date: datetime):
        """
        Initializes a new Payment object.

        Args:
            policyholder_id (str): The ID of the policyholder making the payment.
            product_id (str): The ID of the product the payment is for.
            amount (float): The amount due for the payment.
            due_date (datetime): The date the payment is due.
        """
        self.id = str(uuid.uuid4()) # Unique ID for the payment
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.due_date = due_date
        self.payment_date = None # Will be set when payment is processed
        self.status = "pending" # Initial status: pending, paid, overdue, penalty
        self.penalty_amount = 0.0
        print(f"Payment object created for Policyholder '{self.policyholder_id}' for Product '{self.product_id}' with ID: {self.id}")

    def process_payment(self, payment_date: datetime = None):
        """
        Processes the payment, marking it as 'paid' or 'overdue'/'penalty'.

        Args:
            payment_date (datetime, optional): The actual date the payment was made.
                                               Defaults to current datetime if not provided.
        """
        actual_payment_date = payment_date if payment_date else datetime.now()
        self.payment_date = actual_payment_date

        if self.status in ["pending", "overdue"]:
            if actual_payment_date <= self.due_date:
                self.status = "paid"
                print(f"Payment '{self.id}' processed successfully on {self.payment_date.strftime('%Y-%m-%d')}. Status: Paid.")
            else:
                self.status = "overdue"
                print(f"Payment '{self.id}' processed on {self.payment_date.strftime('%Y-%m-%d')}. It was due on {self.due_date.strftime('%Y-%m-%d')}. Status: Overdue.")
        else:
            print(f"Payment '{self.id}' is already in status: {self.status}. No action taken.")

    def send_reminder(self):
        """
        Simulates sending a payment reminder if the payment is 'pending' or 'overdue'.
        """
        if self.status == "pending":
            print(f"Reminder: Payment '{self.id}' for Policyholder '{self.policyholder_id}' (Amount: ${self.amount:.2f}) is due on {self.due_date.strftime('%Y-%m-%d')}. Please make your payment soon.")
        elif self.status == "overdue":
            print(f"URGENT Reminder: Payment '{self.id}' for Policyholder '{self.policyholder_id}' (Amount: ${self.amount:.2f}) was due on {self.due_date.strftime('%Y-%m-%d')}. It is now overdue.")
        else:
            print(f"No reminder needed for Payment '{self.id}'. Current status: {self.status}.")

    def apply_penalty(self, penalty_rate: float):
        """
        Applies a penalty to an overdue payment and updates its status.

        Args:
            penalty_rate (float): The percentage rate for the penalty (e.g., 0.05 for 5%).
        """
        if self.status == "overdue":
            penalty = self.amount * penalty_rate
            self.penalty_amount = penalty
            self.amount += penalty # Add penalty to the total amount due
            self.status = "penalty_applied"
            print(f"Penalty of ${penalty:.2f} applied to Payment '{self.id}'. New amount due: ${self.amount:.2f}. Status: Penalty Applied.")
        elif self.status == "paid":
            print(f"Cannot apply penalty to Payment '{self.id}'. It is already paid.")
        elif self.status == "penalty_applied":
            print(f"Penalty already applied to Payment '{self.id}'.")
        else:
            print(f"Cannot apply penalty to Payment '{self.id}'. Current status: {self.status}.")

    def get_details(self) -> dict:
        """
        Returns a dictionary containing the payment's details.

        Returns:
            dict: A dictionary with payment information.
        """
        return {
            "ID": self.id,
            "Policyholder ID": self.policyholder_id,
            "Product ID": self.product_id,
            "Amount Due": f"${self.amount:.2f}",
            "Due Date": self.due_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Payment Date": self.payment_date.strftime("%Y-%m-%d %H:%M:%S") if self.payment_date else "N/A",
            "Status": self.status,
            "Penalty Amount": f"${self.penalty_amount:.2f}"
        }

# Example of how to use the Payment class (for testing purposes)
if __name__ == "__main__":
    print("--- Payment Class Demonstration ---")
    
    # Create a dummy policyholder and product ID for testing
    dummy_ph_id = str(uuid.uuid4())
    dummy_prod_id = str(uuid.uuid4())

    # Test a pending payment
    due_tomorrow = datetime.now() + timedelta(days=1)
    pay1 = Payment(dummy_ph_id, dummy_prod_id, 100.00, due_tomorrow)
    pay1.send_reminder()
    pay1.process_payment()
    print("\nDetails for pay1:")
    for key, value in pay1.get_details().items():
        print(f"{key}: {value}")

    print("-" * 40)

    # Test an overdue payment with penalty
    due_yesterday = datetime.now() - timedelta(days=1)
    pay2 = Payment(dummy_ph_id, dummy_prod_id, 200.00, due_yesterday)
    pay2.process_payment() # This will mark it as overdue
    pay2.send_reminder()
    pay2.apply_penalty(0.10) # 10% penalty
    pay2.process_payment(datetime.now() + timedelta(days=2)) # Try to process after penalty
    print("\nDetails for pay2:")
    for key, value in pay2.get_details().items():
        print(f"{key}: {value}")
    print("-" * 40)
