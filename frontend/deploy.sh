#!/bin/bash

set -e

npx vite build --base="/camp-forms/"
rsync -rv --delete ./dist/ ${1}:/opt/http/static/camp-forms/
