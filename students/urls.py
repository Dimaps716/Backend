
# django
from django.urls import path

# views
from students import views

urlpatterns = [
    # url get
    path(
        route='api/students-list/',
        view= views.studentsList,
        name= 'students_list'
    ),
    path(
        route='api/tecnologies-list/',
        view= views.tecnologieList,
        name= 'tecnologies_list'
    ),
    path(
        route='api/projects-list/',
        view= views.projeList,
        name= 'projects_list'
    ),
        path(
        route='api/milestons-list/',
        view= views.milestonsList,
        name= 'milestons_list'
    ),

        path(
        route='api/courses-list/',
        view= views.coursList,
        name= 'courses_list'
    ),
        path(
        route='api/information-list/',
        view= views.infoList,
        name= 'information_list'
    ),

    # url pos detail
        path(
        route='api/students-detail/<str:pk>/',
        view=views.studensDetail,
        name= 'students-detail'
    ),
        path(
        route='api/tecnologies-detail/<str:pk>/',
        view=views.tecnologieDetail,
        name= 'tecnologies-detail'
    ),
        path(
        route='api/projectList-detail/<str:pk>/',
        view=views.projetDetail,
        name= 'projectList-detail'
    ),
        path(
        route='api/milestons-detail/<str:pk>/',
        view=views.milestonsDetail,
        name= 'milestons-detail'
    ),
        path(
        route='api/courses-detail/<str:pk>/',
        view=views.coursDetail,
        name= 'courses-detail'
    ),

    # url post
    path(
        route='api/students-create/',
        view=views.studensCreate,
        name= 'students-create'
    ),
        path(
        route='api/tecnologies-create/',
        view=views.tecnologieCreate,
        name= 'tecnologies-create'
    ),
        path(
        route='api/information-create/',
        view= views.infoCreate,
        name= 'information_create'
    ),
        path(
        route='api/projectList-create/',
        view=views.projeListCreate,
        name= 'projectList-create'
    ),
        path(
        route='api/milestons-create/',
        view=views.milestonsCreate,
        name= 'milestons-create'
    ),
        path(
        route='api/courses-create/',
        view=views.coursCreate,
        name= 'courses-create'
    ),

    # url update
        path(
        route='api/students-update/<str:pk>/',
        view=views.studensUpdate,
        name= 'students-update'
    ),
        path(
        route='api/tecnologies-update/<str:pk>/',
        view=views.tecnologieUpdate,
        name= 'tecnologies-update'
    ),
        path(
        route='api/projectList-update/<str:pk>/',
        view=views.projeUpdate,
        name= 'projectList-update'
    ),
        path(
        route='api/milestons-update/<str:pk>/',
        view=views.milestonsUpdate,
        name= 'milestons-update'
    ),
        path(
        route='api/courses-update/<str:pk>/',
        view=views.coursUpdate,
        name= 'courses-update'
    ),

    # url delete
        path(
        route='api/students-delete/<str:pk>/',
        view=views.studentsDelete,
        name= 'students-delete'
    ),
        path(
        route='api/tecnologies-delete/<str:pk>/',
        view=views.tecnologieDelete,
        name= 'tecnologies-delete'
    ),
        path(
        route='api/projectList-delete/<str:pk>/',
        view=views.projeDelete,
        name= 'projectList-delete',
    ),
        path(
        route='api/milestons-delete/<str:pk>/',
        view=views.milestonsDelete,
        name= 'milestons-delete'
    ),
        path(
        route='api/courses-delete/<str:pk>/',
        view=views.coursDelete,
        name= 'courses-delete'
    ),
]