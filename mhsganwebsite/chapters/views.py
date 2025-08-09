from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ChapterForm
from .models import Chapter

# Create your views here.
@login_required
def create_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.created_by = request.user
            chapter.save()
            return redirect('chapters')
    else:
        form = ChapterForm()
    return render(request, 'chapters/create_chapter.html', {'form': form})


def chapters_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'chapters/chapters.html', {'chapters': chapters})
