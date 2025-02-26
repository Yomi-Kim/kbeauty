from django import forms
from .models import Product
from django.core.validators import MinLengthValidator

class ProductForm(forms.ModelForm):
    class Meta:
        description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "minlength": "10"}),  
        validators=[MinLengthValidator(10, message="설명은 최소 10자 이상 입력해야 합니다.")]
    )
        model = Product
        fields = ["name", "price", "stock", "description"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "제품명 입력"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": "0"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "step": "1", "min": "0"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "cols": 50, "placeholder": "제품 설명 입력"}),
        }

# 가격 소수점 아래 0 제거
    def clean_price(self):
        price = self.cleaned_data.get("price")
        return float(price) if price % 1 != 0 else int(price)
