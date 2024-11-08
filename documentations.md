---

**Using the GoogleDork Module**  
=============================

**Install the Module**  
---------------  
Install the `google-dork` library on your PC or Virtual Environment:

```bash
pip install google-dork
```

**Import the Module**  
---------------  

To use the GoogleDork module, you need to import it first:
```python
from google_dork import GoogleDork
```

**Creating an Instance of GoogleDork**  
-----------------------------  

To use the GoogleDork module, you need to create an instance of the `GoogleDork` class. You can create an instance with several optional parameters:

* `domain`: The domain you want to search (optional)
* `filetype`: The type of file you want to search for (optional)
* `intext`: Text you want to search within the page content (optional)
* `intitle`: Text you want to search within the page title (optional)
* `inurl`: Text you want to search within the page URL (optional)

Example:
```python
dork = GoogleDork(
    domain="example.com",
    filetype="pdf",
    intext="content to search",
    intitle="title to search",
    inurl="url to search"
)
```

**Search Method**  
-----------------  

The `search()` method performs a search using the specified dork and returns the search results in a list format.

Example:
```python
results = dork.search()
```

**Display Results Method**  
-------------------------  

The `display_results()` method displays the search results in a more readable format.

Example:
```python
dork.display_results(results)
```

**Usage Example**  
----------------------  

Below is an example of how to use the GoogleDork module:
```python
from google_dork import GoogleDork

dork = GoogleDork(
    domain="example.com",
    filetype="pdf",
    intext="content to search",
    intitle="title to search",
    inurl="url to search"
)

results = dork.search()
dork.display_results(results)
```
