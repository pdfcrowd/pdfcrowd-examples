using System;
using System.IO;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Linq;

namespace PdfcrowdDemo
{

    public partial class Default : System.Web.UI.Page
    {
		protected override void Render(HtmlTextWriter writer)
		{
			if(Request.HttpMethod == "GET")
			{
				base.Render(writer);
				return;
			}

			if (removeConvertButton.Checked)
			{
				pdfcrowdRemove.Attributes.Add("class", "pdfcrowd-remove");
			}

			// write this html to string
			StringBuilder stringBuilder = new StringBuilder();
			StringWriter stringWriter = new StringWriter(stringBuilder);

			HtmlTextWriter htmlWriter = new HtmlTextWriter(stringWriter);

            base.Render(htmlWriter);

			System.Console.WriteLine("running Pdfcrowd HTML to PDF conversion");
			byte[] pdf = ConvertHtml(stringBuilder.ToString());

			// set HTTP response headers
			Response.ContentType = "application/pdf";
			Response.Headers.Add("Cache-Control", "max-age=0");
			Response.Headers.Add("Accept-Ranges", "none");
			string contentDisp = Request.Form.AllKeys.Contains("asAttachment") ? "attachment" : "inline";
			Response.Headers.Add("Content-Disposition", contentDisp + "; filename=\"demo_asp_net.pdf\"");

            // write PDF to the response
			Response.OutputStream.Write(pdf, 0, pdf.Length);
            Response.Flush();
		}

		private byte[] ConvertHtml(string html)
		{
			try
            {
				// enter your Pdfcrowd credentials to the converter's constructor
                pdfcrowd.HtmlToPdfClient client = new pdfcrowd.HtmlToPdfClient(
					"your_username", "your_apikey");

				if(partForConversion.SelectedValue != "all")
                {
					// convert just selected part of the page
					client.setElementToConvert(partForConversion.SelectedValue);
                }

                // run the conversion and write the result to a file
                return client.convertString(html);
            }
            catch (pdfcrowd.Error why)
            {
                // report the error
                System.Console.Error.WriteLine("Pdfcrowd Error: " + why);

                // handle the exception here or rethrow and handle it at a higher level
				throw new HttpException(why.ToString());
            }
		}
    }
}
