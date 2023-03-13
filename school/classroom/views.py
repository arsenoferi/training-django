from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from .models import Teacher
from . import forms

# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank')

class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
    queryset = Teacher.objects.order_by('first_name')

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')

class ContactForm(FormView):
    form_class = forms.ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thank')

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

