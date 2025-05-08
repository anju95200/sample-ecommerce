from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Category')
    decription = models.TextField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
     name = models.CharField(max_length=30)
     desc = models.TextField()
     price = models.DecimalField(max_digits=10,decimal_places=2)
     stock = models.IntegerField()
     image = models.ImageField(upload_to='product_images/', null=True, blank=True)
     cat = models.ForeignKey(Category,on_delete=models.CASCADE)
     upload_date = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.name



