from django.shortcuts import render, HttpResponse
from .models import*

# Create your views here.
def index(request):
   heads  = paragraph.objects.all().first
   text = paragraph.objects.all().first
   img =paragraph.objects.all().first
   data = {
      'heads': heads,
      'text': text,
      'img': img
   }
   return render(request,'index.html', data)
   
   
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
   heads = aboutt.objects.all().first
   para = aboutt.objects.all().first
   img = aboutt.objects.all().first
   data = {
      'heads' : heads,
      'para' : para,
      'img': img
   } 
   
   
   return render(request , 'about.html', data)

   
   
def form(request):
   
   if request.method =='POST':
       
      name  = request.POST.get('name')
      email  = request.POST.get('email')
      comment  = request.POST.get('comment')
      new_contact = Contact( name = name ,email=email, comment=comment)
      new_contact.save()
      return HttpResponse("<h1> THANKS FOR CONTACT US</h1>")
   return render(request, 'form.html')
   
