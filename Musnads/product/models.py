from django.db import models






class Category(models.Model):
    name = models.CharField(max_length=100)
    




class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
        return self.title
    
    
