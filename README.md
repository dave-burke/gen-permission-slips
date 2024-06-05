# Scout permission slip generator

Generate permission slip PDFs based on data in a yaml input file.

## Requirements

- Python 3.x

### Optional (but highly recommended)

- Bash (for running `make.sh`)
- virtualenv (for keeping python dependencies contained)
- direnv (to automatically activate/deactivate virtualenv)
- Evince (for viewing PDFs)

## Setup

```bash
# Install OS dependencies (in Arch Linux -- will vary by OS)
pacman -S --needed bash base-devel python python-virtualenv direnv evince

# Create virtual environment
virtualenv venv

# ensure you have something like this in .bashrc: `if command -v direnv > /dev/null; eval "$(direnv hook bash)"`

direnv allow .

# you may need to reload your shell now and cd back into this directory
# you should see output from 'direnv' when you enter the directory
# Test with `which pip`. It should say '/path/to/this/repo/venv/bin/pip'

pip install -r requirements.txt
```

## Building PDFs

```bash
mkdir 20xx-mm-dd_name # e.g. 2024-05-01_some_camp
cp data.yaml 20xx-mm-dd_name/data.yaml
vim 20xx-mm-dd_name/data.yaml # Edit as-needed
./make.sh 20xx-mm-dd_name
```
