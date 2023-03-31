from django.db import models


class custommail(models.Model):
    email = models.CharField(max_length = 200, blank=True, null=True)
    subject = models.CharField(max_length = 1000, blank=True, null=True)
    
    def __str__(self):
        return f"{self.email}"
    
# Create your models here.
class EBooksModel(models.Model):
 
    rollno = models.CharField(max_length = 100, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/', default=" ")
 
    class Meta:
        ordering = ['rollno']
     
    def __str__(self):
        return f"{self.rollno}"
    
class adminmodel(models.Model):
 
    username = models.CharField(max_length = 80)
    password = models.CharField(max_length = 80)
 
    class Meta:
        ordering = ['username']
     
    def __str__(self):
        return f"{self.username},{self.password}"   
    
    
class students(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True)
    username = models.CharField(max_length = 200, blank=True, null=True)
    rollno = models.CharField(max_length = 100, blank=True, null=True)
    dept = models.CharField(max_length = 150, blank=True, null=True)
    yoj = models.CharField(max_length = 15, blank=True, null=True)
    email = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length = 100, blank=True, null=True)

    class Meta:
        ordering = ['rollno']
     
    def __str__(self):
        #return f"{self.name},{self.rollno}"  
        return f"{self.rollno}"  
    
    
class skills(models.Model):
    rollno = models.CharField(max_length = 100, blank=True, null=True)
    skill = models.CharField(max_length = 800, blank=True, null=True)
 
    class Meta:
        ordering = ['skill']
     
    def __str__(self):
        return f"{self.rollno}"    
    


class projects(models.Model):
    rollno = models.CharField(max_length = 100, blank=True, null=True)
    project = models.CharField(max_length = 800, blank=True, null=True)
 
    class Meta:
        ordering = ['project']
     
    def __str__(self):
        return f"{self.rollno}"    
        