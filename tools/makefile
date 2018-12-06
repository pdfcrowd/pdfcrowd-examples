test:
	python convert_pages.py --user $(USER_NAME) --key $(API_KEY) --pages urls.txt --out out
	python convert_pages_to_single_pdf.py --user $(USER_NAME) --key $(API_KEY) --pages urls.txt --out out/test.pdf
	python create_brochure.py --user $(USER_NAME) --key $(API_KEY) --out out/brochure.pdf
