from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from .models import Employee, Department
from .models import Role
from datetime import datetime
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):

    emps = Employee.objects.all()

    context = {
        'emps': emps
    }

    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = int(request.POST['age'])
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        medical_problem = request.POST['medical_problem']
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
      
        new_emp = Employee(first_name=first_name, last_name=last_name, age=age, dept_id=dept, salary=salary,
                    medical_problem=medical_problem, role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")

    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exceptionn Occured! Employee Has Not Been Added  ")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Remove Successfully")

        except:
            return HttpResponse("Please Enter A vaild ID")

    emps = Employee.objects.all()

    context = {
        'emps': emps
    }

    return render(request, 'remove_emp.html', context)


def filter_emp(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        dept = request.POST['dept']

        role = request.POST['role']
        emps = Employee.objects.all()
        if first_name:
            emps = emps.filter(Q(first_name__icontains=first_name))

        if last_name:
            emps = emps.filter(Q(last_name__icontains=last_name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if role:
            emps = emps.filter(role__name__icontains=role)
            context = {
                'emps': emps
            }

        return render(request, 'view_all_emp.html', context)
    elif request.method == 'GET':

        return render(request, 'filter_emp.html')
    else:
        return render(request, 'An Exception Ocecured')
