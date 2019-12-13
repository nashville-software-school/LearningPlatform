# Below is based on this article: https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django/
from django.http import HttpResponse
from django.template.loader import get_template
from django.forms.models import model_to_dict
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import os

from io import BytesIO
from xhtml2pdf import pisa


def generate_pdf(template_src, instance):
    template = get_template(template_src)
    data = {'de': model_to_dict(instance)}
    # model_to_dict doesn't work with foreign key values, so have to insert those back in.
    data["de"]["student"] = instance.student
    data["de"]["instructor"] = instance.instructor
    data["de"]["created"] = instance.created
    data["de"]["cohort_type"] = instance.cohort_type
    data["de"]["disengagement_type"] = instance.disengagement_type
    data["de"]["reason"] = instance.reason
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def send_pdf_email(pdf, data):
  draft_email = EmailMessage(
            'Student disengagement document ready for signatures', #subject
            f'An agreement for the withdrawal of {data.student.full_name} has been created, and is ready to be signed by the student and the instructor, {data.instructor.full_name}', #body
            'joeshepmedia@gmail.com', #from
            ('joeshep@nashvillesoftwareschool.com',) #to
          )
  pdf_file = os.path.join(settings.MEDIA_ROOT, pdf)
  draft_email.attach_file(pdf_file)
  draft_email.send()
