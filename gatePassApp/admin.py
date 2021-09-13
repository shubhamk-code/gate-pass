from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Admin)
# admin.site.register(Visitor)
# admin.site.register(DepartmentStaff)
# admin.site.register(Staff)
admin.site.register(Department)
# admin.site.register(Pass)
# admin.site.register(Venue)
# admin.site.register(Event)
# admin.site.register(Contractor)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventData(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'manager', )
    ordering = ('name',)
    search_fields = ('name', 'manager')

@admin.register(Contractor)
class ContractorData(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'company', 'contractual')
    ordering = ('name',)
    search_fields = ('name', 'company')


@admin.register(Staff)
class StaffData(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'contact', 'age', 'gender', 'department')
    ordering = ('name',)
    search_fields = ('name', 'department', 'contact')


@admin.register(Visitor)
class VisitorData(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'contact',
                    'age', 'gender', 'department', 'status')
    ordering = ('name',)
    search_fields = ('name', 'contact', 'status', 'gender')
