package demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.BindingResult;
import org.springframework.http.ResponseEntity;
import org.springframework.http.MediaType;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.ui.ModelMap;
import javax.validation.Valid;
import com.pdfcrowd.*;
import org.thymeleaf.context.Context;
import org.thymeleaf.TemplateEngine;

@Controller
public class DemoController {
    @Autowired
    private TemplateEngine templateEngine;

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("data", new TestForm());
        return "index";
    }

    @RequestMapping(value = "/", method = RequestMethod.POST,
                    produces = {MediaType.APPLICATION_PDF_VALUE})
    public ResponseEntity<byte[]> convertToPdf(@Valid @ModelAttribute("data") TestForm data,
      BindingResult result, ModelMap model) {
        // enter your Pdfcrowd credentials to the converter's constructor
        Pdfcrowd.HtmlToPdfClient client = new Pdfcrowd.HtmlToPdfClient(
            "demo", "ce544b6ea52a5621fb9d55f8b542d14d");

        if(!data.getPartForConversion().equals("all")) {
            // convert just selected part of the page
            client.setElementToConvert(data.getPartForConversion());
        }

        HttpHeaders headers = new HttpHeaders();
        headers.add("Cache-Control", "max-age=0");
        headers.add("Accept-Ranges", "none");
        String contentDisp = data.getAsAttachment() == null || data.getAsAttachment().isEmpty() ? "inline" : "attachment";
        headers.add("Content-Disposition", contentDisp + "; filename=demo_spring.pdf");

        Context context = new Context();
        context.setVariable("data", data);
        String html = templateEngine.process("index", context);

        // convert a web page and store the generated PDF to a variable
        byte[] pdf = client.convertString(html);
        return new ResponseEntity<>(pdf, headers, HttpStatus.OK);
    }
}
