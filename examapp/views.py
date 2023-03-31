from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def index(request):
    return render(request, 'index.html')


def password_reset_custom_greet(request):
    if request.method=='POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'customized password reset'
                    email_template_name = 'password_reset.txt'
                    #email_template_name = 'it it done?'
                    
                    email = render_to_string(email_template_name)
                    #email = email_template_name
                    try:
                        send_mail(subject, email, '', [user.email])
                    except:
                        return HttpResponse('invalid')
                    messages.success(request, 'mail sent')
                    return HttpResponse('mail sent ')
    else:
        password_form =  PasswordResetForm()
    context = {'form':password_form}     
    return render(request, 'password_reset_custom.html', context)


def password_reset_custom(request):
    if request.method=='POST':
        password_form = forms.CustomMailForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'customized password reset'
                    #email_template_name = 'password_reset.txt'
                    email_template_name = password_form.cleaned_data['subject']
                    #email_template_name = 'it it done?'
                    
                    #email = render_to_string(email_template_name)
                    email = email_template_name
                    try:
                        send_mail(subject, email, '', [user.email])
                    except:
                        return HttpResponse('invalid')
                    messages.success(request, 'mail sent')
                    return HttpResponse('mail sent ')
    else:
        password_form =  forms.CustomMailForm()
    context = {'form':password_form}     
    return render(request, 'password_reset_custom.html', context)

def registerPage(request):

	form = forms.CreateUserForm()
	if request.method == 'POST':
		form = forms.CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('details')
		

	context = {'form':form}
	return render(request, 'register.html', context)


def adminlogin(request):
    form = forms.CreateAdminForm()
    if request.method == 'POST':
        form = forms.CreateAdminForm(request.POST)
        #print(form.cleaned_data.get('username'))
        #username = form.cleaned_data.get('username')
        if form.is_valid():
            #user = form.save()
            print(form.cleaned_data.get('username'))
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
			#messages.success(request, 'Admin login enabled.'+username)
            if username=='admin' and password=='admin':
                return redirect('adminoptions')
            else:
                messages.info(request, 'invalid creds')
                return redirect('adminlogin')
		
    context = {'form':form}
    return render(request, 'adminlogin.html', context)

#@login_required(login_url='login')
def adminoptions(request):
    return render(request, 'adminoptions.html')

#@login_required(login_url='login')
def adminview(request):
    #roll = request.POST.get('roll', False)
    roll = request.GET['roll']
    obj = models.students.objects.all().filter(rollno=roll)
    print(obj)
    #dept = request.POST.get('dept', False)
    #print(dept)
    skillobj = models.skills.objects.all().filter(rollno=roll)
    projobj = models.projects.objects.all().filter(rollno=roll)
    cvobj = models.EBooksModel.objects.all().filter(rollno=roll)
    context = {'obj' : obj, 'skillobj':skillobj, 'projobj':projobj, 'cvobj':cvobj, 'roll':roll}
    #return redirect('index')
    return render(request, 'adminview.html', context)

#@login_required(login_url='login')   
def adminviewpdf(request):
    #dept = request.POST.get('dept', False)
    dept = request.GET['dept']
    #print(dept)
    cvobj = models.students.objects.filter(dept=dept)
    rolls=list(models.students.objects.filter(dept=dept))
    #print(cvobj)
    #print(rolls)
    lines = []
    for obj in models.students.objects.filter(dept=dept):
        #lines.append(obj)
        print(obj)
        cvobj = models.EBooksModel.objects.filter(rollno=obj)
        #cvobj = models.EBooksModel.objects.all().filter(rollno=obj)
        print(cvobj)
        lines.append(cvobj)
        #print(cv)
    print('helo')    
    print(lines)    
    #context = {'obj' : obj, 'skillobj':skillobj, 'projobj':projobj, 'cvobj':cvobj, 'roll':roll}
    context = {'dept':dept, 'cvobj' : lines}
    #return redirect('index')
    #return render(request, 'adminview.html', context)
    return render(request, 'adminviewpdf.html', context)

#@login_required(login_url='login')   
def adminviewpdfyoj(request):
    #dept = request.POST.get('dept', False)
    yoj = request.GET['yoj']
    #print(dept)
    cvobj = models.students.objects.filter(yoj=yoj)
    rolls=list(models.students.objects.filter(yoj=yoj))
    #print(cvobj)
    #print(rolls)
    lines = []
    for obj in models.students.objects.filter(yoj=yoj):
        #lines.append(obj)
        print(obj)
        cvobj = models.EBooksModel.objects.filter(rollno=obj)
        #cvobj = models.EBooksModel.objects.all().filter(rollno=obj)
        print(cvobj)
        lines.append(cvobj)
        #print(cv)
    print('helo')    
    print(lines)    
    #context = {'obj' : obj, 'skillobj':skillobj, 'projobj':projobj, 'cvobj':cvobj, 'roll':roll}
    context = {'yoj':yoj, 'cvobj' : lines}
    #return redirect('index')
    #return render(request, 'adminview.html', context)
    return render(request, 'adminviewpdfyoj.html', context)

