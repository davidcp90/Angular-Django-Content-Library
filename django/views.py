from django.shortcuts import (redirect)
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django_decorators.decorators import (add_http_var, requires_post,
                                          json_response)
from django.contrib.auth.decorators import login_required
from .models import (Course, CourseClass, CourseStudentClass, ClassUkanbookSimulation,
                     CourseSimulacrum, CourseStudentResource, CourseResource, StudentConversationTutor as Conversation,  DiscussionMessage,UkanbookSimulation, ProgramCategory,
                     CourseTutorReportClass,CourseStudentGradeClass as Grade, CourseSimSimulacrumStudent)
from dynamicland.models import CourseLanding
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q
from datetime import datetime
from django.core import serializers
from django.core.mail import mail_admins
from profiles.models import User, Student, Tutor
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UkanbookSimulationSerializer
from profiles.views import is_tutor
import itertools
from isoweek import Week

@csrf_exempt
@requires_post
@json_response
@add_http_var('resource')
def mark_resource_as_viewed(request, resource):
    try:
        resource=int(resource)
        res=CourseResource.objects.get(pk=resource)
        try:
            viewed=CourseStudentResource.objects.get(resource=res)
            num=viewed.number_of_views
            viewed.number_of_views=num+1
            viewed.last_view=datetime.now()
            viewed.save()
        except:
            viewed=CourseStudentResource.objects.create(student=request.user.student,resource=res,number_of_views=1,last_view=datetime.now())
        return {'success': True}
    except Exception as e:
        return {'success': False}


@login_required
def course_resources(request,slug=''):
    data = {}
    user = request.user
    cl_arr=[]
    courses = get_active_courses(user)
    if courses == 'no':
        return redirect(reverse('home'))
    else:
        data['courses'] = courses
    try:
        for c in courses:
            resources=c.resources.all()
            if slug:
                last=CourseResource.objects.get(slug=slug)
                data['last']=last
            else:
                last=resources.filter(Q(file_type='IMAGEN') | Q(file_type='VIDEO')).last()
                data['last']=last
    except Exception as e:
        print(e)
    data['page_title'] = 'Librería'
    return render(
        request,
        'courses/student/resources.html',
        data)


def order_by_week(user):
    obj_class = []
    studentclass = CourseStudentClass.objects.get_class_student_with_resources(
        user.student)
    # orderno clases y simulacros y los ordeno por date_start
    result_list = sorted(
        studentclass,
        key=lambda instance:
        (instance.date_start))

    # agrupo la lista ordenada por por numero de semana
    groupweek = itertools.groupby(
        result_list,
        lambda record:
        (record.date_start.isocalendar()[1]))
    i = 1
    for week, classes in groupweek:
        obj_wc = {}
        obj_wc['week'] = i
        obj_wc['class'] = []
        for k in classes:
            obj_wc['class'].append(k)
        week = Week(datetime.now().year, week)
        obj_wc['week_start'] = week.days()[0]
        obj_wc['week_end'] = week.days()[6]
        obj_class.append(obj_wc)
        i += 1
    return obj_class