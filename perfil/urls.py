from django.urls import path
from . import views

urlpatterns = [
        path('home/', views.home,name="home"),
        path('gerenciar/', views.gerenciar, name="gerenciar"),
        path('cadastrar_banco/', views.cadastrar_banco, name="cadastrar_banco"),
        path('update_categoria/<int:id>', views.update_categoria, name="update_categoria"),
]