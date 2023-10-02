from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Item,MyModel,asik
from .serializers import ItemSerializer,MyModelSerializer,LoginSerializer,asikSerializer





from rest_framework import serializers
from rest_framework import status


import json


from django.shortcuts import render, redirect
from .forms import MyModelForm,LoginForm
import requests


import pyrebase




# Create your views here.
def say_hello(request):
    x=1
    y=2
    # return render(request,'hello.html',{'name':'make it happen','x':x})
    return render(request,'hello.html',{'name':'Tushar','x':x})


# @api_view(['GET','POST','PUT'])
@api_view(['GET','POST'])
def index(request):
    courses={
    'course_name':'python',
    'learn' : ['flask','Django'],
    'Course_provieder':'Scalar'
    }
    courses1={
    'course_name':'python',
    'learn' : ['flask','Django'],
    'Course_provieder':'NOT Scalar'
    }
    if request.method == 'GET':
        print('you Hit a GET method')
        return Response(courses)
    elif request.method == 'POST':
        # data = request.data
        print('****************************************************')
        data = request.body
        print(data)
        print('****************************************************')
        

        # You can access specific form fields using their names
        # field_value = request.POST['age']
        print('you Hit a POST method')
        return Response(courses1)
    





@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)
 
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_items(request):
	
	
	# checking for the parameters from the URL
    # http://127.0.0.1:8000/api/all/?category=food
	if request.query_params:
		items = Item.objects.filter(**request.query_params.dict())
	else:
		items = Item.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def update_items(request, pk):
	# http://127.0.0.1:8000/api/update/1/
	item = Item.objects.get(pk=pk)
	data = ItemSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
	# http://127.0.0.1:8000/api/item/2/delete/
	item = get_object_or_404(Item, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)








def create_record(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            # Save data to the API
            data = form.cleaned_data  # Get validated data from the form
            api_url = 'http://127.0.0.1:8000/api/log_in/'  # Replace with your API endpoint
            response = requests.post(api_url, data=data)

            if response.status_code == 200:
                return redirect('success_page')  # Redirect to a success page
            else:
                # Handle API errors
                return render(request, 'error_page.html', {'response': response})

    else:
        form = MyModelForm()

    return render(request, 'form.html', {'form': form})


@api_view(['GET','POST'])
def add_record(request):
    item1 = MyModelSerializer(data=request.data)
 
    # validating for already existing data
    # if item1.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
 
    if item1.is_valid():
        item1.save()
        return Response(item1.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)






def create_record_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # Save data to the API
            data = login_form.cleaned_data  # Get validated data from the form
            api_url = 'http://127.0.0.1:8000/api/login/'  # Replace with your API endpoint
            response = requests.post(api_url, data=data)

            if response.status_code == 200:
                return render(request, 'success_page.html', {'response': response})
            else:
                # Handle API errors
                return redirect('.\templates\success_page')  # Redirect to a success page
               

    else:
        login_form = MyModelForm()

    return render(request, 'log_in.html', {'login_form': login_form})


@api_view(['GET','POST'])
def add_record_login(request):
    item2 = LoginSerializer(data=request.data)
 
    # validating for already existing data
    # if item1.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
 
    if item2.is_valid():
        item2.save()
        return Response(item2.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET','POST'])
def dashbord(request):
	
	
	# checking for the parameters from the URL
    # http://127.0.0.1:8000/api/all/?category=food
	if request.query_params:
		items = Item.objects.filter(**request.query_params.dict())
	else:
		items = Item.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = ItemSerializer(items, many=True)


		return render(request,'dashbord.html',{'data_from_database': serializer.data})

	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

    #  return render(request,'hello.html',{'name':'Tushar','x':x})





@api_view(['GET'])
def dashbord_asik(request):
	
	
	# checking for the parameters from the URL
    # http://127.0.0.1:8000/api/all/?category=food
	if request.query_params:
		items = asik.objects.filter(**request.query_params.dict())
	else:
		items = asik.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = asikSerializer(items, many=True)


		return render(request,'dashbord_asik.html',{'data_from_database_experiment': serializer.data})

	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

    #  return render(request,'hello.html',{'name':'Tushar','x':x})






Config = {
  "apiKey": "AIzaSyD9Umhflh0PxHoeKa_baIq4ZhPfJIGjad8",
  "authDomain": "smart-health-monitor-b15f3.firebaseapp.com",
  "databaseURL":"https://smart-health-monitor-b15f3-default-rtdb.firebaseio.com/",
  "projectId": "smart-health-monitor-b15f3",
  "storageBucket": "smart-health-monitor-b15f3.appspot.com",
  "messagingSenderId": "954528442153",
  "appId": "1:954528442153:web:4ee3c3e7d4aa99d6cb3938",
  
}


# // Initialize Firebase
# const app = initializeApp(firebaseConfig);
# const analytics = getAnalytics(app);
firebase= pyrebase.initialize_app(Config)
authe = firebase.auth()
database=firebase.database()

def experiment_data_firebase(request):
      
    Temperature = database.child('machine').child('sensorData').child('Temperature').get().val()
    HR = database.child('machine').child('sensorData').child('Heart rate').get().val()
    SpO2 = database.child('machine').child('sensorData').child('Spo2').get().val()
    ECG = database.child('machine').child('sensorData').child('ECG').get().val()
    print("Temperature",Temperature)
    return render(request,'experiment_data_firebase.html',{
          
        "Temperature":Temperature,
        "HR":HR,
        "SpO2":SpO2,
        "ECG":ECG

    })
