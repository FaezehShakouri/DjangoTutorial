from django.forms import ModelForm, Form, RadioSelect, ChoiceField
from .models import Favorite

class FavoriteForm(ModelForm):
    class Meta:
        model = Favorite
        fields = ['word']

class FavForm(Form):
    favs = ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(FavForm, self).__init__(*args, **kwargs)
        self.fields['favs'].choices = [(x.pk, x.word) for x in Favorite.objects.all()]
