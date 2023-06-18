from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Batch, Department, All
from .import forms


# Create your views here.
def index(request):
    return render(request, 'index.html')


def All_course(request):
    emps = All.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'All_Course.html', context)


def all_emp(request):
    emps = Course.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_Course.html', context)


def add_emp(request):
    if request.method == 'POST':
        Course_Code = request.POST['Course_Code']
        Course_Title = request.POST['Course_Title']
        dept = int(request.POST['dept'])
        Batch = int(request.POST['Batch'])
        Credits = request.POST['Credits']
        new_emp = Course(Course_Code=Course_Code, Course_Title=Course_Title,dept_id = dept, Batch_id = Batch,Credits=Credits)
        new_emp.save()
        return HttpResponse('Course added Successfully')
    elif request.method=='GET':
        return render(request, 'Add_Course.html')
    else:
        return HttpResponse("An Exception Occured! Course Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Course.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Course Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Course.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_Course.html',context)


def filter_emp(request):
    if request.method == 'POST':
        dept = request.POST['dept']
        Batch = request.POST['Batch']
        emps = Course.objects.all()
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if Batch:
            emps = emps.filter(Batch__name__icontains = Batch)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_Course.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_Course.html')
    else:
        return HttpResponse('An Exception Occurred')


def delete(request, id):  
    emps = Course.objects.get(id=id)  
    emps.delete()  
    return redirect("all_emp")

def update(request, id):  
    emps = Course.objects.get(id=id)  
    if request.method == 'POST':
        emps.Course_Code= request.POST.get('Course_Code')
        emps.Course_Title= request.POST.get('Course_Title')
        emps.dept.name= request.POST.get('dept')
        emps.Batch.name = request.POST.get('Batch')
        emps.Credits = request.POST.get('Credits')
        emps.save()
        return redirect("all_emp")

    context = {
        'emps': emps
    }
    print(context)
    
    return render(request, 'update.html', context)

