from tabnanny import verbose
from django.db import models
from django.forms import CharField



class CustomerCL(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class ProductCL(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='')
    price = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name



STATUS = (
        ('Обробатыватся', 'Обробатыватся'),
        ('Выехал','Выехал'),
        ('Доставлен','Доставлен')
    )

class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE, related_name='order_product')
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.product.name