from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/',views.detail, name = 'detail'),
    path('hello/',views.hello,name='hello'),
    path('profile',views.profile,name ='profile'),
    path('new_something_url',views.new_url_view,name='new_page_url'),
    path('old_url',views.old_url_redirect,name = 'old_url'),
    path('Home/',views.Home,name='Home'),
    path('contact/',views.contact,name ='contact'),
    path('about/',views.about,name='about'),
    path('css_one/',views.css_one, name ='css_one'),
    path('student_list/',views.student_list,   name='student_list'),
    path('add/',          views.add_student,    name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]
