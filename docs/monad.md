# Monnad
handle function all eg api call

- how to use as decorator
```py
from dsm_services.monad.resultify import resultify

@resultify
def function(input):
    ...
```

## example
- example 1
```py

from dsm_services.monad.resultify import resultify

@resultify
def fetch_user_details(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

fetch_user_details(user_id=0) # Error
fetch_user_details(user_id=1) # Sucess
```

- example 2

```py
import pandas as pd
from dsm_services.monad.resultify import resultify

@resultify
def fetch_user_details(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()
    
df2 = pd.DataFrame({'user_id': range(15)}).map(fetch_user_details)
print(df2)
```