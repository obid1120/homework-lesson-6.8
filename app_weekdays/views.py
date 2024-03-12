from django.shortcuts import render
from django.http import HttpResponse

weekdays_desc = {
    'uz_weekdays': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
    'eng_weekdays': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'ru_weekdays': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
}

links = ('<ul>'
         '<li><a href="">Uzbek</a></li>'
         '<li><a href="">English</a></li>'
         '<li><a href="">Russian</a></li>'
         '<li><a href="">Weekdays</a></li>'
         '</ul>')


def weekdays(request):
    return HttpResponse(
        "<h1>Weekdays Table</h1>"
        "<table style = 'border: 1px solid'>"
        "<tr>"
        "<th style = 'border: 1px solid'>Uzbek</th>"
        "<th style = 'border: 1px solid'>English</th>"
        "<th style = 'border: 1px solid'>Russian</th>"
        "</tr>"
        "<tr>"
        "<td>Dushanba</td>"
        "<td>Monday</td>"
        "<td>Понедельник</td>"
        "</tr>"
        "<tr>"
        "<td>Seshanba</td>"
        "<td>Tuesday</td>"
        "<td>Вторник</td>"
        "</tr>"
        "<tr>"
        "<td>Chorshanba</td>"
        "<td>Wednesday</td>"
        "<td>Среда</td>"
        "</tr>"
        "<tr>"
        "<td>Payshanba</td>"
        "<td>Thursday</td>"
        "<td>Четверг</td>"
        "</tr>"
        "<tr>"
        "<td>Juma</td>"
        "<td>Friday</td>"
        "<td>Пятница</td>"
        "</tr>"
        "<tr>"
        "<td>Shanba</td>"
        "<td>Saturday</td>"
        "<td>Суббота</td>"
        "</tr>"
        "<tr>"
        "<td>Yakshanba</td>"
        "<td>Sunday</td>"
        "<td>Воскресенье</td>"
        "</tr>"
        "</table>"
        "<a style='padding: 10px' href='/weekdays/uz'>Uzbek</a>"
        "<a style='padding: 10px' href='/weekdays/en'>English</a>"
        "<a style='padding: 10px' href='/weekdays/ru'>Russian</a>"
    )


def uz_weekdays(request):
    return HttpResponse(
        "<h2>Hafta kunlari</h2>"
        "<ol>"
        "<li>Dushanba</li>"
        "<li>Seshanba</li>"
        "<li>Chorshanba</li>"
        "<li>Payshanba</li>"
        "<li>Juma</li>"
        "<li>Shanba</li>"
        "<li>Yakshanba</li>"
        "</ol>"
        "<a style='padding: 10px' href='/weekdays'>Weekdays</a>"
        "<a style='padding: 10px' href='/weekdays/en'>English</a>"
        "<a style='padding: 10px' href='/weekdays/ru'>Russian</a>"
    )


def en_weekdays(request):
    return HttpResponse(
        "<h1>Weekdays</h1>"
        "<ol>"
        "<li>Monday</li>"
        "<li>Tuesday</li>"
        "<li>Wednesday</li>"
        "<li>Thursday</li>"
        "<li>Friday</li>"
        "<li>Saturday</li>"
        "<li>Sunday</li>"
        "</ol>"
        "<a style='padding: 10px' href='/weekdays'>Weekdays</a>"
        "<a style='padding: 10px' href='/weekdays/uz'>Uzbek</a>"
        "<a style='padding: 10px' href='/weekdays/ru'>Russian</a>"
    )


def ru_weekdays(request):
    return HttpResponse(
        "<h1>Будни</h1>"
        "<ol>"
        "<li>Понедельник</li>"
        "<li>Вторник</li>"
        "<li>Среда</li>"
        "<li>Четверг</li>"
        "<li>Пятница</li>"
        "<li>Суббота</li>"
        "<li>Воскресенье</li>"
        "</ol>"
        "<a style='padding: 10px' href='/weekdays'>Weekdays</a>"
        "<a style='padding: 10px' href='/weekdays/uz'>Uzbek</a>"
        "<a style='padding: 10px' href='/weekdays/en'>English</a>"
    )
