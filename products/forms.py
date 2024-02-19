from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username')

    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user
        
        super().save(commit)
        return product
class UpdateProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username')