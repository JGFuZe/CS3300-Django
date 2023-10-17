from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('test1', views.test1),
    path('test2', views.test2),

    # Student URLs
    path('students/', views.StudentListView.as_view(), name= 'students'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),

    # Portfolio URLs
    path('portfolio', views.PortfolioListView.as_view(), name='portfolios'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),

    # Project URLs
    path('projects', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
]