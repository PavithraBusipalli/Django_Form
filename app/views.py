from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.

def insert_dept(request):
    DO = DeptForm()
    d = {'deptform':DO}
    if request.method == 'POST':
        DCO = DeptForm(request.POST)
        if DCO.is_valid():
            val_data = DCO.cleaned_data
            dno = val_data['deptno']
            dn = val_data['dname']
            dl = val_data['dloc']
            DO = Dept.objects.get_or_create(deptno=dno, dname=dn, dloc=dl)[0]
            DO.save()
            return HttpResponse('Dept inserted successfully')
        else:
            return HttpResponse('Please Nter valid data')
    return render(request,'insert_dept.html',d)


def insert_emp(request):
    EO = EmpForm()
    dd = {'dept':EO}
    if request.method == 'POST':
        ECO = EmpForm(request.POST)
        #print(ECO.cleaned_data)
        if ECO.is_valid():
            val_dataa = ECO.cleaned_data
            ed = val_dataa['edept']
            eno = val_dataa['empid']
            en = val_dataa['ename']
            es = val_dataa['esal']
            DOO = Dept.objects.get(deptno=ed)
            NEO = Employee.objects.get_or_create( edeptno=DOO,empid=eno, ename=en, esal=es)[0]
            NEO.save()
            return HttpResponse('Employee inserted successfully')
        else:
            print(False)
            
    return render(request,'insert_emp.html',dd)



def multi_dept_display(request):
    DO = Multi_deptForm()
    ddd = {'dept':DO}
    if request.method == 'POST':
        DCD = Multi_deptForm(request.POST)
        if DCD.is_valid():
            valid_data = DCD.cleaned_data
            dn = valid_data['DeptName']
            nl = []
            for k in dn:
                nl.append(Dept.objects.get(deptno=k))
            #print("nl: ",nl)
            EDO = Employee.objects.none()
            for i in nl:
                EDO = EDO | Employee.objects.filter(edeptno=i)
            #print("EDO: ",EDO)
            return render(request,'display_emp.html',{'emps':EDO})
    return render(request,'multi_dept_display.html',ddd)












































