# Pdfcrowd & {{ framework }} Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

{% if prerequisites %}
```
{% for req in prerequisites %}
{{ req }}
{% endfor %}
```
{% endif %}

{% if install %}
## Installing

```
{% for line in install %}
{{ line }}
{% endfor %}
```
{% endif %}

{% if start %}
## Web Server Start

```
{% for line in start %}
{{ line }}
{% endfor %}
```
{% endif %}

## Test

   Open a sample web page {% if test %}{{ test }}{% else %}<http://localhost:8080/>{% endif %}


   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Pdfcrowd API License

   If you wish to use your Pdfcrowd API license, replace **demo** credentials with your Pdfcrowd username and API key in **{{ cred_file }}** file.
   A [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) API license can be used too.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/{{ lang }}/>
