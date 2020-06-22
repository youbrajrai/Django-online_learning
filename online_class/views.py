from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')	
def blog_single(request):
	return render(request,'blog-single.html')
def blog(request):
	return render(request,'blog.html')
def contact(request):
	return render(request,'contact.html')		
def course_single(request):
	return render(request,'course-single.html')
def courses(request):
	return render(request,'courses.html')	
def subjects(request):
	return render(request,'subjects.html')	
def first_subjects(request):
	return render(request,'subjects1.html')
def second_subjects(request):
	return render(request,'subjects2.html')			
def third_subjects(request):
	return render(request,'subjects3.html')
def fourth_subjects(request):
	return render(request,'subjects4.html')
def fifth_subjects(request):
	return render(request,'subjects5.html')
def sixth_subjects(request):
	return render(request,'subjects6.html')
def seventh_subjects(request):
	return render(request,'subjects7.html')	
