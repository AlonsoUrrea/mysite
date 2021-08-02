from django.urls import path

from . import views

app_name = 'polls' # namespace for the {% url %} struct
urlpatterns = [
    path('', views.index, name='index'), # name can be used in templates in {% url '<name>' %} structure
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]