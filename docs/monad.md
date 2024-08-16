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