from django.core.files import File
from django.db import models
import mammoth

def user_directory_path(instance, filename):
    return f'uploads/{instance.user.username}/{filename}'

def convert_docx_to_html(docx_file):
    result = mammoth.convert_to_html(docx_file)
    html = result.value
    return html

if __name__ == "__main__":
    docx_file_path = "document.docx"
    converted_html = convert_docx_to_html(docx_file_path)

class PageDetails(models.Model):
    url = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to="uploads/resumes/", blank=True, unique=False, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_resume(self):
        if self.resume:
            resume_path = self.resume.path  # Get the file path of the resume
            return convert_docx_to_html(resume_path)
        return ''