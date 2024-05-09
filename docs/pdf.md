# PDF2Text : Convert PDF file to Text

```python
import dsm_services

pdf_extract = dsm_services.pdf.PDF2Text(
    service_uri='<SERVICES_URI>', 
    api_key='<API_KEY>',
    extract_type='<Normal/Advance-OCR>'
)
pdf_extract.upload_file(file=<Byte Object or str file_path>)
```

- fetch result
```python
pdf_extract.fetch_result()
```