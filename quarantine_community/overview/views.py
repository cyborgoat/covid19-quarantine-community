from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class OverviewView(TemplateView):
    template_name = "overview/index.html"

    def get_context_data(self, **kwargs):
        context = super(OverviewView,self).get_context_data(**kwargs)
        return context