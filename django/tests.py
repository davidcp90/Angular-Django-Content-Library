from django.test import TestCase
from profiles.models import User, Student, Tutor
from django.core.urlresolvers import reverse
from datetime import datetime
from datetime import timedelta
from applications.models import Subject
from profiles.models import TutorCategory, User, Student, Tutor
from courses.models import (CourseGroupStudent, Course, CourseClass,
                            CourseStudentClass, CourseClassCalendar,
                            CourseSimSimulacrumStudent)
from simulacrums.models import SimAnswer, SimQuestion, Simulacrum

# Create your tests here.
class CoursesTestCase(TestCase):
    """
        Pruebas para app de courses
    """
    def setUp(self):
        self.tutor_category = TutorCategory.objects.create(name='Categoria 1',
                                                           id=1)
        # datos usuario student
        self.user_password = "123456"
        self.user_email = 'jonathan@tutorya.com'

        # datos usuario tutor
        self.user_tutor_password = "123456"
        self.user_tutor_email = "jonathan+tutor@tutorya.com"

        # subject
        self.subject = Subject.objects.create(name=u'Matematicas')

        # usuario
        self.user = User.objects.create_user(
            username=self.user_email, email=self.user_email,
            password=self.user_password, first_name='Jonathan',
            last_name='Diaz')
        self.student = Student.objects.create(user=self.user)

        # tutor
        self.user_tutor = User.objects.create_user(
            username=self.user_tutor_email,
            email=self.user_tutor_email, password=self.user_tutor_password,
            first_name='Jonathan', last_name='Diaz')
        self.tutor = Tutor.objects.create(user=self.user_tutor, id=1555,
                                          category=self.tutor_category)
        self.tutor.profile = 'Un texto para el perfil'
        self.tutor.save()

        # create group
        self.course1 = Course(
            name='primer curso',
            description='Este es el primer curso de pruebas',
            subject=self.subject,
            tutor=self.tutor)
        self.course1.save()

        self.course2 = Course(
            name='segundo curso',
            description='Este es el segundo curso curso de pruebas',
            subject=self.subject,
            tutor=self.tutor)
        self.course2.save()

        # create calendar class
        date = datetime.now()
        start_time = date.time()
        end_time = (date + timedelta(hours=1)).time()
        self.calendar1 = CourseClassCalendar(
            date=date.date(), start_time=start_time, end_time=end_time)
        self.calendar1.save()

        # create CourseClass
        self.classe1 = CourseClass(
            name='Primera clase', description='Esta es la primera clase')
        self.classe1.save()
        self.classe1.calendar.add(self.calendar1)
        self.classe1.save()

        self.classe2 = CourseClass(
            name='Segunda clase', description='Esta es la segunda clase')
        self.classe2.save()
        self.classe2.calendar.add(self.calendar1)
        self.classe2.save()

        self.classe3 = CourseClass(
            name='Tercera clase', description='Esta es la Tercera clase')
        self.classe3.save()
        self.classe3.calendar.add(self.calendar1)
        self.classe3.save()

        self.classe4 = CourseClass(
            name='Cuarta clase', description='Esta es la cuarta clase')
        self.classe4.save()
        self.classe4.calendar.add(self.calendar1)
        self.classe4.save()

        # is create answer for simulacrum
        self.simanswer = SimAnswer(text='text de prueba')
        self.simanswer.save()

        # is create question for simulacrum
        self.simquestion = SimQuestion(text='Pregunta de prueba')
        self.simquestion.save()
        self.simquestion.answers.add(self.simanswer)


        # is create simulacrum ty
        self.simulacrum = Simulacrum(
            name='Prueba uno', description='Esto es un simulacrum de test',
            subject=self.subject)
        self.simulacrum.save()
        self.simulacrum.questions.add(self.simquestion)

        # agrego clase al curso

        self.course1.classes.add(self.classe1)
        self.course1.classes.add(self.classe2)
        self.course1.sim_simulacrums.add(self.simulacrum)

        self.course2.classes.add(self.classe3)
        self.course2.classes.add(self.classe4)
        self.course2.sim_simulacrums.add(self.simulacrum)

    def test_group_add_student(self):
        """
            Se crea para probar signal post_add de grupos con estudantes
            Agrega estudiantes a un grupo que ya tiene cursos, y le crea al
            estudiante las clases que tiene el curso
            1. Valida que el estudiante se agrega al curso
            2. Valida que se cree relacion estudiante clase
            3. Valida que se cree la relacion simulacrum tutorya
        """
        group = CourseGroupStudent(name='Prueba de primer grupo')
        group.save()
        group.courses.add(self.course1)
        group.courses.add(self.course2)
        group.students.add(self.student)

        # Verifico que se agregue estudiante a cursos del grupo
        self.assertTrue(
            self.course1.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 1')

        self.assertTrue(
            self.course2.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 2')

        # verifico CourseStudentClass
        exists_class1 = CourseStudentClass.objects.filter(
            course=self.course1, student=self.student)

        self.assertTrue(exists_class1,
                        'No existe primera clase para el estudiante')

        exists_ty_simulacrum = (
            CourseSimSimulacrumStudent.objects.get_for_student_course_simulacrum(
                self.student, self.course1, self.simulacrum))

        self.assertTrue(exists_ty_simulacrum,
                        'No existe simulacro para el estudiante')

    def test_group_remove_student(self):
        """
            Se crea para probar signal pre_remove de grupos con estudantes
            Elimina estudiante del grupo
            1. Valida que el estudiante se elimine de los cursos
            2. Valida que se elimine relacion estudiante clase
            3. Valida que se elimine relacion sim_simulacro estudiante
        """
        group = CourseGroupStudent(name='Prueba de primer grupo')
        group.save()
        group.courses.add(self.course1)
        group.courses.add(self.course2)
        group.students.add(self.student)

        # Verifico que se agregue estudiante a cursos del grupo
        self.assertTrue(
            self.course1.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 1')

        self.assertTrue(
            self.course2.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 2')

        # verifico CourseStudentClass
        exists_class1 = CourseStudentClass.objects.filter(
            course=self.course1, student=self.student)

        self.assertTrue(exists_class1,
                        'No existe primera clase para el estudiante')

        # Se elimina estudiante del grupo

        group.students.remove(self.student)

        # Verifico que se elimine estudiante del curso
        self.assertFalse(
            self.course1.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 1')

        self.assertFalse(
            self.course2.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 2')

        exists_simulacrum_student = CourseSimSimulacrumStudent.objects.filter(
            course=self.course1, student=self.student,
            sim_simulacrum=self.simulacrum
        ).exists()

        self.assertFalse(exists_simulacrum_student,
                         'No se elimino relacion estudiantes sim simulacro')

    def test_group_add_course(self):
        """
            Se crea para probar signal post_add de grupos con cursos
            Agrega un curso al grupo cuando el grupo ya tiene estudiantes
            1.Valido que se agregue estudiante al curso nuevo
            3.Valido que se cree relacion estudiante clase con las clases del
              curso nuevo.
        """
        group = CourseGroupStudent(name='Prueba de primer grupo')
        group.save()
        group.students.add(self.student)

        # agrego curso al grupo
        group.courses.add(self.course1)
        group.courses.add(self.course2)

        # Verifico que se agregue estudiante a cursos del grupo
        self.assertTrue(
            self.course1.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 1')

        self.assertTrue(
            self.course2.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 2')

        # verifico CourseStudentClass
        exists_class1 = CourseStudentClass.objects.filter(
            course=self.course1, student=self.student)

        exists_class2 = CourseStudentClass.objects.filter(
            course=self.course2, student=self.student)

        self.assertTrue(exists_class1,
                        'No existe primera clase para el estudiante')

        self.assertTrue(exists_class2,
                        'No existe primera clase para el estudiante')

        # valido que se cree el simulacro que tenga e curso 1
        exists_ty_simulacrum = (
            CourseSimSimulacrumStudent.objects.get_for_student_course_simulacrum(
                self.student, self.course1, self.simulacrum))

        self.assertTrue(exists_ty_simulacrum,
                        'No existe simulacro para el estudiante')


    def test_group_remove_course(self):
        """
            Se crea para probar signal pre_removed de grupos con cursos
            Elimino curso del grupo cuando el grupo tiene estudiantes y curso
            1. Valido que se elimine estudiante del curso
            2. Valido que se elimine relacion estudiante clase de las clases
               del curso
        """
        group = CourseGroupStudent(name='Prueba de primer grupo')
        group.save()
        group.students.add(self.student)

        # agrego curso al grupo
        group.courses.add(self.course1)
        group.courses.add(self.course2)

        # Verifico que se agregue estudiante a cursos del grupo
        self.assertTrue(
            self.course1.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 1')

        self.assertTrue(
            self.course2.students.filter(id=self.student.id).exists(),
            'No se agrego estudiante a curso 2')

        # verifico CourseStudentClass
        exists_class1 = CourseStudentClass.objects.filter(
            course=self.course1, student=self.student)

        exists_class2 = CourseStudentClass.objects.filter(
            course=self.course2, student=self.student)

        self.assertTrue(exists_class1,
                        'No existe primera clase para el estudiante')

        self.assertTrue(exists_class2,
                        'No existe primera clase para el estudiante')

        # Elimino cursos del grupo
        group.courses.remove(self.course1)
        group.courses.remove(self.course2)

        # Verifico que se agregue estudiante a cursos del grupo
        self.assertFalse(
            self.course1.students.filter(id=self.student.id).exists(),
            'No se elimino estudiante a curso 1')

        self.assertFalse(
            self.course2.students.filter(id=self.student.id).exists(),
            'No se elimino estudiante a curso 2')

        # valido que no existe el simulacro
        exists_simulacrum_student = CourseSimSimulacrumStudent.objects.filter(
            course=self.course1, student=self.student,
            sim_simulacrum=self.simulacrum
        ).exists()

        self.assertFalse(exists_simulacrum_student,
                         'No se elimino relacion estudiantes sim simulacro')


