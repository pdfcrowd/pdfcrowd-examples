window.onload = function() {
    function preserve_form_values() {
        // set form values according current values
        $('input:text').each(function() {
            $(this).attr('value', $(this).val());
        });

        $('input:checkbox').each(function() {
            if($(this).is(':checked')) {
                $(this).attr('checked', 'on');
            } else {
                $(this).removeAttr('checked');
            }
        });

        $('select').find('option').each(function() {
            if($(this).is(':selected')) {
                $(this).attr('selected', 'selected');
            } else {
                $(this).removeAttr('selected');
            }
        });
    }

    $('form').submit(function(e) {
        e.preventDefault(); //prevent form from submitting

        // prepare HTML according form options
        preserve_form_values();

        if($('#id_remove_convert_button:checked').length > 0) {
            // demonstrate usage of pdfcrowd-remove class
            $('.block-button').addClass('pdfcrowd-remove');
        } else {
            $('.block-button').removeClass('pdfcrowd-remove');
        }

        var data = {
            'text': document.documentElement.innerHTML
        };

        // demonstrate conversion of a part of HTML
        var el_to_convert = $('#id_part_for_conversion').val();
        if( el_to_convert != 'all') {
            data['element_to_convert'] = el_to_convert;
        }

        var token = btoa('demo:ce544b6ea52a5621fb9d55f8b542d14d');
        $.ajax({
            type: 'POST',
            url: 'https://api.pdfcrowd.com/convert/',
            data: data,
            headers: {
                'Authorization' : 'Basic ' + token
            },
            xhrFields: {
                responseType: 'blob'
            },
            success: function(data, xhr) {
                var blob = new Blob([data], {type: 'application/pdf'});
                // IE doesn't allow using a blob object directly as link href
                // instead it is necessary to use msSaveOrOpenBlob
                if (window.navigator && window.navigator.msSaveOrOpenBlob) {
                    window.navigator.msSaveOrOpenBlob(blob);
                    return;
                }

                // For other browsers:
                // Create a link pointing to the ObjectURL containing the blob.
                const url = window.URL.createObjectURL(blob);
                var link = document.createElement('a');
                link.href = url;
                link.download = 'test_ajax.pdf';
                link.click();
                setTimeout(function(){
                    // For Firefox it is necessary to delay revoking the ObjectURL
                    window.URL.revokeObjectURL(url);
                }, 100);
            },
            error: function(xhr) {
                alert(xhr.responseText);
            }
        });
    });
};
