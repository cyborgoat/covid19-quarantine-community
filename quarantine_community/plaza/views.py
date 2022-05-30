from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, FormView, CreateView
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from plaza.forms import SpecialRequestForm, SupplyRegistrationForm
from plaza.models import OfficialNotification, SpecialRequest, SupplyRegistration
from django.utils import timezone

from plaza.serializers import SpecialRequestSerializer, SupplyRegistrationSerializer


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


class AddSpecialRequestView(CreateView):
    model = SpecialRequest
    form_class = SpecialRequestForm
    template_name = 'plaza/special-request/submit-request.html'
    # fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        return super().form_valid(form)


class AddSupplyRegistrationView(CreateView):
    model = SupplyRegistration
    form_class = SupplyRegistrationForm
    template_name = 'plaza/supply-registration/supply-registration.html'

    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        return super().form_valid(form)


class QuarantineLifeShareView(TemplateView):
    template_name = 'plaza/quarantine-life-share/quarantine_life_share.html'

    def get_context_data(self, **kwargs):
        context = super(QuarantineLifeShareView, self).get_context_data()
        return context


class SpecialRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = SpecialRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplyRegistrationViewSet(viewsets.ModelViewSet):
    queryset = SupplyRegistration.objects.filter(resolved_by_applicant=False)
    serializer_class = SupplyRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
