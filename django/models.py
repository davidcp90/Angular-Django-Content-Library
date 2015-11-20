from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.comments.models import Comment
from django.template import defaultfilters
from .querysets import (CourseQuerySet, CourseStudentClassQuerySet,
                        ClassUkanbookSimulationQuerySet,
                        CourseSimulacrumQuerySet,
                        CourseStudentResourceQuerySet,
                        CourseResourceQuerySet, CourseClassQuerySet,
                        CourseSimSimulacrumStudentQuerySet)
from django.core import serializers
import json
import requests
from tutorya.settings import SCRIBBLAR_URL
from xml.etree import ElementTree
from django.db.models import Q
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.core.mail import mail_admins
from django.db.models import signals
from django.core.mail import mail_admins
from dynamicland.models import CourseLanding
from profiles.models import Student


# Create your models here.
class Course(models.Model):

    """
        tabla de cursos
    """
    ACTIVO = 'ACTIVO'
    PENDIENTE = 'PENDIENTE'
    FINALIZADO = 'FINALIZADO'
    STATUS_CHOICES = (
        (ACTIVO, u'Activo'),
        (PENDIENTE, u'Pendiente'),
        (FINALIZADO, u'Finalizado'),)
    name = models.CharField(max_length=80, verbose_name=u'Nombre curso')
    description = models.TextField(verbose_name=u'Objetivo')
    #price = models.DecimalField(max_digits=12, decimal_places=2, default=0,verbose_name=u'Precio curso')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    subject = models.ForeignKey('applications.Subject',
                                verbose_name=u'Materia')
    tutor = models.ForeignKey('profiles.Tutor', related_name='course_tutor',
                              verbose_name=u'Tutor')
    students = models.ManyToManyField(
        'profiles.Student',
        related_name='course_students',
        verbose_name=u'Estudiantes',
        blank=True,
        null=True)
    classes = models.ManyToManyField(
        'courses.CourseClass',
        related_name='course_courseclasses',
        verbose_name=u'Curso/Clases',
        blank=True,
        null=True)
    resources = models.ManyToManyField(
        'courses.CourseResource',
        related_name='course_courseresources',
        verbose_name=u'Curso/Recursos',
        blank=True,
        null=True)
    simulacrums = models.ManyToManyField(
        'courses.ClassUkanbookSimulation',
        related_name='course_classsimulacrum',
        verbose_name=u'Curso/Simulacros',
        blank=True,
        null=True)
    sim_simulacrums = models.ManyToManyField(
         'simulacrums.Simulacrum',
        related_name='courses_simsimulacrum',
        blank=True,
        null=True
    )
    status = models.CharField(choices=STATUS_CHOICES,
                              verbose_name=u'Estado',
                              default=PENDIENTE,
                              max_length=80)
    date_added = models.DateTimeField(verbose_name=u'Fecha creacion',
                                      auto_now_add=True)

    objects = CourseQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    @staticmethod
    def create_student_class_simulacrum(self, student):
        """
            Crea el student class para el estudiante con la clase y por cada
            dia del calendario de la clase
        """
        # Creo la nuevas clases para el estudiante
        for classe in self.classes.all():
            for calendarclass in classe.calendar.all():
                date_start = calendarclass.get_date_start()
                date_end = calendarclass.get_date_end()
                # si no existe el registro lo creo
                if (not CourseStudentClass.objects.exists_student_class(
                   student, classe, self, date_start, date_end)):
                    stcl = CourseStudentClass(student=student, classe=classe,
                                              course=self)
                    stcl.date_start = date_start
                    stcl.date_end = date_end
                    stcl.save()

        # Creo los simulacros para el nuevo estudiante
        for simulacrum in self.simulacrums.all():
            # Verifico que no existe el registro
            if (not CourseSimulacrum.objects.exists_simulacrum(
               student, self, simulacrum)):
                csst = CourseSimulacrum(student=student, simulacrum=simulacrum,
                                        course=self)
                csst.save()

        for simulacrum in self.sim_simulacrums.all():
            coursesimsimulacrum =(
                CourseSimSimulacrumStudent.objects
                    .get_for_student_course_simulacrum(student, self,
                                                       simulacrum))
            if not coursesimsimulacrum:
                coursesimsimulacrum = CourseSimSimulacrumStudent(
                    student=student, course=self, sim_simulacrum=simulacrum)
                coursesimsimulacrum .save()

    @staticmethod
    def remove_student_class_simulacrum(self, student):
        """
            Elimina las relaciones classe y simulacros al estudiante del curso
        """
        # Elimino studentclass del estudiante a eliminar del curso
        for classe in self.classes.all():
            studentclass = CourseStudentClass.objects.filter(
                student=student, classe=classe, course=self)
            for st in studentclass:
                st.delete()

        for simulacrum in self.simulacrums.all():
            coursesimulacrum = (
                CourseSimulacrum.objects.get_for_student_course_simulacrum(
                    student, self, simulacrum))
            if coursesimulacrum:
                coursesimulacrum.delete()

        for simulacrum in self.sim_simulacrums.all():
            coursesimsimulacrum =(
                CourseSimSimulacrumStudent.objects
                    .get_for_student_course_simulacrum(student, self,
                                                       simulacrum))
            if coursesimsimulacrum:
                coursesimsimulacrum.delete()

    def __str__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'
        ordering = ('-date_added',)
        get_latest_by = 'date_added'


