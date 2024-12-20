from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV File")
    sport = forms.ChoiceField(
        choices=[
            ('NBA', 'NBA'),
            ('NFL', 'NFL'),
            ('MLB', 'MLB'),
            ('GOLF', 'Golf')
        ],
        label="Sport",
    )
    site = forms.ChoiceField(
        choices=[
            ('YAHOO', 'Yahoo'),
            ('DRAFTKINGS', 'DraftKings'),
            ('FANDUEL', 'FanDuel'),
        ],
        label="Site",
    )
    num_lineups = forms.IntegerField(min_value=1, label="Number of Lineups")
