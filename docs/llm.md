# LLM
Large Language Model using Ollama
- generate_content
```python
import dsm_services

model = dsm_services.llm.dsmLLM(
    model_name='llama3.1', 
    api_key="o94fsLLw.********"
)
res = model.generate_content("Hello my name is Bob")
print(res.response)
```

- chat

```python
import dsm_services

model = dsm_services.llm.dsmLLM(
    model_name='llama3.1', 
    api_key="o94fsLLw.********"
)
res = model.chat(messages=[
    {'role': 'system', 'content': 'your assistance for me'},
    {'role': 'user', 'content': 'Hello my name is Bob'},
])
print(res.message)
```

## Langchain Integrations
```python
from dsm_services.llm.langchain import llmChatModel
llm = llmChatModel(model_name="llama3.1", api_key="o94fsLLw.********")

res = llm.invoke("Hello")
print(res)
```