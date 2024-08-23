#!/bin/bash

set -e

if [[ $# -eq 0 ]]; then
	echo "Usage: $(basename ${0})" [folder]
	exit 1
fi

python ./make_pdf.py template.html "${1}/data.yaml" "${1}.pdf"
evince "${1}.pdf"
