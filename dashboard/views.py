from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ideas.models import Idea


@login_required
def index(request):
    ideas = Idea.objects.filter(user=request.user).order_by('-created_at')[:20]
    return render(request, 'dashboard/index.html', {'ideas': ideas})
