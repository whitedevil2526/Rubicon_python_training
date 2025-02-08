from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price=models.IntegerField()

    def __str__(self):
            return self.name

class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Links to Product
    customer_name = models.CharField(max_length=255)  # Customer's name
    customer_email = models.EmailField()  # Customer's email
    quantity = models.IntegerField()  # Number of products ordered
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Auto-calculated price
    order_status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("Shipped", "Shipped"), ("Delivered", "Delivered"), ("Cancelled", "Cancelled")],
        default="Pending"
    )  # Order status choices
    order_date = models.DateTimeField(auto_now_add=True)  # Timestamp when order is placed

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} ({self.order_status})"
