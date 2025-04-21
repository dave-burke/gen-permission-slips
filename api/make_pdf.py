import sys
import yaml
from jinja2 import Environment, BaseLoader
from datetime import datetime
from weasyprint import HTML

def format_datetime(datetime_string, format_string):
    valid_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%d']
    for fmt in valid_formats:
        try:
            datetime_obj = datetime.strptime(datetime_string, fmt)
            return datetime_obj.strftime(format_string)
        except ValueError:
            continue
    raise ValueError(f"Invalid datetime format: {datetime_string}")

def render_template(template_content, data_yaml):
    # Create Jinja2 environment
    env = Environment(loader=BaseLoader)
    env.filters['format_datetime'] = format_datetime

    # Load HTML template
    template = env.from_string(template_content)

    # Render the data into the template
    return template.render(data_yaml)

def make_pdf(template_content, data):
    rendered_content = render_template(template_content, data)

    # with open('debug.html', 'w') as f:
        # f.write(rendered_content)

    return HTML(string=rendered_content, base_url='./').write_pdf(pdf_forms=True, optimize_images=True)

if __name__ == "__main__":
    template_file = sys.argv[1]
    data_file = sys.argv[2]
    output_file = sys.argv[3]

    # Load data from YAML file
    with open(data_file, 'r') as f:
        data_yaml = yaml.safe_load(f)

    with open(template_file, 'r') as f:
        template_content = f.read()

    pdf = make_pdf(template_content, data_yaml)

    with open(output_file, 'wb') as f:
        f.write(pdf)
