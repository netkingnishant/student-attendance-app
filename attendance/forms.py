from django.forms import ModelForm

from attendance.models import attendance


class attendanceForm(ModelForm):
    class Meta:
        model = attendance
        fields = ['Name', 'Status', 'Class']
