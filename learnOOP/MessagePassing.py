class Customer:
    def pickupCar(self):
        return

class Dealer:
    
    def notifyCarReady(self, car):
        customer = findCustomer(car)
        Customer.pickupCar(customer)
    # mechanical department notifies dealer, then dealer finds customer for that car, then notifies the customer
    def findCustomer(self, car):
        return Customer()
    # usually, these relationships tend to exist in real life