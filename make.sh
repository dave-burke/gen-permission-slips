#!/bin/bash

set -e

make -e DATA="${1}/data.yaml"
mv -v output.pdf "${1}.pdf"
evince "${1}.pdf"
