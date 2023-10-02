from django.urls import path,include
from playground.views import index
# from . import views

from playground.views import ApiOverview
from playground.views import add_items
from playground.views import view_items
from playground.views import update_items
from playground.views import delete_items
from playground.views import add_record
from playground.views import add_record_login
#URLConf
urlpatterns=[
    path('index/',index),
    path('',ApiOverview, name='home'),
    path('create/',add_items, name='add-items'),
    path('all/', view_items, name='view_items'),   # http://127.0.0.1:8000/api/all/?category=food
    path('update/<int:pk>/', update_items, name='update-items'),
    path('item/<int:pk>/delete/', delete_items, name='delete-items'),
    path('add/',add_record, name='add-records'),     # http://127.0.0.1:8000/api/add/
    
    path('log_in/',add_record, name='add-items'),      #http://127.0.0.1:8000/api/log_in/
    
    path('login/',add_record_login, name='add-items2'),

]

