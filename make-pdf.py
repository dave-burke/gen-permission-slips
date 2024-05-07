import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from weasyprint import HTML

def format_datetime(datetime_string, format_string):
    datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M')
    return datetime_obj.strftime(format_string)

def render_template(template_file, data_file):
    # Load data from YAML file
    with open(data_file, 'r') as f:
        data = yaml.safe_load(f)

    # Create Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    env.filters['format_datetime'] = format_datetime

    # Load HTML template
    template = env.get_template(template_file)

    # Render the data into the template
    return template.render(data)

if __name__ == "__main__":
    # Paths to template, data, and output files
    template_file = sys.argv[1]
    data_file = sys.argv[2]
    output_file = sys.argv[3]

    # Render template
    rendered_content = render_template(template_file, data_file)

    # with open('debug.html', 'w') as f:
        # f.write(rendered_content)

    # Write the PDF
    HTML(string=rendered_content).write_pdf(target=output_file, pdf_forms=True, optimize_images=True)
