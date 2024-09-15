from django.shortcuts import render
from .forms import InputForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import InputModelForm
# Create your views here.
def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, 'forms_test/home.html',context)
class InputFormView(FormView):
    template_name = 'forms_test/input_form.html'
    form_class = InputModelForm
    success_url = reverse_lazy('form_success')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)