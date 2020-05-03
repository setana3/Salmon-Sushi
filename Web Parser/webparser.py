import requests
from bs4 import BeautifulSoup as bs
import json

#retriving page contents from this web URL 
page = requests.get("https://www.osta.ee/en/category/computers")

print(page.encoding)

#Contents is <'bytes'> object.
contents = page.content


#Objectifying content to BeautifulSoup4
soup = bs(contents, 'html.parser')
product_fig = soup.find_all("figure", class_="offer-thumb")



#data storage to contain list of dictionary of computer_info
ds = list()



#Parser
for class_fig in product_fig:

    href = class_fig.find("figure", class_="offer-thumb__image").find("a")['data-original']
    item_name = class_fig.find('p')['title']
    print(item_name)

    try: #Fix NoneType is properly rendered as '' Rather than AttributeError beings
        price = class_fig.find('p', class_="offer-thumb__price").find('span').text
    except AttributeError:
        price = class_fig.find('p', class_="offer-thumb__price")


    computer_info = {"Title": item_name,
                     "Price": price,
                     "Picture href": href}

    ds.append(computer_info) 

json_text = json.dumps(ds)




#Write to output.json data
with open('./output.json', 'w+') as f_Write:
    json.dump(ds, f_Write, ensure_ascii=False) #Ascii will not render euro char


### --- END ---- ###  
### Seho Tanaka 