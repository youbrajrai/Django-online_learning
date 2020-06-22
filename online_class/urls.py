from django.urls import path
from .views import (
	index,about,blog_single,
	blog,contact,course_single,courses,
	subjects,first_subjects,
	second_subjects,third_subjects,fourth_subjects,fifth_subjects,sixth_subjects,seventh_subjects)
app_name = 'online_class'
urlpatterns = [
	path('',index,name='index'),
	path('index/',index,name='index'),
	path('about/',about,name='about'),
	path('blog-single/',blog_single,name='blog_single'),
	path('blog/',blog,name='blog'),
	path('contact/',contact,name='contact'),
	path('course-single/',course_single,name='course_single'),
	path('courses/',courses,name='courses'),
	path('subjects/',subjects,name='subjects'),
	path('subjects1/',first_subjects,name='first_subjects'),
	path('subjects2/',second_subjects,name='second_subjects'),
	path('subjects3/',third_subjects,name='third_subjects'),
	path('subjects4/',fourth_subjects,name='fourth_subjects'),
	path('subjects5/',fifth_subjects,name='fifth_subjects'),
	path('subjects6/',sixth_subjects,name='sixth_subjects'),
	path('subjects7/',seventh_subjects,name='seventh_subjects'),

]