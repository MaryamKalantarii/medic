from django.contrib import admin
from .models import NewsLetter,ContactUs,Doctor,Skills,Services,HealthService
# Register your models here.


admin.site.register(NewsLetter)
admin.site.register(ContactUs)
admin.site.register(Doctor)
admin.site.register(Skills)
admin.site.register(Services)
admin.site.register(HealthService)