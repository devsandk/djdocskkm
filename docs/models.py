# -*- coding:utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models 

# Create your models here.

class Coll(models.Model):
    value=models.CharField(max_length=100, verbose_name=u'Название реквизита')
    description=models.TextField(verbose_name=u'Описание реквизита')
    def __unicode__(self):
        return self.value
    class Meta:
        verbose_name=u'Реквизит'
        verbose_name_plural=u'Справочник реквизитов'


class HTMLinput(models.Model):
    name=models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Doctemp(models.Model):
    name=models.CharField(max_length=90, verbose_name=u'Название раздела меню')
    image=models.ImageField(upload_to='image/doctemp/%Y/%m/%d', verbose_name=u'Иконка',blank=True)
    class Meta:
        verbose_name=u'Раздель меню'
        verbose_name_plural=u'Разделы графического меню'

class Tags(models.Model):
    name=models.CharField(max_length=25, verbose_name=u'Теги')
    class Meta:
        verbose_name=u'Управление тегами'
        verbose_name_plural=u'Управление тегами'


class Doc(models.Model):
    name=models.CharField(max_length=50, verbose_name=u'Название документа')
    file=models.FileField(upload_to='tpfile/%Y/%m/%d', verbose_name=u'Файл шаблон')
    text=tinymce_models.HTMLField(verbose_name=u'Описание документа', blank=True)
    image=models.ImageField(blank=True, verbose_name=u'Загрузить изображение документа', upload_to='image/doc/%Y/%m/%d')
    doctemps=models.ManyToManyField(Doctemp,verbose_name=u'Выбор меню документа')
    tags=models.ManyToManyField(Tags, verbose_name=u'Выбор тегов документа')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=u'Название документа'
        verbose_name_plural=u'Справочник документов'


class Coll4doc(models.Model):
    coll=models.ForeignKey(Coll, verbose_name=u'Выберите реквизит')
    doc=models.ForeignKey(Doc, verbose_name=u'Выберите документ')
    codecoll=models.CharField(max_length=15, verbose_name=u'HTML имя')
    image=models.ImageField(upload_to='image/coll/%Y/%m/%d', blank=True, verbose_name='Загрузить изображение')
    HTMLinput=models.ForeignKey(HTMLinput, verbose_name=u'HTML тип input')
    defi=models.CharField(max_length=15)
    sorting=models.IntegerField(verbose_name=u'Порядковый номер')
    def __unicode__(self):
        return unicode(self.coll)
    class Meta:
        verbose_name=u'Реквизиты и документ'
        verbose_name_plural=u'Реквизиты и документ'
