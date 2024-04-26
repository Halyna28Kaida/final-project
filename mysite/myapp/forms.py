from datetime import datetime
from django import forms
from myapp.models import Order, Tour, Review, Buscket


class TourCreateForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = ['name', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 
                  'beginning', 'image', 'adult_price', 'tour_type', 'place_quantity']
        

class BuscketCreateForm(forms.ModelForm):
        

    

    def __init__(self, *args, **kwargs):

        beginning = kwargs.pop('beginning', None)
        place_quantity = kwargs.pop('place_quantity', None)
        

        super().__init__(*args, **kwargs)

        min_day_value = datetime.today().strftime("%Y-%m-%d")


        if place_quantity:
            self.fields['person_quantity'] = forms.ChoiceField(
                label='Количество человек',
                choices=[(i, str(i)) for i in range(1, place_quantity + 1)],
                widget=forms.Select(attrs={'class': 'input'}),
            )

        if beginning is not None:
            self.fields['time'] = forms.ChoiceField(
                label='Время', 
                choices=[(beginning, beginning.strftime('%H:%M'))],
                widget=forms.Select(attrs={'class': 'input'}),
            )



    class Meta:
        model = Buscket
        fields = ['date', 'time', 'person_quantity']


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        first_name = kwargs.pop('first_name', None)
        last_name = kwargs.pop('last_name', None)

        super().__init__(*args, **kwargs)  
    
        if first_name:  
            self.fields['first_name'] = forms.CharField(
                label='Имя',
                widget=forms.TextInput(attrs={'class': 'input'}),
            )
    
        if last_name:
            self.fields['last_name'] = forms.CharField(
                label='Фамилия',
             widget=forms.TextInput(attrs={'class': 'input'}),
            )

    class Meta:
            model = Order
     
            fields = ['buyer', 'phone_number', 'email', 'tour', 'amount']



class ReviewCreateForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text']


