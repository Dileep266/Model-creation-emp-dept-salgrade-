from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(max_length=2,primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)

class Salgrade(models.Model):
    grade=models.IntegerField()
    salary=models.IntegerField(primary_key=True)
    comm=models.IntegerField(default=10000)

    def __str__(self):
        return str(self.salary)

class Emp(models.Model):
    empno=models.IntegerField(max_length=4,primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    salary=models.OneToOneField(Salgrade,on_delete=models.CASCADE)
    
   

    def __str__(self):
        return str(self.empno)
    
    



  