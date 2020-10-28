from . import views

app_name='buscador'

urlpatterns=[
    path('',views.index,name='index'),
    path('/listagem',views.listagem,name='listagem')
]