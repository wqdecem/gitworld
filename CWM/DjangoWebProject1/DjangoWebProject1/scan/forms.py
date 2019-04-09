from django import forms

class ScanDIRForm(forms.Form):
    scan_dir = forms.CharField(label='Scan DIR', max_length=256)
