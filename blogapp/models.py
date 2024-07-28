from django.db import models
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField( )
    created_at=models.DateTimeField(auto_now_add = True)
    author=models.CharField(max_length=50)
    tags=models.CharField(max_length=50) 
    image=models.ImageField(upload_to="media/")
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title