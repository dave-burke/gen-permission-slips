# Scout permission slip generator

Generate permission slip PDFs based on data in a yaml input file.

## Requirements

- Python 3.x (for rendering template)
- [weasyprint](https://weasyprint.org/) (for html to pdf conversion)

### Optional (but highly recommended)

- Bash (for running `make.sh`)
- GNU Make (for running the build)
- virtualenv (for keeping python dependencies contained)
- direnv (to automatically activate/deactivate virtualenv)
- Evince (for viewing PDFs)

## Setup

```bash
virtualenv venv
direnv allow
pip install -r requirements.txt
```

## Building PDFs

```bash
mkdir 20xx-mm-dd_name # e.g. 2024-05-01_some_camp
cp data.yaml 20xx-mm-dd_name/data.yaml
vim 20xx-mm-dd_name/data.yaml # Edit as-needed
./make.sh 20xx-mm-dd_name
```
