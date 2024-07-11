# Analyzer

- init analyzer instance
```python
import dsm_services

analyzer = Analyzer(service_uri="https://<SERVICES_URI>", api_key="<API_KEY>")
```

- list distric
```python
analyzer.list_district()
```

- get distric detail
```python
distric = analyzer.get_district(district_id='1-อำเภอเมืองปทุมธานี')
distric.display()
```

- prepair context
```python
context = analyzer.prep_context(data={
    '1.1': 'dfellow',
    '1.2': 'รับจ้างทำ software',
    '1.3': '29/1493 คลองสาม คลองหลวง ปทุมธานี',
    '2': 'ชอบเที่ยว',
    '3': 'เจ้าของอินดี้',
    '4': 'ลูกค้าเรื่องมาก',
    '5': 'ไม่รู้',
    '6': 'เที่ยวไปโค้ดไปกินเวลาวันหยุดไป',
    '7': 'กลุ่มที่มีเงิน',
    '8': 'ทุกคนอยากมีตัง',
    '9': 'ทำไปเรื่อยๆหาเงินเรื่อยๆ',
    '10': 'ปวดหลังมาก'
})
context.display()
```

- upload context
```python
analyzer.upload_context(context=context, district_id="<DISTRIC_ID>")
```

- get wizmap
```python
analyzer.get_wizmap(version=-1)
```

- RAG
```python
analyzer.rag("<PROMPT>").display()
# example : analyzer.rag("สถานที่ท่องเที่ยวของปทุมธานีคืออะไรบ้าง").display()
```

- list RAG history
```python
analyzer.list_rag()
```

- get rag history
```python
analyzer.get_rag(rag_id=<RAG_ID>).display()
```

- create mindmap
```python
analyzer.create_mindmap("<PROMPT>")

# example : analyzer.create_mindmap("please create mindmap about ปทุมธานี")
```