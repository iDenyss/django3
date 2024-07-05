from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('anime', views.anime, name='anime'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('shop-single', views.shopsingle, name='shop-single'),
    path('shop-single2', views.shopsingle2, name='shop-single2'),
    path('shop-single3', views.shopsingle3, name='shop-single3'),

    path('listadoSQL', views.listadoSQL, name='listadoSQL'),

    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),


]

