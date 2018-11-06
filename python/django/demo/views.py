import logging
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django import forms

import pdfcrowd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    gender = forms.ChoiceField(
        required=False,
        choices=(('', '------'),
                 ('M', 'Male'),
                 ('F', 'Female')))
    remove_convert_button = forms.BooleanField(required=False, label='Remove convert buttons from PDF')

def index(request):
    form = TestForm(request.POST)
    response = render(request, 'index.html', {
        'form': form,
        'pdfcrowd_remove': 'pdfcrowd-remove' if form.data.get('remove_convert_button') else ''
        })

    if request.method != 'POST':
        return response

    try:
        # enter your Pdfcrowd credentials to the converter's constructor
        client = pdfcrowd.HtmlToPdfClient('your_username', 'your_apikey')

        # convert a web page and store the generated PDF to a variable
        logger.info('running Pdfcrowd HTML to PDF conversion')
        pdf = client.convertString(response.content)

        # set HTTP response headers
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Cache-Control'] = 'max-age=0'
        pdf_response['Accept-Ranges'] = 'none'
        content_disp = 'attachment' if 'asAttachment' in request.POST else 'inline'
        pdf_response['Content-Disposition'] = content_disp + '; filename=demo_django.pdf'

        # send the generated PDF
        pdf_response.write(pdf)
        return pdf_response
    except pdfcrowd.Error as why:
        logger.error('Pdfcrowd Error: %s', why)
        return HttpResponse(why)
