from django.shortcuts import render
from .models import Section, Chapter, Item
from django.views.generic import ListView, CreateView
from .forms import SectionForm


# Create your views here.


class SectionList(ListView):
    model = Section
    template_name = "section_list.html"
    context_object_name = 'sections'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Sections'
        return context


class SectionView(CreateView):
    model = Section
    form_class = SectionForm
    template_name = "add_section.html"


class ChapterList(ListView):
    model = Chapter
    template_name = "chapter_list.html"
    context_object_name = 'chapters'

    # def get_queryset(self, *args, **kwargs):
    #     query = Chapter.objects.filter(section_id=self.kwargs.get('section_id'))
    #     return query

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'chapters'
        context['section'] = Section.objects.get(pk=self.kwargs.get('section_id'))
        return context


class ItemList(ListView):
    model = Item

