from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from .forms import ProjectForm
from .models import Student, Portfolio, Project, ThemeChanger


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
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render(request, 'portfolio_app/index.html', {'student_active_portfolios': student_active_portfolios})

#
#
def createProject(request, portfolio_id):

    form = ProjectForm()
    portfolio = Portfolio.objects.get(id=portfolio_id)
    print(portfolio)

    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id

        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form
            project = form.save()

            # Set the projects parent portfolio
            project.porfolio = portfolio
            project.save()

            # Redirect back to portfolio details page
            return redirect('portfolio-detail', portfolio_id)
        
    context = {'form':form}
    return render(request, 'portfolio_app/project_form.html', context)

#
#
def deleteProject(request, portfolio_id, project_id):

    # Store project object in project variable
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-detail', portfolio_id)
    
    context = {'project':project}
    return render(request, 'portfolio_app/delete_project_form.html', context)


#
#
def updateProject(request, portfolio_id, project_id):
    form = ProjectForm()
    # Store project object in project variable
    project = Project.objects.get(id=project_id)

    # Update form with current information
    form = ProjectForm(instance=project)
    if form.is_valid():
        # Save the form
        project = form.save()
        
        # Redirect back to portfolio details page
        return redirect('portfolio_app/portfolio-detail', portfolio_id)
        
    context = {'form':form}
    return render(request, 'portfolio_app/project_form.html', context)



#
#
def ThemeChangerView(request):
    theme_mode = ThemeChanger.objects.latest('id')
    if theme_mode.is_dark == False:
        theme_mode.is_dark = True
        theme_mode.save()
    else:
        theme_mode.is_dark = False
        theme_mode.save()          
    context = {'theme_mode':theme_mode.is_dark}
    return render(request,'portfolio_app/index.html',context)

