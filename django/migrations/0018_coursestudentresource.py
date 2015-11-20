# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_user_course'),
        ('courses', '0017_auto_20150818_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseStudentResource',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number_of_views', models.PositiveIntegerField(default=0, verbose_name='Numero de veces vistos')),
                ('date_added', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('resource', models.ForeignKey(verbose_name='Recurso', related_name='csr_resource', to='courses.CourseResource')),
                ('student', models.ForeignKey(verbose_name='Estudiante', related_name='csr_student', to='profiles.Student')),
            ],
            options={
                'verbose_name': 'Curso estudiante recurso',
                'ordering': ('-date_added',),
                'get_latest_by': 'date_added',
                'verbose_name_plural': 'Cursos estudiantes recursos',
            },
            bases=(models.Model,),
        ),
    ]
