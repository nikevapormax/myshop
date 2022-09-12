from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
    class Meta:
        db_table = "categories"


