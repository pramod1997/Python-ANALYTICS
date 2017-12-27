from django import forms
from .models import *


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document','seasonal_length','forecast_period','holt_w',)



class ArimaForm(forms.ModelForm):
	class Meta : 
		model = Arima 
		fields = ('document',)

class CrostonForm(forms.ModelForm):
	class Meta:
		model=Croston
		fields = ('document',)


class FbprophetForm(forms.ModelForm):
	class Meta:
		model=Fbprophet
		fields = ('document',)


class 	DecompositionForm(forms.ModelForm):
	class Meta:
		model=Decomposition
		fields = ('document',)