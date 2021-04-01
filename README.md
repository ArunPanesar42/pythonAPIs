# Python APIs
## Using a library API to find out book publishers 

- I've done this by getting the ISBN

### Create the Api Method file
- here is the file we created
```python
import requests

class get_book():
    def __init__(self, book_isbn):
        # Set up details to get book publisher and see if website is up
        self.url = 'https://openlibrary.org/isbn/'
        self.publisher = self.get_publisher(book_isbn)
        url = "https://openlibrary.org/isbn/"
        url_arg = url + book_isbn
        response = requests.get(url_arg)
        if response.status_code == 200:
            print(f"This website is running and the code is: {response.status_code}")
        else:
            print("Website is unavailable")

    def get_publisher(self, book_isbn):
        url = "https://openlibrary.org/isbn/"
        url_arg = url + book_isbn
        response = requests.get(url_arg)
        response_dict = response.json()
        response_keys = response_dict['publishers']
        # for items in response_keys.keys():
        print(f"the publisher of your book is: {response_keys[0]}")

```
 ### Then get the file where we store the book information

- here is the book details file 
```python
from python_api_books import get_book

book_isbn = "9780140328721.json"
get_book(book_isbn)

```

- this is our result 

````
the publisher of your book is: Puffin

This website is running and the code is: 200
````
- this is a test 