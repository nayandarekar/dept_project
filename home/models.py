from django.db import models
from django import forms

from book_repositor.models import Book, Author, BookAuthor
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


class HomePage(Page):
    """Home Page Model"""

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField()
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('banner_image')
    ]

    def get_template(self, request, *args, **kwargs):
        return 'home/home_page.html'
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        banner_title = self.banner_title
        banner_subtitle = self.banner_subtitle
        banner_image = self.banner_image
        if request.POST.get('form_type')=='sform' or request.method == 'GET':
            # print(request.POST['form_type'])
            if request.method == 'POST' and request.POST['search_book']!="":
                q = request.POST['search_book']
            else:
                q = ''
            f=''
            book_rows = Book.objects.filter(name__contains=q).order_by('name').values() | Book.objects.filter(description__contains=q).order_by('name').values()
            book_name = {}
            for brow in book_rows:
                book_name[brow['id']] = brow['name']
            
            bookauthor_rows = BookAuthor.objects.all()
            mapbookauthor_data = {}
            
            for barow in bookauthor_rows:
                if barow.book_id in  mapbookauthor_data:
                    mapbookauthor_data[barow.book_id].append(barow.author_id)
                else:    
                    mapbookauthor_data[barow.book_id]=[]
                    mapbookauthor_data[barow.book_id].append(barow.author_id)

        
        elif request.POST.get('form_type')=='aform':
            # print(request.POST['form_type'], ":", request.POST['author_id'])
            if request.method == 'POST' and request.POST['author_id']!="":
                f = request.POST['author_id']
            else:
                f = ''
            q=''
            bookauthor_rows = BookAuthor.objects.filter(author_id=f).values()
            mapbookauthor_data = {}
            book_id_list = []

            for aarow in bookauthor_rows:
                book_id_list.append(aarow['book_id'])
                if aarow['book_id'] in  mapbookauthor_data:
                    mapbookauthor_data[aarow['book_id']].append(aarow['author_id'])
                else:
                    mapbookauthor_data[aarow['book_id']] = []
                    mapbookauthor_data[aarow['book_id']].append(aarow['author_id'])
            
            book_rows = Book.objects.filter(id__in=book_id_list).order_by('name').values()
        

        author_rows = Author.objects.filter(name__contains='').order_by('name').values()
        author_name = {}
        for arow in author_rows:
            author_name[arow['id']] = arow['name']
   
        
        context = {
            'banner_title': banner_title,
            'banner_subtitle': banner_subtitle,
            'banner_image': banner_image,
            'book_rows': book_rows,
            'mapbookauthor_data': mapbookauthor_data,
            'author_name': author_name,
            'current_name':q,
            'current_id':f,
        }
        return context

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"