class DiscussionMessage(models.Model):
    related_conversation = models.ForeignKey(
        'courses.StudentConversationTutor',
        verbose_name=u'Conversacion Estudiante-Tutor',
        related_name="dis_sct")
    date_sent = models.DateTimeField(verbose_name=u'Fecha envio',
                                     auto_now_add=True)
    message = models.TextField(verbose_name=u'Mensaje')
    sent_by_student = models.BooleanField(
        default=False, verbose_name=u'Mensaje enviado por estudiante')
    readed = models.BooleanField(default=False,
                                 verbose_name=u'¿Mensaje Leido?')
    readed_by_tutor = models.BooleanField(
        default=False, verbose_name=u'¿Mensaje leido por tutor?')

    def __str__(self):
        return u'%s %s %s' % (self.related_conversation, self.date_sent,
                              self.sent_by_student)

    @classmethod
    def post_save(cls, sender, instance, created, **kwargs):
        """
            Signal para enviar correo con mensaje a tutor o estudiante
            1. Se envia correo despues de 15 minutos de inactividad
        """
        if created:
            # Valido ultimo mensaje enviado
            discussions = DiscussionMessage.objects.filter(
                related_conversation=instance.related_conversation).order_by('-date_sent')
            if discussions.exists():
                # selecciono el penultimo no el ultimo por que el ultimo es el
                # que acabe de hacer

                if discussions.count() > 1:
                    discussion = discussions[1]
                    date = datetime.now() - discussion.date_sent
                    mins = date.total_seconds() / 60
                    if mins >= 15:
                        user = instance.related_conversation.tutor.user
                        user.user_email_course(5, None, None, None, instance)
                else:
                    user = instance.related_conversation.tutor.user
                    user.user_email_course(5, None, None, None, instance)

    class Meta:
        verbose_name = u'Mensaje'
        verbose_name_plural = u'Mensajes'
        ordering = ('-date_sent',)
        get_latest_by = 'date_sent'


class CourseResource(models.Model):
    VIDEO = 'VIDEO'
    DOCUMENTO = 'DOCUMENTO'
    ENLACE = 'ENLACE'
    IMAGEN = 'IMAGEN'
    FILE_TYPE = (
        (VIDEO, u'Video Youtube/Wiztia'),
        (DOCUMENTO, u'Documento'),
        (ENLACE, u'Enlace'),
        (IMAGEN, u'Imagen'),)
    name = models.CharField(max_length=80, verbose_name=u'Nombre recurso')
    description = models.TextField(verbose_name=u'Descripcion')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    file_type = models.CharField(choices=FILE_TYPE,
                                 verbose_name=u'Estado',
                                 default=DOCUMENTO,
                                 max_length=80)
    attachment = models.FileField(upload_to=u'courses_files', blank=True,
                                  null=True,
                                  verbose_name=u'Documento o Imagen')
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Fecha de creación')
    external_url = models.CharField(
        max_length=140, blank=True, null=True,
        verbose_name=u'URL para video(youtube/wiztia) o enlace externo')
    subject = models.ForeignKey('applications.Subject',
                                blank=True, null=True, verbose_name=u'Materia')
    courseclass = models.ForeignKey(
        'courses.CourseClass', related_name='courseresource_courseclass',
        blank=True, null=True,
        verbose_name=u'curso clase')
    objects = CourseResourceQuerySet.as_manager()

    def serialize_json(self):
        return json.loads(serializers.serialize('json', [self],).strip('[]'))

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(CourseResource, self).save(*args, **kwargs)

    def __str__(self):
        return u'%s %s' % (self.name, self.file_type)

    class Meta:
        verbose_name = u'Curso recurso'
        verbose_name_plural = u'Cursos recursos'
        ordering = ('-date_added',)
        get_latest_by = 'date_added'

class CourseStudentResource(models.Model):
    """
        En este modelo se maneja el historico de recursos que ve el estudiante
        Se cuenta como recurso cada vez que el estudiante le de click a recurso
    """
    student = models.ForeignKey(
        'profiles.Student', verbose_name=u'Estudiante',
        related_name="csr_student")
    resource = models.ForeignKey(
        'courses.CourseResource', verbose_name=u'Recurso',
        related_name="csr_resource")
    number_of_views = models.PositiveIntegerField(
        verbose_name=u'Numero de veces vistos',
        default=0)
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Fecha de creación')
    last_view = models.DateField(verbose_name=u'Ultima vez visto')
    objects = CourseStudentResourceQuerySet.as_manager()

    def __str__(self):
        return u'%s' % (self.resource.name)

    class Meta:
        verbose_name = u'Curso estudiante recurso'
        verbose_name_plural = u'Cursos estudiantes recursos'
        ordering = ('-date_added',)
        get_latest_by = 'date_added'