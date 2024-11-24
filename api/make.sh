#!/bin/bash

set -e

if [[ $# -eq 0 ]]; then
	echo "Usage: $(basename ${0})" [folder]
	exit 1
fi

template="template.html"
if [[ -r ${1}/template.html ]]; then
	template="${1}/template.html"
fi
python ./make_pdf.py ${template} "${1}/data.yaml" "${1}.pdf"
evince "${1}.pdf"
