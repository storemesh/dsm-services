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
    '2.1': 'Pumpkin Art Town มีกิจกรรม Workshop งานศิลปะ โดยมีทั้งการทำผ้ามัดย้อม กิจกรรมวาดรูประบายสี กิจกรรมทอผ้า',
    '2.2': 'Pumpkin Art Town 11 หมู่ 1 ซอยกระแชง 5 ตำบลกระแชง อำเภอสามโคก',
    '2.3': 'Pumpkin Art Town ยังไม่มีผลิตภัณฑ์ภายใต้ชื่อแบรนด์ แต่เน้นการนำของจากชุมชนมาจำหน่าย เช่น งานแฮนด์เมด กิ๊ฟต์ช็อป ผ้าไหมจากกลุ่มทอผ้าที่นครพนม เป็นต้น',
    '2.4': 'Pumpkin Art Town คัดเลือกของจากชุมชนชาวบ้าน แล้วนำมาจำหน่ายผ่านตลาดเล็ก ๆ ในร้าน รวมถึงรับพนักงานจากชุมชนโดยรอบเข้ามาทำงาน',
    '3.1': 'กลุ่มลูกค้าหลักของ Pumpkin Art Town คือกลุ่มครอบครัว และวัยรุ่นหรือผู้ใหญ่ที่มีความสนใจในด้านเวิร์กช็อปงานศิลปะ',
    '3.2': 'Pumpkin Art Town มีการจัดอีเวนต์ในทุก ๆ เทศกาลสำคัญ เช่น เทศกาลฮาโลวีน ทางร้านจะตกแต่งร้านเป็นธีมฮาโลวีน และประชาสัมพันธ์ให้ลูกค้าแต่งตัวมาตามธีม',
    '4.1': """Pumpkin Art Town มีโรงแรมมี 11 ห้อง แบ่งเป็นโซน โซนหนึ่งเป็นตึกที่มี 4 ห้อง (ห้องแยก) พักได้ 2 ท่าน ชื่อว่า Little Pumpkin
ถัดมา ใหญ่ขึ้นมานิดหนึ่งจะชื่อว่า Middle Pumpkin ก็จะมีอีก 4 ห้อง แยกเป็นบ้านหลัง ๆ พักได้ 2 ท่านเหมือนกัน แต่จะแยกความไพรเวตออกมา ซึ่งตกแต่งไม่เหมือนกัน ต่อไปจะเป็น Big Pumpkin มี 2 ห้อง พักได้ 4 ท่าน ก็จะเป็นเตียง 2 ชั้นกับเตียงคิงไซซ์ แล้วก็ห้องนั่งเล่น ไซซ์ใหญ่สุดจะเป็น Jumbo Pumpkin มีห้องเดียว จะเป็นบ้านหลังใหญ๋ มี 2 ห้องนอน 3 ห้องน้ำ""",
    '4.2': 'สามารถเดินทางที่ Pumpkin Art Town ได้โดยรถส่วนตัว',
    '5.1': 'Pumpkin Art Town ใช้แนวคิด “พื้นที่สีเขียว” ในการสร้างสรรค์ที่แห่งนี้ให้เป็นพื้นที่สำหรับพักผ่อน โดยยังคงคำนึงถึงวิถีชีวิตริมน้ำ วิถีชุมชน',
    '5.2': 'Pumpkin Art Town ใช้วัฒนธรรมท้องถิ่นในกิจกรรมทอผ้า และทำผ้ามัดย้อม รวมถึงยังคงวัฒนธรรมการต้อนรับแบบไทย คือ ไป ลา มา ไหว้',
    '6.1': 'Pumpkin Art Town พยายามปรับปรุงพื้นที่ในปทุมธานีให้เป็นแหล่งท่องเที่ยว เพราะปทุมธานีไม่ใช่พื้นที่สำหรับท่องเที่ยว พอคุณหยีมาทำตรงนี้จึงมองว่า ปทุมธานีมีแหล่งท่องเที่ยวเยอะ มีวัดเยอะ เป็นโซนที่ยังมีความเป็นชุมชน ค่อย ๆ วิวัฒ ไม่ใช่ชุมชนประดิษฐ์ อีกทั้งตรงนี้ก็ไม่ไกลเมืองมากเท่าไร เพราะคุณหยีมองกลุ่มลูกค้าเป็นเด็กและครอบครัว ซึ่งหลักสำคัญคือเป็นพื้นที่ให้ครอบครัวได้มาใช้เวลาร่วมกันในวันหยุดพักผ่อน',
})
context.display()
```

- convert QA to article
```python
article = analyzer.context2article(context=context)
article.display()
```

- upload context
```python
analyzer.upload_context(context=article, district_id="<DISTRIC_ID>")
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