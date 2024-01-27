from django import forms
from app.models import *


def Dept_Valid(data):
    if data>50:
        raise forms.ValidationError('Please Nter Valid Dept')
    

def Dname(data):
    if not data.startswith(data).isupper():
        raise forms.ValidationError()

def Dlen(data):
    if len(Dlen)>10:
        raise forms.ValidationError()       
        
    

class DeptForm(forms.Form):
    deptno = forms.IntegerField(validators=[Dept_Valid,])
    dname = forms.CharField(required=False, validators=[Dname,Dlen])
    dloc = forms.CharField()



c = [[i.deptno ,i.dname] for i in Dept.objects.all()]
class EmpForm(forms.Form):
    edept = forms.ChoiceField(choices=c)
    empid= forms.IntegerField()
    ename = forms.CharField()
    esal = forms.IntegerField()

    

ccc = [[i.deptno, i.dname] for i in Dept.objects.all()]
class Multi_deptForm(forms.Form):
    DeptName = forms.MultipleChoiceField(choices=ccc)