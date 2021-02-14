from django.contrib import admin
from news_profit.models import News, ConfirmationCode, User, FavoriteNews, NewsImage

class ImageInline(admin.StackedInline):
    model = NewsImage
    extra = 2


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_filter = 'created_date'.split()
    list_display = 'id title image link'.split()
    search_fields = 'title description'.split()
    list_editable = 'title'.split()
    inlines = [ImageInline]


admin.site.register(News, NewsAdmin)
admin.site.register(ConfirmationCode)
admin.site.register(User)
admin.site.register(FavoriteNews)
admin.site.register(NewsImage)