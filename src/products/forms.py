from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Item name"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Item description",
                "class": "my-new-class",
                "id": "my-new-id-i-can-use-in-css",
                "row": 10,
                "column": 50
            }
        ))

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "summary"
        ]

    def clean_name(self, *args, **kwars):
        '''
        The reason for this function is to define custom validation for form fields.
        The clean data is what is received after django validation, now we are going to define
        our own custom validation. In this example we are checking for CFE to be in the name
        :param args:
        :param kwars:
        :return:
        '''
        name = self.cleaned_data.get("name")
        if not "CFE" in name:
            raise forms.ValidationError("This is not a valid name")
        else:
            return name

# We should use the model.form as per django documentation
class RawProductForm(forms.Form):
    """
    This class was created for illustration purpose. The ModelForm is the main class to be
    used when saving data to the database.
    """
    name = forms.CharField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "my-new-class",
                "id": "my-new-id-i-can-use-in-css",
                "row": 10,
                "column": 50
            }
        ))
    price = forms.DecimalField()
    summary = forms.CharField()
