from django.contrib.auth.models import User

from advising_portal.models import Department, Course

courses = [
    {
        'course_id': 'CSE103',
        'course_code': 'CSE103',
        'course_title': 'Structured Programming',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 4.5,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'ENG101',
        'course_code': 'ENG101',
        'course_title': 'Basic English',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'ENG102',
        'course_code': 'ENG102',
        'course_title': 'Composition and Communication Skills',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': "ENG101",
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'MAT101',
        'course_code': 'MAT101',
        'course_title': 'Differential and Integral Calculus',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE106',
        'course_code': 'CSE106',
        'course_title': 'Discrete Mathematics',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': 'CSE103',
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'MAT102',
        'course_code': 'MAT102',
        'course_title': 'Differential Equations and Special Functions',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': 'MAT101',
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE110',
        'course_code': 'CSE110',
        'course_title': 'Object Oriented Programming',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': "CSE106",
        'credit': 4.5,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'MAT104',
        'course_code': 'MAT104',
        'course_title': 'Co-ordinate Geometry & Vector Analysis',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': "MAT101",
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CHE109',
        'course_code': 'CHE109',
        'course_title': 'Engineering Chemistry-I',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': None,
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE209',
        'course_code': 'CSE209',
        'course_title': 'Electrical Circuits',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'MAT205',
        'course_code': 'MAT205',
        'course_title': 'Linear Algebra & Complex Variables',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': "MAT102",
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'GEN226',
        'course_code': 'GEN226',
        'course_title': 'Emergence of Bangladesh',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': 'ENG102',
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'ECO101',
        'course_code': 'ECO101',
        'course_title': 'Principles of Microeconomics',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE251',
        'course_code': 'CSE251',
        'course_title': 'Electronic Circuits',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': 'CSE209',
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'STA102',
        'course_code': 'STA102',
        'course_title': 'Statistics and Probability',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'PHY109',
        'course_code': 'PHY109',
        'course_title': 'Engineering Physics-I (Introductory Classical Physics)',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': 'MAT205',
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE200',
        'course_code': 'CSE200',
        'course_title': 'Computer-Aided Engineering Drawing',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 1,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'BUS231',
        'course_code': 'BUS231',
        'course_title': 'Engineering Physics-I (Introductory Classical Physics)',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': 'MAT205',
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE207',
        'course_code': 'CSE207',
        'course_title': 'Data Structures',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': "CSE110",
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE246',
        'course_code': 'CSE246',
        'course_title': 'Algorithms',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': 'CSE207',
        'credit': 4.5,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE302',
        'course_code': 'CSE302',
        'course_title': 'Database Systems',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': "CSE106",
        'credit': 4.5,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE325',
        'course_code': 'CSE325',
        'course_title': 'Operating Systems',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': "CSE207",
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE345',
        'course_code': 'CSE345',
        'course_title': 'Digital Logic Design',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': "CSE251",
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE347',
        'course_code': 'CSE347',
        'course_title': 'Information System Analysis and Design',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': "CSE302",
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE360',
        'course_code': 'CSE360',
        'course_title': 'Computer Architecture',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': 'CSE325',
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE405',
        'course_code': 'CSE405',
        'course_title': 'Computer Networks',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': 'CSE246',
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'GEN203',
        'course_code': 'GEN203',
        'course_title': 'Ecological System and Environment',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'GEN214',
        'course_code': 'GEN214',
        'course_title': 'Development Studies',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': "ENG102",
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'GEN210',
        'course_code': 'GEN210',
        'course_title': 'International Relation',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': "ENG102",
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'PHY209',
        'course_code': 'PHY209',
        'course_title': 'Engineering Physics-II (Introductory Quantum Physics)',
        'department_id': Department.objects.get(pk='GEN').pk,
        'prerequisite_course_id': "PHY109",
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE475',
        'course_code': 'CSE475',
        'course_title': 'Machine Learning',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE477',
        'course_code': 'CSE477',
        'course_title': 'Data Mining',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 4,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE487',
        'course_code': 'CSE487',
        'course_title': 'Computer and Cyber Security',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    },
    {
        'course_id': 'CSE407',
        'course_code': 'CSE407',
        'course_title': 'Green Computing',
        'department_id': Department.objects.get(pk='CSE').pk,
        'prerequisite_course_id': None,
        'credit': 3,
        'created_by_id': User.objects.get(username='admin').pk
    }
]
