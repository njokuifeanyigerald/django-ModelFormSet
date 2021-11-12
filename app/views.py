from django.shortcuts import render
  
# relative import of forms
from .models import ModelFormSetModel
  
# importing formset_factory
from django.forms import modelformset_factory
  
def home(request):
  
    # creating a formset and 5 instances of GeeksForm
    DjangoFormSet = modelformset_factory(ModelFormSetModel, fields =['name', 'email','department'])
    formset = DjangoFormSet()
  
              
    # Add the formset to context dictionary
    context = {
        'formset':formset
    }

    return render(request, "app/home.html", context)