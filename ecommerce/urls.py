from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Ecommerce Admin"
admin.site.site_title = "Ecommerce Admin Portal"
admin.site.index_title = "Welcome to Ecommerce Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('project.urls'))
]