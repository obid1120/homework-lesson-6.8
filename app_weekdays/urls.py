from django.urls import path

from .views import weekdays, uz_weekdays, en_weekdays, ru_weekdays

urlpatterns = [
    path('', weekdays, name='weekdays'),
    path('uz/', uz_weekdays, name='uz'),
    path('en/', en_weekdays, name='en'),
    path('ru/', ru_weekdays, name='ru'),
]