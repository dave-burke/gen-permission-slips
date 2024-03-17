main: tmp.html
	weasyprint --pdf-forms --optimize-images tmp.html output.pdf
	rm tmp.html
tmp.html:
	python make-template.py template.html data.yaml tmp.html
