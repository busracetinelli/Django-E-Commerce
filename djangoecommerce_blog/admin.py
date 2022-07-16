from django.contrib import admin
from djangoecommerce_blog.models import Blog,BlogCategory,Hashtag

admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Hashtag)

"""
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author",
                    "created_date", "slug", "status"]
    list_display_links = ["id", "title", "author"]
    list_filter = ["created_date"]
    list_editable = ["status"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Blog


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_slug"]
    prepopulated_fields = {"category_slug": ("title",)}

    class Meta:
        model = BlogCategory

@admin.register(Page)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author",
                    "created_date", "slug", "status"]
    list_display_links = ["id", "title", "author"]
    list_filter = ["created_date"]
    list_editable = ["status"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Blog


@admin.register(PageCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_slug"]
    prepopulated_fields = {"category_slug": ("title",)}

    class Meta:
        model = BlogCategory
"""
