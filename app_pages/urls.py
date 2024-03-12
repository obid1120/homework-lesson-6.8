from django.urls import path

from .views import index

urlpatterns = [
    # path('about/', about, name='about_urls'),
    # path('contact/', contact, name='contact_urls'),
    path('', index, name='index_urls'),
]


