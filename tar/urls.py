from django.urls import path
from .views import SectionList, ChapterList, ItemList, AddNewSection

urlpatterns = [
    path('', SectionList.as_view(), name='section_list'),
    path('<int:section_id>/', ChapterList.as_view(), name='chapter_list'),
    path('section/<int:chapter_id>/', ItemList.as_view(), name='item_list'),
    path('new_section/', AddNewSection.as_view(), name='new_section'),

]
