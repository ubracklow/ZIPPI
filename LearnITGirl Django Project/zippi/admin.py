from django.contrib import admin
from .models import Pin, Map, UserProfile


class PinAdmin(admin.ModelAdmin):
	list_display = ["comment", "category", "pin_address"]
	list_filter = ["category"]

class PinInlineAdmin(admin.TabularInline):
	model = Pin
	#fields = ["comment", "category", "pin_address"]

class MapAdmin(admin.ModelAdmin):
	list_display = ["user", "map_title"]
	inlines = [PinInlineAdmin]




admin.site.register(Pin, PinAdmin)

admin.site.register(Map, MapAdmin)

admin.site.register(UserProfile)



