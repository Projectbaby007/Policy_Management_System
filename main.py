# main.py
from datetime import datetime, timedelta
from policyholder import Policyholder
from product import Product
from payment import Payment

def main():
    """
    Demonstrates the policy management system by creating policyholders,
    products, and payments efficiently.
    """
    print("--- Policy Management System Demonstration ---")
    print("\n1. Creating Products:")
    # Create some insurance products
    prod_life = Product("LifeGuard Pro", "Comprehensive life insurance with investment options.", 1200.00, "Covers death, critical illness, and provides maturity benefits.")
    prod_life.create_product()

    prod_health = Product("HealthShield Max", "Premium health insurance with extensive hospital and outpatient coverage.", 850.00, "Covers hospitalization, surgeries, doctor visits, and prescription drugs.")
    prod_health.create_product()

    prod_auto = Product("DriveSafe Auto", "Standard auto insurance for personal vehicles.", 450.00, "Covers third-party damage, fire, and theft.")
    prod_auto.create_product()

    print("\n2. Creating Policyholders:")
    # Create at least two policyholders
    ph1 = Policyholder("John Doe", "123 Main St, Anytown, USA", "john.doe@example.com")
    ph1.register()

    ph2 = Policyholder("Jane Smith", "456 Oak Ave, Otherville, USA", "jane.smith@example.com")
    ph2.register()

    print("\n3. Policyholders Purchasing Products and Making Payments:")

    # Policyholder 1 (John Doe) buys LifeGuard Pro
    print(f"\n--- {ph1.name} purchases {prod_life.name} ---")
    ph1.add_product(prod_life.id)
    
    # John Doe makes a payment for LifeGuard Pro
    due_date_john = datetime.now() + timedelta(days=30) # Due in 30 days
    payment_john = Payment(ph1.id, prod_life.id, prod_life.price, due_date_john)
    ph1.add_payment(payment_john.id)
    
    # Simulate John paying on time
    payment_john.process_payment(datetime.now() + timedelta(days=5)) # Paid 5 days from now

    # Policyholder 2 (Jane Smith) buys HealthShield Max
    print(f"\n--- {ph2.name} purchases {prod_health.name} ---")
    ph2.add_product(prod_health.id)

    # Jane Smith makes a payment for HealthShield Max
    due_date_jane = datetime.now() - timedelta(days=5) # Due 5 days ago (to demonstrate overdue)
    payment_jane = Payment(ph2.id, prod_health.id, prod_health.price, due_date_jane)
    ph2.add_payment(payment_jane.id)

    # Simulate Jane paying late
    payment_jane.process_payment(datetime.now()) # Paid today, but it was due 5 days ago
    payment_jane.send_reminder() # Reminder will show it's overdue
    payment_jane.apply_penalty(0.05) # Apply 5% penalty

    print("\n4. Displaying Policyholder Account Details:")

    # Display John Doe's account details
    print("\n" + "=" * 50)
    print(f"ACCOUNT DETAILS FOR: {ph1.name}")
    print("=" * 50)
    ph1_details = ph1.get_details()
    for key, value in ph1_details.items():
        print(f"{key}: {value}")
    
    print("\n--- Associated Product Details ---")
    # In a real system, you'd fetch product details from a central product registry
    # For this demo, we'll just show the product John bought
    print(prod_life.get_details())

    print("\n--- Associated Payment Details ---")
    print(payment_john.get_details())
    print("=" * 50)


    # Display Jane Smith's account details
    print("\n" + "=" * 50)
    print(f"ACCOUNT DETAILS FOR: {ph2.name}")
    print("=" * 50)
    ph2_details = ph2.get_details()
    for key, value in ph2_details.items():
        print(f"{key}: {value}")
    
    print("\n--- Associated Product Details ---")
    # In a real system, you'd fetch product details from a central product registry
    # For this demo, we'll just show the product Jane bought
    print(prod_health.get_details())

    print("\n--- Associated Payment Details ---")
    print(payment_jane.get_details())
    print("=" * 50)

    print("\n--- End of Demonstration ---")

if __name__ == "__main__":
    main()
