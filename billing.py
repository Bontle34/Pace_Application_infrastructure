#billing automation

import datetime
import csv

class Invoice:
    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount
        self.date = datetime.datetime.now()

    def generate_invoice(self):
        invoice_number = str(hash(self.customer_name + str(self.date)))
        filename = f"Invoice_{invoice_number}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Invoice Number', 'Customer Name', 'Amount', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Invoice Number': invoice_number, 'Customer Name': self.customer_name, 'Amount': self.amount, 'Date': self.date})

        print(f"Invoice generated: {filename}")

class PaymentGateway:
    def process_payment(self, invoice):
        # Implement payment processing logic here
        print(f"Payment processed for invoice {invoice.customer_name} - ${invoice.amount}")

# Example usage
customer_name = "John Doe"
amount = 100.00

invoice = Invoice(customer_name, amount)
invoice.generate_invoice()

payment_gateway = PaymentGateway()
payment_gateway.process_payment(invoice)