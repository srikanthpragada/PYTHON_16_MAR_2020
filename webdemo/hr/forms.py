import django.forms as forms


class DiscountForm(forms.Form):
    amount = forms.IntegerField(label="Selling Amount")
    rate = forms.FloatField(label="Discount Rate")



class JobForm(forms.Form):
    pass

