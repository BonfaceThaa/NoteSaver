from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import Tag

from .models import Note, Category, Goal

def home(request):
    return render(request, 'personal_site/home.html', {})

def note_list(request, tag_slug=None):
    note_list = Note.public.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        note_list = note_list.filter(tags__in=[tag])

    paginator = Paginator(note_list, 4)
    page = request.GET.get('page')

    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    return render(request, 'personal_site/notes/list.html',{'page': page,'notes': notes,'tag': tag})

def note_detail(request, year, month, day, note):
    note = get_object_or_404(Note, slug=note, status='public', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'personal_site/notes/detail.html', {'note': note})


def goal_list(request, tag_slug=None, category_slug=None):
    category = None
    categories = Category.objects.all()
    goals = Goal.objects.filter(achieved=False)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        goals = goals.filter(tags__in=[tag])

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        goals = goals.filter(category=category)
    return render(request,'personal_site/notes/goal_list.html',{'category': category,
                                                  'categories': categories,
                                                  'goals': goals,
                                                  'tag': tag})

def goal_detail(request, id, slug):
    goal = get_object_or_404(Goal, id=id, slug=slug)
    return render(request,'personal_site/notes/goal_detail.html',{'goal': goal})