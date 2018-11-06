package demo;

import lombok.Data;

@Data
class TestForm {

    private String firstName;
    private String lastName;
    private String gender;
    private Boolean removeConvertButton;
    private String asAttachment;

    TestForm() {
    }
}
