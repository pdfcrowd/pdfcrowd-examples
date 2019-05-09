# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader, StrictUndefined

THIS_DIR = os.path.dirname(__file__)

BUTTONS = """<center class='{}'>
                <input type='submit' value='Convert to PDF' name='asAttachment'>
                <input type='submit' value='Convert to PDF and open' name='asInline'>
            </center>
        </form>"""

BUTTONS_JINJA = BUTTONS.format('{{ pdfcrowd_remove }}')
BUTTONS_ERB = BUTTONS.format('<%= pdfcrowd_remove %>')

FORM = """<form action='#' method='post'>
            <p>
                 <label for='id_first_name'>First name:</label>
                 <input type='text' name='first_name' id='id_first_name' value='{}'>
            </p>
            <p>
                <label for='id_last_name'>Last name:</label>
                <input type='text' name='last_name' id='id_last_name' value='{}'>
            </p>
            <p>
                 <label for='id_part_for_conversion'>Part of the page for the conversion:</label>
                 <select name='part_for_conversion' id='id_part_for_conversion'>
                     <option value='all'>Everything</option>
                     <option value='#font-block'>Custom Font</option>
                     <option value='#chart-block'>Google Chart</option>
                     <option value='#form-block' {}>Dynamic Content</option>
                 </select>
            </p>
            <p>
                 <label for='id_gender'>Gender:</label>
                 <select name='gender' id='id_gender'>
                     <option value=''>------</option>
                     <option value='M' {}>Male</option>
                     <option value='F' {}>Female</option>
                 </select>
            </p>
            <p>
                <label for='id_remove_convert_button'>Remove convert buttons from PDF:</label>
                <input type='checkbox' name='remove_convert_button' id='id_remove_convert_button' {}>
            </p>
            """

def get_form_with_vars(first_name, last_name,
                       part_form,
                       gender_m, gender_f, remove_buttons, buttons):
    return FORM.format(first_name, last_name,
                       part_form,
                       gender_m, gender_f, remove_buttons) + buttons

FORM_JINJA = get_form_with_vars('{{ first_name }}', '{{ last_name }}',
                                '{{ part_form }}',
                                '{{ gender_m }}', '{{ gender_f }}',
                                '{{ remove_buttons }}', BUTTONS_JINJA)

FORM_ERB = get_form_with_vars('<%= first_name %>', '<%= last_name %>',
                              '<%= part_form %>',
                              '<%= gender_m %>', '<%= gender_f %>',
                              '<%= remove_buttons %>', BUTTONS_ERB)

FORM_SPRING = """<form action='#' method='post'>
            <p>
                 <label for='id_first_name'>First name:</label>
                 <input type='text' name='firstName' id='firstName' th:value='${data.firstName}'>
            </p>
            <p>
                <label for='id_last_name'>Last name:</label>
                <input type='text' name='lastName' id='lastName' th:value='${data.lastName}'>
            </p>
                 <label for='gender'>Gender:</label>
                 <select name='gender' id='gender'>
                     <option value=''>------</option>
                     <option value='M' th:selected="${data.gender == 'M'}">Male</option>
                     <option value='F' th:selected="${data.gender == 'F'}">Female</option>
                 </select>
            </p>
            </p>
                 <label for='part_for_conversion'>Part of the page for the conversion:</label>
                 <select name='partForConversion' id='part_for_conversion'>
                     <option value='all'>Everything</option>
                     <option value='#font-block'>Custom Font</option>
                     <option value='#chart-block'>Google Chart</option>
                     <option value='#form-block' th:selected="${data.partForConversion == '#form-block'}">Dynamic Content</option>
                 </select>
            </p>
            <p>
                <label for='removeConvertButton'>Remove convert buttons from PDF:</label>
                <input type='checkbox' name='removeConvertButton' id='removeConvertButton' th:checked='${data.removeConvertButton}'>
            </p>
            <center th:class='${data.removeConvertButton} ? pdfcrowd-remove : dummy'>
                <input type='submit' value='Convert to PDF' name='asAttachment'>
                <input type='submit' value='Convert to PDF and open' name='asInline'>
            </center>
        </form>"""

FORM_ASP_NET = """<form id="form1" runat="server">
            <p>
                <asp:Label AssociatedControlId="firstName" Text="First name:" runat="server" />
                <asp:TextBox id="firstName" runat="server" />
            </p>
            <p>
                <asp:Label AssociatedControlId="lastName" Text="Last name:" runat="server" />
                <asp:TextBox id="lastName" runat="server" />
            </p>
            <p>
                <asp:Label AssociatedControlId="gender" Text="Gender:" runat="server" />
                <asp:DropDownList id="gender" runat="server">
                    <asp:ListItem Text ="Please Select" Value = ""></asp:ListItem>
                    <asp:ListItem Text ="Male" Value ="M"></asp:ListItem>
                    <asp:ListItem Text ="Female" Value ="F"></asp:ListItem>
                </asp:DropDownList>
            </p>
            <p>
                <asp:Label AssociatedControlId="partForConversion" Text="Part of the page for the conversion:" runat="server" />
                <asp:DropDownList id="partForConversion" runat="server">
                    <asp:ListItem Text ="Everything" Value = "all"></asp:ListItem>
                    <asp:ListItem Text ="Custom Font" Value ="#font-block"></asp:ListItem>
                    <asp:ListItem Text ="Google Chart" Value ="#chart-block"></asp:ListItem>
                    <asp:ListItem Text ="Dynamic Content" Value ="#form-block"></asp:ListItem>
                </asp:DropDownList>
            </p>
            <p>
                <asp:Label AssociatedControlId="removeConvertButton" Text="Remove convert buttons from PDF:" runat="server" />
                <asp:CheckBox id="removeConvertButton" runat="server" />
            </p>
            <center id="pdfcrowdRemove" runat="server">
                <asp:Button id="asAttachment" runat="server" Text="Convert to PDF" />
                <asp:Button id="asInline" runat="server" Text="Convert to PDF and open" />
            </center>
        </form>"""

