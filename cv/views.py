from django.shortcuts import render

# Create your views here.
def cv_list(request):
    return render(request, 'cv/cv_list.html', {})