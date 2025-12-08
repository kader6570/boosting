from django import forms
from . models import Inscription

class FormInscription(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['numero','tiktok_username']
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'w-full py-3 pl-11 pr-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-base text-gray-800 transition duration-150',
                'placeholder': 'Entrez votre numero',
            }),
            'tiktok_username': forms.TextInput(attrs={
                'class': 'w-full py-3 pl-11 pr-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 text-base text-gray-800 transition duration-150',
                'placeholder': '@votrepseudo',
            }),
            # Répétez pour tous les autres champs...
        }