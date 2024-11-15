from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.Projecthomepage,name='projecthomepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('add_task/', views.add_Task,name='add_task'),
    path('<int:pk>/delete/', views.delete_task,name='delete_task'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('logout/', views.logout,name='logout'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_studentpagecall/',views.add_studentpagecall,name='add_studentpagecall'),
    path('student_list/',views.student_list,name='student_list'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
]

