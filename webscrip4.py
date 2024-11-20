import urllib.request

# URL of the web page to fetch
url = 'https://www.example.com' # exemple brk jib kach site w syi

try:
    # Open the URL and read its content
    response = urllib.request.urlopen(url)
    
    # Read the content of the response
    data = response.read()
    
    # Decode the data (if it's in bytes) to a string
    html_content = data.decode('utf-8')
    
    # Print the HTML content of the web page
    print(html_content)

except Exception as e:
    print("Error fetching URL:", e)

##We define the URL of the web page we want to fetch.
#We use urllib.request.urlopen() function to open the URL and obtain a response object.
#We read the content of the response object using the read() method.
#Since the content is returned as bytes, we decode it to a string using the decode() method with ‘utf-8’ encoding.
#Finally, we print the HTML content of the web page.
