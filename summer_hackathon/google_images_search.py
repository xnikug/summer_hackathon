from googleapiclient.discovery import build

def google_search_images(search_term, api_key, cse_id, num_images=10):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(
        q=search_term,          # Query term
        cx=cse_id,              # Custom search engine ID
        searchType="image",     # Search for images
        num=num_images          # Number of images to retrieve
    ).execute()
    
    if 'items' in res:
        images = [item['link'] for item in res['items']]
        return images
    else:
        return "No images found"

# Replace 'your_api_key' and 'your_cse_id' with your API key and custom search engine ID
api_key = 'your_api_key'
cse_id = 'your_cse_id'
search_term = 'puppies'  # Change the search term as needed

images = google_search_images(search_term, api_key, cse_id)
for img in images:
    print(img)
