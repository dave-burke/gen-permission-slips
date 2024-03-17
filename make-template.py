import sys
import yaml
from jinja2 import Environment, FileSystemLoader

def render_template(template_file, data_file, output_file):
    # Load data from YAML file
    with open(data_file, 'r') as f:
        data = yaml.safe_load(f)

    # Create Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))

    # Load HTML template
    template = env.get_template(template_file)

    # Render template with data and write to output file
    rendered_content = template.render(data)
    with open(output_file, 'w') as f:
        f.write(rendered_content)

if __name__ == "__main__":
    # Paths to template, data, and output files
    template_file = sys.argv[1]
    data_file = sys.argv[2]
    output_file = sys.argv[3]

    # Render template
    render_template(template_file, data_file, output_file)

