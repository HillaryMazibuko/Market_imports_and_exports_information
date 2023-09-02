from django import forms



class InputForm(forms.Form):
    product = forms.CharField(label='product', max_length=100)
    quantity = forms.CharField(label='quantity', max_length=100)
    Country = forms.CharField(label='Country', max_length=100)
    
