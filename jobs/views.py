from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .models import Job
from .forms import PostJobForm

# Create your views here.

def jobs(request):
    jobs = Job.objects.all()
    
    return render(request, 'jobs/jobs.html', {'jobs': list(jobs)})


@login_required
def postjob(request):
    if request.method == 'POST':
        form = PostJobForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('postjob')
    else:
        form = PostJobForm(request.POST)
    return render(request, 'jobs/create.html', {'form': form})