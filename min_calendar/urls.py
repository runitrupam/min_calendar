"""min_calendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

'''
URL EXAMPLE:

You can add / sub ->, minute , hour , days , weeks , months
GET : /add    To add to the date.
GET : /sub    TO sub to the date.

I am not using POST as there is no saving into database is involved . 

# To subtract from the given date , here date is a query_param
http://localhost:8000/sub/?week=6&days=5&month=1&hour=3&min=30&date=12-jan-2019
Returns (with date, hr , min , sec) # "2018-10-25 20:30:00"

GET : http://localhost:8000/sub/?week=6&days=5&month=1&date=12-jan-2019
# Returns (date only , as there is no hr ,minute as a param) "2018-10-26"

# To subtract .from current date , as here date as a query_param is not present
GET : http://localhost:8000/sub/?min=30&hour=3&days=5&week=6&month=1
GET : http://localhost:8000/sub/?min=30&hour=3&days=5&week=6
GET : http://localhost:8000/sub/?min=30&hour=3&days=5&week=6&month=1


# To add from the given date , here date is a query_param
http://localhost:8000/add/?week=6&days=5&month=1&hour=3&min=30&date=12-jan-2019
Returns (with hr , min , sec) # "2019-03-28 03:30:00"

GET : http://localhost:8000/add/?week=6&days=5&month=1&date=12-jan-2019
# "2019-03-28"

# To add .from current date , as here date as a query_param is not present
GET : http://localhost:8000/add/?min=30&hour=3&days=5&week=6&month=1
GET : http://localhost:8000/add/?min=30&hour=3&days=5&week=6
GET : http://localhost:8000/add/?min=30&hour=3&days=5&week=6&month=1

GET : http://localhost:8000        # Gives today's date
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_into_date.as_view()),
    path('today/', add_into_date.as_view()),  # returns today's date
    path('sub/', sub_from_date.as_view()),  # subtracts from today's date or given date
    path('add/', add_into_date.as_view()),  # add into today's date or given date
]
