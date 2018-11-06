require 'pdfcrowd'

class DemoController < ApplicationController
    protect_from_forgery except: :index

    # use the same routing point for GET and POST
    def index
        data = {
            :first_name => '',
            :last_name => '',
            :gender_m => '',
            :gender_f => '',
            :remove_buttons => '',
            :pdfcrowd_remove => ''
        }
        if request.post?
            data.each do |key, value|
                data[key] = params[key]
            end

            if params[:gender] == 'F'
                data[:gender_f] = 'selected'
            elsif params[:gender] == 'M'
                data[:gender_m] = 'selected'
            end

            if params[:remove_convert_button] == 'on'
                # remove convert buttons from PDF
                data[:pdfcrowd_remove] = 'pdfcrowd-remove'

                # set test checkbox to be checked properly
                data[:remove_buttons] = 'checked'
            end

            html = render_to_string('demo/index', :locals => data)

            begin
                # enter your Pdfcrowd credentials to the converter's constructor
                client = Pdfcrowd::HtmlToPdfClient.new('your_username', 'your_apikey')

                # convert a web page and store the generated PDF to a variable
                logger.info 'running Pdfcrowd HTML to PDF conversion'
                pdf = client.convertString(html)

                content_disp = params['asAttachment'] ? 'attachment' : 'inline'
                send_data pdf,
                          :type => 'application/pdf',
                          :disposition => content_disp,
                          :filename => 'demo_rails.pdf'
            rescue Pdfcrowd::Error => why
                # report the error
                logger.error "Pdfcrowd Error: #{why}"
                raise
            end
        else
            render 'demo/index', :locals => data
        end
    end
end
