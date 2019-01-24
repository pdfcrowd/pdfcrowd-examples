<?php

require_once __DIR__.'/bootstrap.php';

if($_SERVER['REQUEST_METHOD'] == 'GET') {
    // GET request section
    // just render HTML
    echo $twig->render('index.html');
    return;
}

// POST request section

// prepare data set for HTML rendering
// make dropdown controls to show selected values
// by setting 'selected' attribute
if($_POST['part_for_conversion'] == '#form-block') {
    $_POST['part_form'] = 'selected';
}
if($_POST['gender'] == 'F') {
    $_POST['gender_f'] = 'selected';
} else if($_POST['gender'] == 'M') {
    $_POST['gender_m'] = 'selected';
}

if(array_key_exists('remove_convert_button', $_POST) && $_POST['remove_convert_button'] == 'on') {
    // remove convert buttons from PDF
    $_POST['pdfcrowd_remove'] = 'pdfcrowd-remove';

    // set test checkbox to be checked properly
    $_POST['remove_buttons'] = 'checked';
}

// prepare HTML content for a conversion
$html = $twig->render('index.html', $_POST);

// choose a content disposition
$content_disp = 'inline';
if(array_key_exists('asAttachment', $_POST)) {
    $content_disp = 'attachment';
}

// run HTML to PDF conversion
try
{
    // enter your Pdfcrowd credentials to the converter's constructor
    $client = new \Pdfcrowd\HtmlToPdfClient('your_username', 'your_apikey');

    if($_POST['part_for_conversion'] != 'all') {
        // convert just selected part of the page
        $client->setElementToConvert($_POST['part_for_conversion']);
    }

    // running Pdfcrowd HTML to PDF conversion
    $pdf = $client->convertString($html);

    header('Content-Type: application/pdf');
    header('Cache-Control: no-cache');
    header('Accept-Ranges: none');
    header("Content-Disposition: $content_disp; filename=\"demo_php.pdf\"");

    // return the final PDF in the response
    echo $pdf;
}
catch(\Pdfcrowd\Error $why)
{
    error_log("Pdfcrowd Error: {$why}\n");
    // return error in the response
    echo $why;
}

?>
