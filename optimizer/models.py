from django.db import models

class UploadedCSV(models.Model):
    csv_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # New fields for exposure settings
    min_exposure = models.FloatField(
        default=0,
        help_text="Minimum percentage of lineups this player should appear in."
    )
    max_exposure = models.FloatField(
        default=100,
        help_text="Maximum percentage of lineups this player should appear in."
    )
