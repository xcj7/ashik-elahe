from django.urls import path
from . import views

#URLConf
urlpatterns=[
    path('hello/',views.say_hello),
    path('create/', views.create_record, name='create_record'),
    path('login/', views.create_record_login, name='create_record_login'),
    path('dashbord/', views.dashbord, name='dashbord'),
    path('dashbord_experiment/', views.dashbord_asik, name='dashbord_experiment'),
    path('experiment_data_firebase/', views.experiment_data_firebase, name='dashbord_experiment_asik'),
]


