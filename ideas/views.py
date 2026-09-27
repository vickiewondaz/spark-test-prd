from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Idea


@login_required
def index(request):
    ideas = Idea.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'ideas/index.html', {'ideas': ideas})


@login_required
def detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk, user=request.user)
    return HttpResponse(f"idea {idea.id}: {idea.title} (placeholder detail)")
