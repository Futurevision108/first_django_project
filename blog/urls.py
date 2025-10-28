from django.urls import path    
from blog.views import my_vlog  

urlpatterns = [
    path('', my_vlog,name='my_vlog'),
      # Home page route
]