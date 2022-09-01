from django.db import models

# Create your models here.


class Section(models.Model):
    title = models.TextField(max_length=200, verbose_name='Title', null=True, blank=True)
    note1 = models.TextField(max_length=200, verbose_name='Note', null=True, blank=True)
    note2 = models.TextField(max_length=200, verbose_name='Extra Note', null=True, blank=True)
    note3 = models.TextField(max_length=200, verbose_name='Extra', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Chapter(models.Model):
    section_id = models.ForeignKey(Section, related_name='chapters', on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(max_length=200, verbose_name='Title', null=True, blank=True)
    note1 = models.TextField(max_length=200, verbose_name='Note', null=True, blank=True)
    note2 = models.TextField(max_length=200, verbose_name='Extra Note', null=True, blank=True)
    note3 = models.TextField(max_length=200, verbose_name='Extra', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Item(models.Model):
    UNIT_CHOICE = [('num', 'number'),
                   ('m2', 'square_meter'),
                   ('m3', 'cube_meter'),
                   ('kg', 'kilo_gram')]
    chapter_id = models.ForeignKey(Chapter, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    code1 = models.CharField(max_length=2, null=True, blank=True)
    code2 = models.CharField(max_length=2, null=True, blank=True)
    code3 = models.CharField(max_length=2, null=True, blank=True)
    code4 = models.CharField(max_length=2, null=True, blank=True)
    dach = models.CharField(max_length=4, null=True, blank=True)
    desc = models.TextField(max_length=200, verbose_name='Description', null=True, blank=True)
    tax = models.CharField(max_length=3, null=True, blank=True)
    unit = models.CharField(max_length=5, choices=UNIT_CHOICE, null=True, blank=True)

    def __str__(self):
        return str(self.desc)
