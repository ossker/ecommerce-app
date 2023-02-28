from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prize = models.DecimalField(max_digits=12, decimal_places=2)

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


