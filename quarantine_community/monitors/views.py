from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DrinkingWaterView(TemplateView):
    template_name = 'monitors/drinking-water/index.html'

    def get_context_data(self, **kwargs):
        context = super(DrinkingWaterView, self).get_context_data(**kwargs)
        return context
