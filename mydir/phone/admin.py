from django.contrib import admin
from . models import Phone #Model_name

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class PhoneResource(resources.ModelResource):

    class Meta:
        model = Phone
        exclude = ('id', )

class PhoneAdmin(ImportExportModelAdmin):
    resource_class = PhoneResource

admin.site.register(Phone,PhoneAdmin)

# admin.site.register(Phone)

