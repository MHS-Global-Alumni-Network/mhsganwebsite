from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ChapterForm
from .models import Chapter

# Create your views here.
@login_required
def create_chapter(request):
    if request.method == 'POST':
        chapter_form = ChapterForm(request.POST)
        if chapter_form.is_valid():
            chapter = chapter_form.save(commit=False)
            chapter.created_by = request.user
            chapter.save()
            return redirect('chapters')
    else:
        chapter_form = ChapterForm()
    return render(request, 'chapters/create_chapter.html', {'form': chapter_form})


def chapters_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'chapters/chapters.html', {'chapters': chapters})
