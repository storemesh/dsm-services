# NLP : Netural Language Processing

### Keyword Extraction
```python
import dsm_services

kw_extract = dsm_services.nlp.KeywordExtract(
    service_uri='<SERVICES_URI>', 
    api_key='<API_KEY>'
)
kw_extract.submit_job(texts=['Text1', 'Text2', ... 'TextN'])
results = kw_extract.get_result()
print(results)
```

### NER Named Entity Recognition
```python
import dsm_services

ner_extract = dsm_services.nlp.NERextract(
    service_uri='<SERVICES_URI>', 
    api_key='<API_KEY>'
)

ner_extract.submit_job(texts=['Text1', 'Text2', ... 'TextN'])
results = ner_extract.get_result()
print(results)
```

### POS Part Of Speech
```python
import dsm_services

pos_extract = dsm_services.nlp.POSextract(
    service_uri='<SERVICES_URI>', 
    api_key='<API_KEY>'
)

pos_extract.submit_job(texts=['Text1', 'Text2', ... 'TextN'])
results = pos_extract.get_result()
print(results)
```