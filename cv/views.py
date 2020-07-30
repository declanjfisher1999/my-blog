from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import CVPost
from .forms import CVForm
from django.http import HttpResponse

# Create your views here.
def cv_list(request):
    cvPost = CVPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cv/cv_list.html', {'cvPost': cvPost})

def cv_edit(request):
    cvPost = CVPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post = cvPost[0]
    if request.method == "POST":
        form = CVForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('cv_list')
    else:
        form = CVForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form})