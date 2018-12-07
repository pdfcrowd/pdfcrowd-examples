test:
	python convert_pages.py --user $(USER_NAME) --key $(API_KEY) --pages sample_urls.txt --out out/txt
	python convert_pages.py --user $(USER_NAME) --key $(API_KEY) --pages sample_sitemap.xml --out out/xml

	python convert_pages_to_single_pdf.py --user $(USER_NAME) --key $(API_KEY) --pages sample_urls.txt --out out/test.pdf
	python convert_pages_to_single_pdf.py --user $(USER_NAME) --key $(API_KEY) --pages sample_sitemap.xml --out out/test_sitemap.pdf

	python create_brochure.py --user $(USER_NAME) --key $(API_KEY) --out out/brochure.pdf
