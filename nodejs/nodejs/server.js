"use strict";

const http = require('http');
const fs = require('fs');
const pdfcrowd = require('pdfcrowd');
const querystring = require('querystring');

// define form fields and thier default values
// we don't use any HTML template engine, to be more demonstrative
const FORM_FIELDS = {
    'first_name': '',
    'last_name': '',
    'gender_m': '',
    'gender_f': '',
    'remove_buttons': '',
    'pdfcrowd_remove': ''
    }

http.createServer(function (req, res) {
    if (req.method === 'POST') {
        var body = '';
        req.on('data', function (chunk) {
            body += chunk.toString();
        });
        req.on('end', function () {
            var data = querystring.parse(body);
            var content_disp = data.asAttachment ? 'attachment' : 'inline';
            var callbacks = pdfcrowd.sendPdfInHttpResponse(res,
                                                           'demo_nodejs.pdf',
                                                           content_disp);
            if(data.gender == 'F') {
                data.gender_f = 'selected';
            } else if(data.gender == 'M') {
                data.gender_m = 'selected';
            }

            if(data.remove_convert_button === 'on') {
                // remove buttons
                data.pdfcrowd_remove = 'pdfcrowd-remove';
                data.remove_buttons = 'checked';
            }

            var html = fs.readFileSync('index.html').toString();
            for(let key in FORM_FIELDS) {
                html = html.replace('$' + key, data[key]);
            }

            // enter your Pdfcrowd credentials to the converter's constructor
            var client = new pdfcrowd.HtmlToPdfClient('your_username', 'your_apikey');

            console.log('running Pdfcrowd HTML to PDF conversion');
            client.convertString(html, callbacks);
        });
    }
    else
    {
        var html = fs.readFileSync('index.html').toString();
        // set defaults to the form
        for(let key in FORM_FIELDS) {
            html = html.replace('$' + key, FORM_FIELDS[key]);
        }
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(html);
    }
}).listen(8080);
