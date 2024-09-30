from django.shortcuts import render, redirect
from .models import File, Person
from django.core.paginator import Paginator
import pandas as pd


def create_db(file_path):
    df = pd.read_csv(file_path) 
    # print("Columns in CSV:", df.columns.tolist())  

    for _, row in df.iterrows():
        Person.objects.create(
            enrollee_id=row['enrollee_id'],
            last_name=row['Last Name'],
            email=row['Email'],
            gender=row['Gender'],
            ip_address=row['IP Address'],
            address=row['Address']
        )


#  here we are having View to handle the file upload
def main(request):
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES['file']
        file_instance = File.objects.create(file=file)  
        create_db(file_instance.file.path)  
        return redirect('display_data') 
    return render(request, 'main.html')

#  here we are creating View to display the paginate
def display_data(request):
    people = Person.objects.all()  
    paginator = Paginator(people, 20)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'display_data.html', {'page_obj': page_obj})
