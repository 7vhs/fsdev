from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PizzaSize(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class PizzaCrust(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PizzaSauce(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PizzaCheese(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(PizzaCheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField("Topping", blank=True)

    def __str__(self):
        return f"{self.size.name.capitalize()} Pizza with {self.crust.name} crust"

class Delivery(models.Model):
    name = models.CharField(max_length=100)
    
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)  # Optional
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True)  # Optional
    eircode = models.CharField(max_length=7, blank=True, null=True)  # Optional
    
    card_number = models.CharField(max_length=19)
    cvv = models.CharField(max_length=4)
    expiry_date = models.CharField(max_length=5) 

    delivery_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"Delivery for {self.name} at {self.address_line_1}, {self.city}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    delivery_name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=255)
    delivery_time = models.DateTimeField()
    payment_info = models.CharField(max_length=255)  # summary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user} on {self.created_at}"