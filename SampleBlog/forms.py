from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note, Level, Subject


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('subject','level','document')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.none()

        if 'level' in self.data:
            try:
                level_id = int(self.data.get('level'))
                self.fields['subject'].queryset = Subject.objects.filter(level=level_id).order_by('document')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.level.subject_set.order_by('document')


class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = "__all__"


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = "__all__"
