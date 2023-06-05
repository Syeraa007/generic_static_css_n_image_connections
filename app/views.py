from django.shortcuts import render

# Create your views here.
def add_css(request):
    return render(request, 'add_css.html')

def generic_static(request):
    return render(request, 'generic_static.html')