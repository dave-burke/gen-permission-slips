#!/bin/bash

set -e

npm run lint
npm run type-check
npx vite build --base="/camp-forms/"
rsync -rv --delete ./dist/ ${1}:/opt/http/static/camp-forms/
