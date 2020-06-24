from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        

    


