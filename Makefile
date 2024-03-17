main: input.html
	weasyprint --pdf-forms --optimize-images input.html output.pdf
input.html:
	python make-template.py template.html data.yaml input.html
