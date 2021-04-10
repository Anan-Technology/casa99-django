from django.shortcuts import render
# Create your views here.
from django.template.response import TemplateResponse
from .models import Projects
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def projects_index(request):
    project_list = Projects.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(project_list,5)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    ctx = {'projects':projects}
    return TemplateResponse(request, "projects/index.html", ctx)
