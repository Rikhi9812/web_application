from django.shortcuts import redirect, render

from crud.forms import EmployeeForm
from crud.models import Employee

# Create your views here.


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "index.html", {'form': form})            


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    print(employee.ename)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'employee': employee})
    
def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def home(request):
    return render(request,"home.html")    
