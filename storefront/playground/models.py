from django.db import models

# Create your models here.




class MyModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    dob = models.DateField()

class Item(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
 
    def __str__(self) -> str:
        return self.name




class Login(models.Model):
    name = models.CharField(max_length=255)
    password = models.TextField()


class asik(models.Model):
    Temparature = models.IntegerField()
    HR_And_SPo2 = models.TextField()
    EGG = models.IntegerField()
    Time = models.IntegerField()







# ///////////////////////////

# # importing required library
# import mysql.connector
 
# # connecting to the database
# dataBase = mysql.connector.connect(
#                      host = "localhost",
#                      user = "user",
#                      passwd = "gfg",
#                      database = "geeks4geeks" ) 
 
# # preparing a cursor object
# cursorObject = dataBase.cursor()
 
# # creating table 
# studentRecord = """CREATE TABLE STUDENT (
#                    NAME  VARCHAR(20) NOT NULL,
#                    BRANCH VARCHAR(50),
#                    ROLL INT NOT NULL,
#                    SECTION VARCHAR(5),
#                    AGE INT
#                    )"""
 
# # table created
# cursorObject.execute(studentRecord) 
 
# # disconnecting from server
# dataBase.close()