from django.contrib import admin

from .models import Author, Book, Category, Subcategory


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug',)
    list_filter = ('title',)
    empty_value_display = '-empty-'
    inlines = [SubcategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'isbn',
                    )
    list_filter = ('title',)
    empty_value_display = '-empty-'
