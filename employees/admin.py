from django.contrib import admin
from .models import Employee,AttendanceRecord
from django.utils.html import format_html

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name','department','email','phone',)
    search_fields = ('first_name','last_name','email','phone')
    list_filter = ('first_name','last_name','email','phone')

class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'check_in_time', 'check_out_time', 'formatted_total_time', 'message')
    ist_filter = ('employee', 'check_in_time')  # Filter by employee or check-in time
    search_fields = ('employee__first_name', 'employee__last_name')

    def formatted_total_time(self, obj):
        total_time = obj.total_time()
        if total_time is not None:
            hours, remainder = divmod(total_time.seconds, 3600)
            minutes = remainder // 60
            return f"{hours} hours, {minutes} minutes"
        return "N/A"
    formatted_total_time.short_description = 'Total'

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)