
from django.contrib import admin
from django.urls import path
from products.views import index, model, contact, about 
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = 'index'),
    path('model/',model,  name = 'model'),
    path('contact/', contact, name =  'contact'),
    path('about/', about, name = 'about')

    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
