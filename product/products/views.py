from django.shortcuts import render, HttpResponse
from .models import*
# Create your views here.
def index(request):
 return render(request,'index.html')
   
   
def model(request):
   info = CompanyInformation.objects.all().first
   products = Product.objects.all()
   
   data = {
      'info': info,
      'products': products
      
   }
   
   
   
   return render(request , 'model.html', data)

 
def contact(request):
      return render(request , 'contact.html')

def about(request):
      return render(request , 'about.html')
