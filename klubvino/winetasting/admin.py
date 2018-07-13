from django.contrib import admin
from winetasting.models import WineTasting, WineTastingInfo, WineTastingResults


# Register your models here.
admin.site.register(WineTasting)
admin.site.register(WineTastingInfo)
admin.site.register(WineTastingResults)
