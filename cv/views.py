from django.shortcuts import render
from django.utils import timezone
from .models import CVPost

# Create your views here.
def cv_list(request):
    cvPost = CVPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cv/cv_list.html', {'cvPost': cvPost})