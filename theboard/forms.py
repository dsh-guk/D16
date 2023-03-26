from django import forms
from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):   
    ''' Form for creation Post ''' 
    class Meta:
        model = Post
        fields = ['title', 'category', 'body', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),            
            'category': forms.Select(attrs={'class': 'form-control'}),            
            'body': forms.Textarea(attrs={'class': 'form-control'}),            
        }

    
class EditForm(ModelForm):
    ''' Form for editing Post ''' 
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),            
            'category': forms.Select(attrs={'class': 'form-control'}),       
            'body': forms.Textarea(attrs={'class': 'form-control'}),            
        }


class CommentForm(ModelForm):
    ''' Form for creation response/comment '''     
    class Meta:
        model = Comment
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type comment text here ...'}),                        
        }
        
