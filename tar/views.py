from .models import Section, Chapter, Item
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .form import SectionForm
# Create your views here.


class SectionList(LoginRequiredMixin, ListView):
    model = Section
    template_name = "section_list.html"
    context_object_name = 'sections'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Sections'
        return context


class ChapterList(ListView):
    model = Chapter
    template_name = "chapter_list.html"
    context_object_name = 'chapters'

    def get_queryset(self, *args, **kwargs):
        query = Chapter.objects.filter(section_id=self.kwargs.get('section_id'))
        return query

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'chapters'
        context['section'] = Section.objects.get(pk=self.kwargs.get('section_id'))
        return context


class ItemList(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

    def get_queryset(self, *args, **kwargs):
        query = Item.objects.filter(chapter_id=self.kwargs.get('chapter_id'))
        return query

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'items'
        context['section'] = Chapter.objects.get(pk=self.kwargs.get('chapter_id')).section_id
        context['chapter'] = Chapter.objects.get(pk=self.kwargs.get('chapter_id'))
        return context


class AddNewSection(CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'new_section.html'
    success_url = reverse_lazy('section_list')
