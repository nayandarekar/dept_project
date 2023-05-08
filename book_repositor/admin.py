from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Book
from .models import Author
from .models import BookAuthor


class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    # search_fields = ('name', 'description')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(BookAdmin)

class AuthorAdmin(ModelAdmin):
    model = Author
    menu_label = 'Author'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    # search_fields = ('name', 'description','book')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(AuthorAdmin)

class BookAuthorAdmin(ModelAdmin):
    model = BookAuthor
    menu_label = 'Map Book-Author'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('book', 'author','extra_live')
    list_filter = ('book', 'author','extra_live')
    # search_fields = ('book', 'author','extra_live')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(BookAuthorAdmin)