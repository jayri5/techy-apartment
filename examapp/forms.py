from django import forms
from . import models


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomMailForm(forms.ModelForm):
    class Meta:
        model = models.custommail
        fields = ( 'email', 'subject',)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
        
class CreateAdminForm(forms.ModelForm):
	class Meta:
		model = models.adminmodel
		fields = ['username', 'password']        


class UploadBookForm(forms.ModelForm):
    class Meta:
        model = models.EBooksModel
        fields = ( 'pdf',)
    
    
class UploadDetails(forms.ModelForm):
    class Meta:
        model = models.students
        fields = ('name','username','rollno','dept', 'yoj', 'email','phone',)
        
class skillsform(forms.ModelForm):
    class Meta:
        model = models.skills
        fields = ('skill',)    
        
class projectsform(forms.ModelForm):
    class Meta:
        model = models.projects
        fields = ( 'project',)           
        