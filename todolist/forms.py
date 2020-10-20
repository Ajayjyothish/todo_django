from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45, required=True, widget= forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter todo eg. Wash car", 'aria-label': 'Todo', 'aria-describeby': 'add-btn' }
    ))