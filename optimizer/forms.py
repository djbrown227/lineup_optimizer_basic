from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV File")
    sport = forms.ChoiceField(
        choices=[
            ('NBA', 'NBA'),
            ('NFL', 'NFL'),
            ('MLB', 'MLB'),
            ('GOLF', 'Golf'),
            ('NHL', 'NHL'),
            ('SOCCER', 'Soccer'),
            ('CFL', 'CFL'),
            ('CFB', 'CFB'),
            ('LOL', 'LOL'),
            ('MMA', 'MMA'),
            ('NASCAR', 'Nascar'),
            ('TENNIS', 'Tennis'),
            ('CSGO', 'CSGO'),
        ],
        label="Sport",
    )
    site = forms.ChoiceField(
        choices=[
            ('YAHOO', 'Yahoo'),
            ('DRAFTKINGS', 'DraftKings'),
            ('FANDUEL', 'FanDuel'),
            ('FANTASYDRAFT', 'FantasyDraft'),
            ('FANBALL', 'Fanball')
        ],
        label="Site",
    )
    num_lineups = forms.IntegerField(min_value=1, label="Number of Lineups")
    
    # New fields for exposure settings
    min_exposure = forms.FloatField(
        required=False,
        label="Minimum Exposure (%)",
        min_value=0,
        max_value=100,
        initial=0,
        help_text="Minimum percentage of lineups this player should appear in."
    )
    max_exposure = forms.FloatField(
        required=False,
        label="Maximum Exposure (%)",
        min_value=0,
        max_value=100,
        initial=100,
        help_text="Maximum percentage of lineups this player should appear in."
    )
