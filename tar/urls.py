from django.urls import path
from .views import SectionList, SectionView, ChapterList, ItemList

urlpatterns = [
    path('', SectionList.as_view(), name='section_list'),
    path('add/', SectionView.as_view(), name='add-section'),
    path('<int:section_id>/', ChapterList.as_view(), name='chapter_list'),
    path('section/<int:chapter_id>/', ItemList.as_view(), name='item_list'),

]
