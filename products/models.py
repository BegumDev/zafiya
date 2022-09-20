from django.db import models


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    visual_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def __get_visual_name__(self):
        return self.visual_name


class Product(models.Model):
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name