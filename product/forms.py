from django import forms
from product.models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.DecimalField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ("name", "discount", "marked_price")
        exclude = ("display_price", "status", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def clean_marked_price(self):
        marked_price = self.cleaned_data.get("marked_price")
        if marked_price <= 0:
            raise forms.ValidationError("Price can not be less than zero.")
        return marked_price