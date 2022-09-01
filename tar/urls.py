from django.urls import path
from .views import SectionList, SectionView, ChapterList

urlpatterns = [
    path('', SectionList.as_view(), name='section_list'),
    path('add/', SectionView.as_view(), name='add-section'),
    path('<int:section_id>/', ChapterList.as_view(), name='chapter_list'),
    path('<int:section_id>/', ChapterList.as_view(), name='chapter_list'),

]
