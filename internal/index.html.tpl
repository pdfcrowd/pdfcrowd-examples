{{ html_top }}
<html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
    <head>
        <meta charset='utf-8'/>
        <meta name='google' content='notranslate'>
        <meta http-equiv='Content-Language' content='en'>

        <title>HTML to PDF in {{ framework }} by Pdfcrowd API</title>

        <style>
         html {
             background-color: white;
         }
         body {
             font-size: 110%;
             background-color: #CCCCCC;
             padding: 0.5em;
             width: 700px;
             margin: 0 auto;
         }
         .block {
             border-radius: 10px;
             -moz-border-radius: 10px;
             -webkit-border-radius: 10px;
             border: 1px solid #1e5786;
             padding: 1em;
             background-color: white;
             margin: 0.5em auto;
             width: fit-content;
         }
         h1 {
             font-size: 30px;
             margin-top: 0;
         }
         h2 {
             font-size: 26px;
             margin-top: 0;
         }
         form {
             margin-bottom: 0;
         }
         p {
             margin: 0;
         }
         input, select {
             margin: 0.5em;
             height: 2.2em;
             background-color: khaki;
         }
         input[type='checkbox'] {
             width:20px;
             height: 20px;
         }
         input[type=submit] {
             height: 3em;
             background-color: #2a7abb;
             color: white;
         }
         @font-face
         {
             font-family: 'UniqueRegular';
             src: url(https://storage.googleapis.com/pdfcrowd-public/Unique.ttf) format('truetype');
             font-weight: normal;
             font-style: normal;
         }
        </style>
    </head>
    <body>
        <a style='float: right' href='https://pdfcrowd.com'>
            <img src='https://pdfcrowd.com/static/images/pdfcrowd_icon_48.png'/>
        </a>
        <h1>HTML to PDF in {{ framework }} by Pdfcrowd API</h1>
        <p>This page demonstrates <a href='https://pdfcrowd.com/doc/api/html-to-pdf/{{ lang }}/'>HTML to PDF</a> conversion by <a href='https://pdfcrowd.com/doc/api/'>Pdfcrowd API v2</a> for static and dynamic content.</p>

        <div class='block' id='font-block'>
            <h2>Custom Font</h2>
            <div style='font-size: 12pt; font-family: "UniqueRegular";'>
                <p>ABCČĆDĐEFGHIJKLMNOPQRSŠTUVWXYZŽabcčćdđefghijklmnopqrsštuvwxyzž</p>
                <p>กขคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮะาเใไโฤฤๅ</p>
                <p>1234567890๐๑๒๓๔๕๖๗๘๙‘?’“!”(%)[#]{@}/&\&lt;-+÷×=&gt;®$€£¥¢:;,.*ๆฯฯฯ๏๚๛฿</p>
            </div>
        </div>

        <div class='block' id='chart-block'>
            <h2>Google Chart</h2>
            <div id='piechart' style='width: 400px'></div>
        </div>

        <script type='text/javascript' src='https://www.gstatic.com/charts/loader.js'></script>
        <script type='text/javascript'>
         google.charts.load('current', {'packages':['corechart']});
         google.charts.setOnLoadCallback(drawChart);

         function drawChart() {
             var data = google.visualization.arrayToDataTable([
                 ['Food', 'Preffered'],
                 ['Fruit', 8],
                 ['Vegetable', 7],
                 ['Meat', 4]
             ]);

             var chart = new google.visualization.PieChart(document.getElementById('piechart'));
             chart.draw(data, {
                 chartArea: {
                     left: 40,
                     top: 10,
                     width: '100%',
                     height: 350
                 }
             });
         }
        </script>

        <div class='block' id='form-block'>
            <h2>Dynamic Content</h2>
            <p>Fill out the form to see the data in PDF. Select what you want to convert.</p>
            {{ form }}
        </div>

        <hr style='page-break-before: always;'>

        <h3>NOTES</h3>
        <ul>
          <li>This demo uses API method <a href='https://pdfcrowd.com/doc/api/html-to-pdf/{{ lang }}/#convert_string'>convertString</a>. If your web server has public URLs, you can use simplier solution with <a href='https://pdfcrowd.com/doc/api/html-to-pdf/{{ lang }}/#convert_url'>convertUrl</a> method.</li>
          <li>The remote font must be served with HTTP header 'Access-Control-Allow-Origin: *' to enable <a href='https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS'>CORS</a>.</li>
          <li>The page break is placed always before NOTES section. It demonstrates the CSS rule <em>page-break-before: always;</em></li>
        </ul>
    </body>
</html>
