import sys
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
    part_for_conversion = forms.ChoiceField(
        required=False,
        label='Part of the page for the conversion',
        choices=(('all', 'Everything'),
                 ('#font-block', 'Custom Font'),
                 ('#chart-block', 'Google Chart'),
                 ('#form-block', 'Dynamic Content')))
    remove_convert_button = forms.BooleanField(required=False, label='Remove convert buttons from PDF')

def index(request):
    form = TestForm(request.POST)
    if request.method != 'POST':
        return render(request, 'index.html', {'form': form})

    try:
        # enter your Pdfcrowd credentials to the converter's constructor
        client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

        part = request.POST.get('part_for_conversion')
        if part != None and part != 'all':
            # convert just selected part of the page
            client.setElementToConvert(part)

        # convert a web page and store the generated PDF to a variable
        logger.info('running Pdfcrowd HTML to PDF conversion')

        # set HTTP response headers
        response = HttpResponse(content_type='application/pdf')
        response['Cache-Control'] = 'max-age=0'
        response['Accept-Ranges'] = 'none'
        content_disp = 'attachment' if 'asAttachment' in request.POST else 'inline'
        response['Content-Disposition'] = content_disp + '; filename=demo_django.pdf'

        html = render_to_string(
            'index.html', {
                'form': form,
                'pdfcrowd_remove': 'pdfcrowd-remove' if form.data.get('remove_convert_button') else ''
                })
        client.convertStringToStream(html, response)

        # send the generated PDF
        return response
    except pdfcrowd.Error as why:
        logger.error('Pdfcrowd Error: %s', why)
        return HttpResponse(why)
