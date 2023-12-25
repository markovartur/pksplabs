from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.archive, name='Articles'),
	path('<int:article_id>/', views.get_article, name='get_article'),
]
