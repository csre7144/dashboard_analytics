from django.db import models

# Create your models here.
class category(models.Model):
      title = models.CharField(max_length=255)
      description = models.TextField(max_length=255)
      image = models.ImageField(upload_to='images/categories')
      status = models.BooleanField(default=False)

      def __str__(self):
            return self.title
      
      class Meta:
            verbose_name_plural = "Category"

class product(models.Model):
      subcategory = models.ForeignKey(category, on_delete=models.CASCADE)
      title = models.CharField(max_length=255)
      description = models.TextField(max_length=255)
      image = models.ImageField(upload_to='images/categories')

      def __str__(self):
            return self.title
      
      class Meta:
            # verbose_name = "product category" 
            verbose_name_plural = "product"
            