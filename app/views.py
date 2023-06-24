from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *
import csv

def bank_upload(request):
    a = 'C:\Users\G Gouthami\OneDrive\Desktop\apiprojects\rock\Scripts\project6\templates\bank.csv'
    
    with open(a, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        i=1
        for row in csv_data:
            print(i)
            i+=1
            bn=row[0].strip()
            instance = Bank(bank_name=bn,)
           
            instance.save()

       

        return HttpResponse('successful')
def branch_upload(request):
    b = 'C:\Users\G Gouthami\OneDrive\Desktop\apiprojects\rock\Scripts\project6\templates\branch1.csv'
    
    with open(b, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        i=1
        for row in csv_data:
              i+=1
              bank_name = row[0]
              print(row[0])
              bo = Bank.objects.filter(bank_name=bank_name)[0]
              instance = Branches(
                      bank_name=bo,            
                      
                      ifsc = row[1],
                      branch = row[2],
                      address =row[3],
                      contact=row[4],
                      city = row[5],
                      district = row[6],
                      state = row[7],)
                                  
              instance.save()


       

        return HttpResponse('successful')







def display(request):
    BO=Branches.objects.all()
    d = {'BO': BO}
    return render(request, 'display.html',d)

