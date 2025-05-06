from django import forms
from .models import data




class bangdata(forms.ModelForm):
    class Meta:
        model = data
        fields = ['fecha','usuario', 'planta','hostname','departamento','serialnumber','activofijo','tipodeequipo','marca','modelo','ipaddress','procesador','os','ram','hdd','epc','tenable','sophos','borrartemporales','encriptacionhdd','updates','imgantes','imgdespues','tempcpu','imgtemp','imgagent','limpinterna','limpexterna','limpram','limpteclado','limpventilador','limppasta','aplicacionpasta','limpiezadisipador','nombretech','empresa','comentarios']

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'planta': forms.TextInput(attrs={'class': 'form-control'}),
            'hostname': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'serialnumber': forms.TextInput(attrs={'class': 'form-control'}),
            'activofijo': forms.NumberInput(attrs={'class': 'form-control'}),  
            'tipodeequipo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ipaddress': forms.TextInput(attrs={'class': 'form-control'}), 
            'procesador': forms.TextInput(attrs={'class': 'form-control'}),
            'os': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'hdd': forms.TextInput(attrs={'class': 'form-control'}),
            'epc': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'tenable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sophos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'borrartemporales': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'encriptacionhdd': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'updates': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imgantes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  
            'imgdespues': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'tempcpu': forms.TextInput(attrs={'class': 'form-control'}),
            'imgtemp': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imgagent': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'limpinterna': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limpexterna': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limpram': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limpteclado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limpventilador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limppasta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'aplicacionpasta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limpiezadisipador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nombretech': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }


     
       