LANGS = (
    ('python/django', {
        'framework': 'Django',
        'lang': 'python',
        'prerequisites': ['python'],
        'cred_file': '[demo/views.py](demo/views.py#L37)',
        'install': [
            'pip install -r requirements.txt'
            ],
        'start': [
            'python manage.py runserver 8080'
            ],
        'form': """<form action='#' method='post'>
            {{% if csrf_token %}}{{% csrf_token %}}{{% endif %}}
            {{{{ form.as_p }}}}
            {}""".format(BUTTONS_JINJA)
        }
     ),
    ('nodejs/nodejs', {
        'framework': 'Node.js Web Server',
        'lang': 'nodejs',
        'install': [
            'npm install'
            ],
        'start': [
            'nodejs server.js'
            ],
        'index_path': 'index.html',
        'prerequisites': ['nodejs', 'npm'],
        'cred_file': '[server.js](server.js#L56)',
        'form': get_form_with_vars('$first_name', '$last_name',
                                   '$part_form',
                                   '$gender_m', '$gender_f',
                                   '$remove_buttons',
                                   BUTTONS.format('$pdfcrowd_remove'))
     }
    ),
    ('nodejs/express', {
        'framework': 'Express',
        'lang': 'nodejs',
        'install': [
            'npm install'
            ],
        'start': [
            'nodejs app.js'
            ],
        'prerequisites': ['nodejs', 'npm'],
        'cred_file': '[app.js](app.js#L55)',
        'form': FORM_JINJA
        }
     ),
    ('php/php', {
        'framework': 'PHP Web Server',
        'lang': 'php',
        'install': [
            'composer install'
            ],
        'start': [
            'php -S localhost:8080 index.php'
            ],
        'prerequisites': ['php', 'composer'],
        'cred_file': '[index.php](index.php#L47)',
        'form': FORM_JINJA
        }
     ),
    ('ruby/rails', {
        'framework': 'Ruby on Rails',
        'lang': 'ruby',
        'install': [
            'gem install rails',
            'bundle install'
            ],
        'start': [
            'rails server -p 8080'
            ],
        'prerequisites': ['ruby', 'ruby-dev', 'ruby-bundler'],
        'cred_file': '[app/controllers/demo_controller.rb](app/controllers/demo_controller.rb#L45)',
        'index_path': 'app/views/demo/index.html.erb',
        'form': FORM_ERB
        }
     ),
    ('java/spring', {
        'framework': 'Spring',
        'lang': 'java',
        'install': [
            './gradlew build',
            ],
        'start': [
            'java -jar build/libs/pdfcrowd-demo-0.1.0.jar'
            ],
        'prerequisites': ['java', 'gradle'],
        'cred_file': '[src/main/java/demo/DemoController.java](src/main/java/demo/DemoController.java#L39)',
        'index_path': 'src/main/resources/templates/index.html',
        'form': FORM_SPRING
        }
     ),
    ('dotnet/asp-net-web-forms', {
        'framework': 'ASP.NET Web Forms',
        'lang': 'dotnet',
        'install': [
            'nuget install -OutputDirectory packages'
            ],
        'start': [
            'xsp --port=8080'
            ],
        'prerequisites': ['.NET', 'XSP'],
        'cred_file': '[Default.aspx.cs](Default.aspx.cs#L55)',
        'index_path': 'Default.aspx',
        'form': FORM_ASP_NET,
        'html_top': '<%@ Page Language="C#" Inherits="PdfcrowdDemo.Default" %>'
        }
     ),
     ('ajax', {
        'framework': 'Ajax Request',
        'lang': 'rest',
        'test': 'index.html in your web browser.',
        'cred_file': '[post_request.js](post_request.js#L48)',
        'index_path': 'index.html',
        'form': FORM.format('', '', '', '', '', '') + """
            <center class='block-button'>
                <input type='submit' value='Convert to PDF'>
            </center>
        </form>""",
        'head': """
        <script type='text/javascript' src='https://code.jquery.com/jquery-3.3.1.min.js'></script>
        <script type='text/javascript' src='post_request.js'></script>
        """
        }
     ),
)

env = Environment(loader=FileSystemLoader(THIS_DIR),
                  keep_trailing_newline=True)
env.trim_blocks = True
env.lstrip_blocks = True

html_template = env.get_template('index.html.tpl')
readme_template = env.get_template('README.md.tpl')

for framework_dir, ctx in LANGS:
    if 'html_top' not in ctx:
        ctx['html_top'] = '<!DOCTYPE html>'
    framework_dir = os.path.join(THIS_DIR, '..', framework_dir)
    with open(os.path.join(framework_dir, 'README.md'), 'w') as out:
        out.write(readme_template.render(ctx).encode('utf-8'))
    index_path = ctx.get('index_path', 'templates/index.html')
    with open(os.path.join(framework_dir, index_path), 'w') as out:
        out.write(html_template.render(ctx).encode('utf-8'))
