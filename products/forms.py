from .models import Product                                                                                 # Shu ilovadagi Product modelini import qiladi.
from django import forms                                                                                    # Django formalaridan foydalanish uchun forms modulini import qiladi.

class NewProductForm(forms.ModelForm):                                                                      # Product modeli bilan bog'langan yangi mahsulot formasini yaratadi.
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))                    # Bir nechta rasm tanlash imkoniga ega rasm maydonini belgilaydi.
    class Meta:                                                                                             # ModelForm uchun model va maydonlar sozlamalarini saqlaydi.
        model = Product                                                                                     # Forma Product modeli bilan ishlashini belgilaydi.
        fields = ('title', 'description', 'price', 'adress', 'category', 'phone_number', 'tg_username')     # Formada ko'rsatiladigan Product maydonlarini belgilaydi.
        labels = {
            'title': "E'lon nomi",
            'description': 'Tavsif',
            'price': 'Narxi',
            'adress': 'Manzil',
            'category': 'Toifa',
            'phone_number': 'Telefon raqami',
            'tg_username': 'Telegram foydalanuvchi nomi',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].label = 'Rasmlar'

    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user
        super().save(commit)
        return product


class ProductForm(forms.ModelForm):                                                                      
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))                    # 
    class Meta:                                                                                             # 
        model = Product                                                                                     # 
        fields = ('title', 'description', 'price', 'adress', 'category', 'phone_number', 'tg_username')     # 
        labels = NewProductForm.Meta.labels

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].label = 'Rasmlar'
