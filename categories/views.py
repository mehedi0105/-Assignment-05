from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

# Create your views here.
def Add_Category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category Added Successfully')
            return redirect('add_category')
    else:
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html',{'form':category_form})