from django.urls import path
from . import views # импорт представлений из текущего пакета

# настройка маршрутов
# urlpatterns - это список путей, которые могут быть вызваны в приложении

urlpatterns = [
    path('', views.index, name='index'), # путь к представлению index
    path('about/', views.about, name='about'), # путь к представлению about
]