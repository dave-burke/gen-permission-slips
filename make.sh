#!/bin/bash

set -e

if [[ $# -eq 0 ]]; then
	echo "Usage: $(basename ${0})" [folder]
	exit 1
fi

make -e DATA="${1}/data.yaml"
mv -v output.pdf "${1}.pdf"
evince "${1}.pdf"