def filldetails(request):
    form = forms.UploadDetails()
    if request.method == 'POST':
        form = forms.UploadDetails(request.POST,request.FILES)
        if form.is_valid():
            # Create a model Store instance
            skillobj = models.skills()

            # Assign attribute value to instance with Python dotted notation
            rollno = form.cleaned_data.get('rollno')
            skillobj.rollno = rollno

            # Invoke the save() method to create the record
            skillobj.save()

            # If successful, record reference has id 
            skillobj.id
            
            # Create a model Store instance
            projectobj = models.projects()

            # Assign attribute value to instance with Python dotted notation
            rollno = form.cleaned_data.get('rollno')
            projectobj.rollno = rollno

            # Invoke the save() method to create the record
            projectobj.save()

            # If successful, record reference has id 
            projectobj.id
            
            
            # Create a model Store instance
            cvobj = models.EBooksModel()

            # Assign attribute value to instance with Python dotted notation
            rollno = form.cleaned_data.get('rollno')
            cvobj.rollno = rollno

            # Invoke the save() method to create the record
            cvobj.save()

            # If successful, record reference has id 
            cvobj.id
            name = form.cleaned_data.get('name')
            username = form.cleaned_data.get('username')
            rollno = form.cleaned_data.get('rollno')
            dept = form.cleaned_data.get('dept')
            yoj = form.cleaned_data.get('yoj')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            if name and username and rollno and dept and email and phone:
                form.save()
                return redirect('login')
            else:
                return redirect('details')
    
    else:
        form = forms.UploadDetails()
        context = {
            'form':form,
        }
    
    #allPost = models.students.objects.all()
    #context = {'form':form,'allPost':allPost} 
    context = {'form':form} 
    return render(request, 'filldetails.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        #if username=="admin" and password=="admin":
            #return redirect('adminoptions')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('afterlogin')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def aboutus(request):
    return render(request, 'aboutus.html')

def career(request):
    return render(request, 'career/index.html')

@login_required(login_url='login')
def studentview(request):
    if request.user.is_authenticated:
        username = request.user.username
    result = models.students.objects.get(username=username)
    roll=result.rollno
    obj = models.students.objects.all().filter(rollno=roll)
    print(obj)
    skillobj = models.skills.objects.all().filter(rollno=roll)
    projobj = models.projects.objects.all().filter(rollno=roll)
    cvobj = models.EBooksModel.objects.all().filter(rollno=roll)
    if cvobj:
        print("heyyy")
    else:
        print("byee")
    #print(cvobj) 
    share = models.EBooksModel.objects.get(rollno=roll)
    print(share.pdf)
    if share.pdf:
        print("heueey")
    else:
        print("byee") 
        cvobj = None
    context = {'obj' : obj, 'skillobj':skillobj, 'projobj':projobj, 
               'cvobj':cvobj, 
               'roll':roll}
    #return redirect('index')
    #return render(request, 'index.html')
    return render(request, 'studentview.html', context)
   

@login_required(login_url='login')
def afterlogin(request):   
    return render(request, 'afterlogin.html')    
    
@login_required(login_url='login')
def addskill(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(username)    
    result = models.students.objects.get(username=username)
    print(result.rollno)
    if request.method == 'POST':
        form1 = forms.skillsform(request.POST,request.FILES)
        #form1.rollno = result.rollno
        if form1.is_valid():
            form1.save()
            print(form1.cleaned_data.get('skill'))
            print(result.rollno)
            #t = models.skills.objects.all().filter(rollno=result.rollno)
            t = models.skills.objects.get(rollno=result.rollno)
            print(t.skill)
            new = form1.cleaned_data.get('skill')
            if t.skill==None:
                t.skill = new
            else:    
                t.skill = t.skill + ', ' + new
            t.save()
            #form1.rollno = result.rollno
            
    form1 = forms.skillsform() 
    context={'user':username, 'rollno':result.rollno, 'dept': result.dept,
             'email':result.email, 'phone':result.phone, 'form':form1}    
    return render(request, 'addskill.html', context)


#@login_required(login_url='login')
def addproject(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    result = models.students.objects.get(username=username)
    print(result.rollno)

    if request.method == 'POST':
        form2 = forms.projectsform(request.POST,request.FILES)
        #form1.rollno = result.rollno
        if form2.is_valid():
            form2.save()
            print(form2.cleaned_data.get('project'))
            print(result.rollno)
            #t = models.skills.objects.all().filter(rollno=result.rollno)
            t = models.projects.objects.get(rollno=result.rollno)
            #t.project = form2.cleaned_data.get('project')
            new = form2.cleaned_data.get('project')
            if t.project==None:
                t.project = new
            else:    
                t.project = t.project + ', ' + new
            t.save()
    #if request.method == 'POST':
        #form2 = forms.projectsform(request.POST,request.FILES)
        #if form2.is_valid():
            #form2.save()
    form2 = forms.projectsform() 
    
    
    context={'user':username, 'rollno':result.rollno, 'dept': result.dept,
             'email':result.email, 'phone':result.phone, 'form':form2}    
    return render(request, 'addproject.html', context) 

#@login_required(login_url='login')
def addcv(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    result = models.students.objects.get(username=username)
    print(result.rollno)
    if request.method == 'POST':
        form3 = forms.UploadBookForm(request.POST,request.FILES)
        #form1.rollno = result.rollno
        if form3.is_valid():
            form3.save()
            print(form3.cleaned_data.get('pdf'))
            print(result.rollno)
            #t = models.skills.objects.all().filter(rollno=result.rollno)
            t = models.EBooksModel.objects.get(rollno=result.rollno)
            t.pdf = form3.cleaned_data.get('pdf')
            t.save()
            return HttpResponse('your CV is uploaded')
            
    form3 = forms.UploadBookForm()
    context={'user':username, 'rollno':result.rollno, 'dept': result.dept,
             'email':result.email, 'phone':result.phone, 'form':form3}    
    return render(request, 'addcv.html', context)   

def BookUploadView(request):
    if request.method == 'POST':
        form = forms.UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = forms.UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'UploadBook.html', context)

def viewbooks(request):
    books=models.EBooksModel.objects.all()
    return render(request,'viewbooks.html',{'books':books})