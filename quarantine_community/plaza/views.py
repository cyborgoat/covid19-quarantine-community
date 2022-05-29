from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from plaza.forms import SpecialRequesstForm
from plaza.models import OfficialNotification
from django.utils import timezone


class OfficialNotificationsView(ListView):
    """Page for official notifications"""
    model = OfficialNotification
    paginate_by = 100  # if pagination is desired
    context_object_name = 'notification_list'
    queryset = OfficialNotification.objects.filter(active=True)
    template_name = "plaza/official-notifications/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class SpecialRequestFormView(FormView):
    template_name = 'plaza/special-request/form.html'
    form_class = SpecialRequesstForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        return super().form_valid(form)
