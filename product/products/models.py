from django.db import models

# Create your models here.
#company info
#product

class CompanyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self)->str:
     return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)   
    def __str__(self)->str:
     return self.name

        
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE) 
    image = models.ImageField(null = True)
    price = models.FloatField(null = True)
    date = models.DateField(auto_now_add=True)
    def __str__(self)->str:
     return self.product_name
 
 
class paragraph (models.Model):
        header = models.CharField(max_length = 100 )
        text = models.TextField()
        pics = models.ImageField(null= True)
        
        def __str__(self)->str:
           return self.header
       
class aboutt (models.Model):
    para = models.TextField()
    image= models.ImageField(null = True)  
    h5 = models.CharField(max_length = 100)
    def __str__(self)->str:
           return self.h5
       
class Contact(models.Model):
   name  = models.CharField(max_length=100)
   email  = models.EmailField()
   comment  = models.TextField()

   def __str__(self) -> str:
      return self.name       
    
        
     
     

 
