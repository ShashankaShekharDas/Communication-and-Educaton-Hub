from google_images_download import google_images_download  
  
# creating object 
response = google_images_download.googleimagesdownload()  
  
search_queries =['apple','cat','appropriate','exorbitant'] 
  
  
def downloadimages(query): 
    arguments = {"keywords": query} 
    try: 
        response.download(arguments) 
        
    except FileNotFoundError:  
        arguments = {"keywords": query} 
                       
        try: 
            response.download(arguments)  
        except: 
            pass
  
for query in search_queries: 
    downloadimages(query)  
    print()
