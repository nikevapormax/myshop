from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
    class Meta:
        db_table = "categories"
        
    def __str__(self):
        return self.category_name


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=20)
    
    class Meta:
        db_table = "order_statuses"
        
    def __str__(self):
        return self.status_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "products"
        
    def __str__(self):
        return self.product_name