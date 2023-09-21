from django.core.files import File
from django.utils.text import Truncator
from django.utils.text import slugify
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
    name = models.CharField(max_length=255,blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    url = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to="uploads/resumes/", blank=True, unique=False, null=True)
    
    class Meta:
        app_label = 'page_details' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def generate_slug(self):
        truncated_content = Truncator(self.name).chars(20)
        slug_text = slugify(truncated_content)
        return slug_text
    
    def get_slug(self):
        return self.slug

    def get_resume_html(self):
        if self.resume:
            resume_path = self.resume.path
            return convert_docx_to_html(resume_path)
        return ''
    
    def get_resume_url(self):
        if self.resume:
            return self.resume.path
        return None

    def get_resume_file(self):
        if self.resume:
            with open(self.resume.path, 'rb') as resume_file:
                opened_file = resume_file.read()
            return opened_file
        return None