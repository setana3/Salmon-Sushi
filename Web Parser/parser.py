import requests
from bs4 import BeautifulSoup as bs
import json
import re

# define OK 200


def parser(contents):

    # data storage to contain list of dictionary of computer_info
    ds = list()

    for each in contents:

        href = each.find(
            "figure", class_="offer-thumb__image").find("a")['data-original']
        item_name = each.find('p')['title']

        price = each.find("span", class_="discount-price")
        if price != None:
            price = price.get_text()

        if price == None:
            try:
                price = each.find(
                    "span", class_="price-bn price-cp").get_text()
            except AttributeError:
                try:
                    price = each.find("span", class_="price-bn-old").get_text()
                except AttributeError:
                    price = "not retrived"
            except AttributeError:
                price = "Could not retrieve"

        computer_info = {"Title": item_name,
                         "Price": price,
                         "Picture href": href}

        ds.append(computer_info)

    return ds


html = ("https://www.osta.ee/en/category/computers/")


# Open a file to write to

with open('./output.json', 'a', newline='\n', encoding='utf8') as f_Write:

    if requests.get(html).status_code == 200:
        print("%s : is valid URL" % html)
        page = requests.get(html)
        contents = page.content
        data = bs(contents, 'html.parser')
        slides = data.find_all(class_="slide")
        parsed_content = parser(slides)
        print("%s : FINISHED" % (html))
        json.dump(parsed_content, f_Write, ensure_ascii=False)

    #From page-2 
    cnt = 2
    ERROR_CODE = 0

    while ERROR_CODE == 0:
        try:

            page = requests.get("%spage-%s" % (html, cnt))
            contents = page.content
            data = bs(contents, 'html.parser')
            items = data.find_all("figure", class_=re.compile(
                "^offer-thumb has-footer new-th"))
            parsed_content = parser(items)
            #This will stop parsing process if page exists, but nothign to parse
            if len(parsed_content) == 0:
                print("IT IS DONE!")
                exit()
            json.dump(parsed_content, f_Write, ensure_ascii=False)
            print("%spage-%s : FINISHED" % (html, cnt))

        except:
            print("%spage-%s : PROBLEM" % (html, cnt))
            print("You can try again from where it stopped")
            print("Copy and paste the URL")
            ERROR_CODE = 1  # exit while loop

        cnt += 1  # go to next page
