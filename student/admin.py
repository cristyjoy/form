# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Detail, Course, Subject

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
	#list_display = ("last_name",)
	#list_editable = ("last_name",)
	list_filter = ("last_name",)
	search_fields = ("last_name",)
	
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ("course_name","description",)
	list_editable = ("description",)
	lst_filter = ("course_name",)
	search_fields = ("course_name","description")

	
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ("subject_name","description",)
	list_editable = ("description",)
	list_filter = ("subject_name",)
	search_fields = ("subject_name","description",)



#admin.site.register(Detail)
#admin.site.register(Course, CourseAdmin)
#admin.site.register(Subject)
