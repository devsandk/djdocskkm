# -*- coding:utf-8 -*-
from django.contrib import admin
from docs.models import *

class Coll4docInline(admin.TabularInline):
    model = Coll4doc
    extra=3

class CollAdmin(admin.ModelAdmin):
    list_display=('value',)
    search_fields=['value']

class DocAdmin(admin.ModelAdmin):
    list_display=('name','file',)
    search_fields=['name']

    filter_horizontal=('doctemps','tags',)
    inlines=[Coll4docInline]
    fieldsets=[
        (u'Создать документ', {'fields':['name','text','file','image'],'classes':['wide'], 'description':u'Укажите название документа, текст и шаблон. Поле изображение не обязательное'}),
        (u'Пункты меню и теги', {'fields':['doctemps','tags'],'classes':['collapse','wide']})
    ]

class Coll4docAdmin(admin.ModelAdmin):
    list_display=('coll','doc')
    list_filter=['doc']
    search_fields=['coll']

class DoctempAdmin(admin.ModelAdmin):
    list_display=('name', 'image')


admin.site.register(Coll, CollAdmin)
admin.site.register(Doc, DocAdmin)
#admin.site.register(HTMLinput)
admin.site.register(Coll4doc, Coll4docAdmin)
admin.site.register(Doctemp, DoctempAdmin)
admin.site.register(Tags)
