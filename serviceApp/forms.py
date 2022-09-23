from django import forms
from serviceApp.models import Service, Category, Blog


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'cat_name',
            'cat_image',
            'cat_details'
        ]


class ServiceForm (forms.ModelForm):
    serv_details=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'placeholder':'Enter'}),label='Enter Service Details')
    class Meta:
        model=Service
        fields=[
            'serv_name',
            'serv_details',
            'serv_Img',
        ]


class BlogForm (forms.ModelForm):
    blog_vid=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'https://youtu.be/WTQOVd-5FwA'}),label='Enter Blog Video Link')

    class Meta:
        model = Blog
        fields = [
            'blog_img',
            'blog_title',
            'blog_content',
            'blog_quote',
            'blog_vid',
            'blog_vid_content',
            'cat_type'
        ]
