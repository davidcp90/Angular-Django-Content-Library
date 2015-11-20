from django.contrib import admin
from .models import (Course,
                     CourseResource,CourseStudentResource,)
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib import messages
from datetime import datetime
from daterange_filter.filter import DateRangeFilter




@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file_type', 'attachment',
                    'external_url', 'subject', 'courseclass']
    list_filter = ['name', 'file_type', 'subject', 'courseclass']
    exclude = ('slug', )

@admin.register(CourseStudentResource)
class CourseStudentResourceAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['student', 'resource', 'number_of_views', 'date_added']
    list_filter = ['student', 'resource', 'number_of_views']
    raw_id_fields = ['student', 'resource']

