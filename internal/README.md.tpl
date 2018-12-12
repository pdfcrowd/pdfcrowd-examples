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

Replace **'your_username'** with your Pdfcrowd username and **'your_apikey'** with your Pdfcrowd API key in **{{ cred_file }}** file. Sign up for a [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) if you don't have the credentials.

{% if install %}
## Installing

```
{% for line in install %}
{{ line }}
{% endfor %}
```
{% endif %}

{% if start %}
## Web server start

```
{% for line in start %}
{{ line }}
{% endfor %}
```
{% endif %}

## Test

   Open a sample web page {% if test %}{{ test }}{% else %}<http://localhost:8080/>{% endif %}


   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/{{ lang }}/>
