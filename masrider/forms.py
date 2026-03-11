from django import forms
from .models import MasRider, CompetitionHistory, Ability


class MasRiderForm(forms.ModelForm):
    class Meta:
        model = MasRider
        fields = ['name', 'alias', 'age', 'series', 'organization',
                  'transformation_device', 'abilities', 'bio', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อจริง'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อมาสไรเดอร์'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 150}),
            'series': forms.Select(attrs={'class': 'form-select'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'transformation_device': forms.TextInput(attrs={'class': 'form-control'}),
            'abilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 1 or age > 150):
            raise forms.ValidationError("อายุต้องอยู่ระหว่าง 1 ถึง 150 ปี")
        return age

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 2:
            raise forms.ValidationError("ชื่อต้องมีอย่างน้อย 2 ตัวอักษร")
        return name


class CompetitionHistoryForm(forms.ModelForm):
    class Meta:
        model = CompetitionHistory
        fields = ['opponent', 'event_name', 'event_date', 'result', 'description']
        widgets = {
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class AbilityForm(forms.ModelForm):
    class Meta:
        model = Ability
        fields = ['name', 'description', 'power_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'power_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 100}),
        }

    def clean_power_level(self):
        level = self.cleaned_data.get('power_level')
        if level is not None and (level < 1 or level > 100):
            raise forms.ValidationError("ระดับพลังต้องอยู่ระหว่าง 1 ถึง 100")
        return level
