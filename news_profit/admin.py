from django.contrib import admin
from news_profit.models import News, ConfirmationCode, User

admin.site.register(News)
admin.site.register(ConfirmationCode)
admin.site.register(User)