from django.shortcuts import render
from django.http import HttpResponse


links = ("<ul>"
         "<li><a href='/weekdays'>Weekdays</a></li>"
         "<li><a href='/weekdays/uz'>Weekdays in Uzbek</a></li>"
         "<li><a href='/weekdays/en'>Weekdays in English </a></li>"
         "<li><a href='/weekdays/ru'>Weekdays in Russian </a></li>"
         "</ul")


# Create your views here.
def index(request):
    return HttpResponse('<h1>Index page</h1>'+links)


# def about(request):
#     html = '<h1>About page</h1>'
#     html += links
#     return HttpResponse(html)
#
#
# def contact(request):
#     html = '<h1>Contact page</h1>'
#     html += links
#     return HttpResponse(html)
