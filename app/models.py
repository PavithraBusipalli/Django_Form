from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=10)
    dloc = models.CharField(max_length=10)
    def __str__(self):
        return self.dname
class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    esal = models.IntegerField()
    edeptno = models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename


    