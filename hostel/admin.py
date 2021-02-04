from django.contrib import admin
from .models import Hostel, Room, Student, Parents, Visitors, Fees, Staff
from django.contrib.auth.models import User, Group


admin.site.unregister(Group)
"""
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Parents)
admin.site.register(Staff)
admin.site.register(Fees)
admin.site.register(Visitors)
"""


class CSSAdminMixin(object):
    class Media:
        css = {
            "all": ("css/adminpanel.css",),
        }


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ["hostel_name", "no_of_rooms", "no_of_students"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_id",
        "student_name",
        "student_phone",
        "student_branch",
        "hostel",
        "room",
    ]
    list_filter = ["hostel", "room"]
    search_fields = ["student_name", "student_id", "student_branch"]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["room_name", "hostel"]
    list_filter = ["hostel", "capacity"]


@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display = ["student", "father_name", "mother_name"]
    search_fields = ["student__student_name", "father_name", "mother_name"]


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ["visitor_name", "student", "in_time", "out_time"]
    list_filter = ["in_time", "out_time"]
    search_fields = ["student__student_name", "visitor_name"]


@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = ["student", "fees_status"]
    list_filter = ["fees_status"]
    search_fields = ["student__student_name"]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["staff_name", "staff_duty", "hostel"]
    search_fields = ["staff_name"]
    list_filter = ["hostel", "staff_name"]
