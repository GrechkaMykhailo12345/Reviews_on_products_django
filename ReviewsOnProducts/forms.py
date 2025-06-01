from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
        labels = {
            'author': 'Ваше ім\'я',
            'text': 'Текст відгуку',
            'rating': 'Рейтинг (від 1 до 5)',
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }