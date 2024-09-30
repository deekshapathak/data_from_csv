from django.shortcuts import render, redirect
from .models import File, Person
from django.core.paginator import Paginator
import pandas as pd


def create_db(file_path):
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        Person.objects.create(
            enrollee_id=row.get('enrollee_id', None),  # Using .get() to allow for missing keys
            city=row.get('City', None),
            city_development_index=row.get('City Development Index', None),
            gender=row.get('Gender', None),
            enrolled_university=row.get('Enrolled University', None),
            education_level=row.get('Education Level', None),
            major_discipline=row.get('Major Discipline', None),
            experience=row.get('Experience', None),
            company_size=row.get('Company Size', None),
            company_type=row.get('Company Type', None),
            last_new_job=row.get('Last New Job', None),
            training_hours=row.get('Training Hours', None),
            target=row.get('Target', None)
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
