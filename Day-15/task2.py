class PaymentMethod:
    def process_payment(self, amount):
        pass   
      
class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"CreditCard: Processing payment of ₹{amount}")

class UPI(PaymentMethod):
    def process_payment(self, amount):
        print(f"UPI: Processing payment of ₹{amount}")

class Cash(PaymentMethod):
    def process_payment(self, amount):
        print(f"Cash: Accepting payment of ₹{amount}")

payments = [(CreditCard(), 5000), (UPI(), 1200), (Cash(), 250)]

for method, amount in payments:
    method.process_payment(amount)
