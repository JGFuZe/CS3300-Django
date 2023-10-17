from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Student, Portfolio, Project


# Create your views here.

# Student Class Views
class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student


# Portfolio Class Views
class PortfolioListView(generic.ListView):
    model = Portfolio


class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    # override get_context_data to add a project_info object to portfolio_detail.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        k = Portfolio.pk
        context["project_info"] = Project.objects.filter(
            portfolio_id=self.get_object())
        return context


# Project Class Views
class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project


# pass all active portfolio's to homepage
def index(request):
    student_active_portfolios = Student.objects.select_related(
        'portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render(request, 'portfolio_app/index.html', {'student_active_portfolios': student_active_portfolios})


def oldHome(request):
    return HttpResponse('Home Page')


def test1(request):
    return HttpResponse('test1')


def test2(request):
    return HttpResponse('test2')
