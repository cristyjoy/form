# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import Course, Detail, Subject

# Create your views here.
def list_student(request):
	students = Detail.objects.exclude()
	
	context = {
		'students': students
	}
	return render(request,"index.html", context)
	
class CourseList(View):
	def get(self, request):
		courses = Course.objects.all()

		context = {
			'courses': courses,
			}
		return render(request, "courses.html", context)
		
class SubjectList(View):
	def get(self, request):
		subjects = Subject.objects.all()
			
		context = {
			'subjects': subjects,
			}
		return render(request, "subject.html", context)