
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book/upload', views.BookUploadView, name ='BookUploadView'),
    path('viewbooks', views.viewbooks, name='viewbooks'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('details/', views.filldetails, name="details"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminoptions/', views.adminoptions, name="adminoptions"),
    path('adminview/', views.adminview, name="adminview"),
    path('adminviewpdf/', views.adminviewpdf, name="adminviewpdf"),
    path('adminviewpdfyoj/', views.adminviewpdfyoj, name="adminviewpdfyoj"),
    #path('adminlogin/adminview/', views.adminview, name="adminview"),
    path('adminlogin/adminoptions/', views.adminoptions, name="adminoptions"),
    path('adminlogin/adminoptions/adminview', views.adminview, name="adminview"),
    path('adminlogin/adminoptions/adminviewpdf', views.adminviewpdf, name="adminviewpdf"),
    path('adminlogin/adminoptions/adminviewpdfyoj', views.adminviewpdfyoj, name="adminviewpdfyoj"),
    path('afterlogin/', views.afterlogin, name="afterlogin"),
    path('studentview/', views.studentview, name="studentview"),
    #path('afterlogin/studentview', views.studentview, name="studentview"),
    
    path('addskill/', views.addskill, name="addskill"),
    #path('studentview/addskill', views.addskill, name="addskill"),
    #path('afterlogin/addskill', views.addskill, name="addskill"),
    #path('afterlogin/studentview/addskill', views.addskill, name="addskill"),
    path('addproject/', views.addproject, name="addproject"),
    #path('afterlogin/addproject', views.addproject, name="addproject"),
    path('addcv/', views.addcv, name="addcv"),
    #path('afterlogin/addcv', views.addcv, name="addcv"),
    path('aboutus/', views.aboutus, name="aboutus"),
    
	path('login/logout/', views.logoutUser, name="logout"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),
    
    path('password_reset_custom_greet/', views.password_reset_custom_greet, name='password_reset_custom_greet'),
    path('password_reset_custom/', views.password_reset_custom, name='password_reset_custom'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += [
     #path('accounts/', include('django.contrib.auth.urls')),

# ]