# LLM
Large Language Model using Ollama
```python
import dsm_services

model = dsm_services.llm.dsmLLM(
    model_name='llama3.1', 
    api_key="o94fsLLw.********"
)
res = model.generate_content("Hello my name is Bob")
print(res.response)
```