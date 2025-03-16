from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    drive_link = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def embed_link(self):
        """Convert Google Drive shareable link to an embeddable iframe link"""
        if "drive.google.com" in self.drive_link:
            file_id = self.drive_link.split('/d/')[1].split('/')[0]
            return f"https://drive.google.com/file/d/{file_id}/preview"
        return self.drive_link

    def __str__(self):
        return self.title
