from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView,ListView
from app.forms import *
from django.http import HttpResponse

class SchoolInsertForm(FormView):
    form_class=SchoolForm
    template_name='SchoolInsertForm.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return HttpResponse('Data is inserted')


class DisplaySchool(ListView):
    model=School
    template_name='DisplaySchool.html'
    context_object_name='sclist'
    ordering=['Sage']