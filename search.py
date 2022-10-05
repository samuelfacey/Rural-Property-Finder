from bs4 import BeautifulSoup
import requests


def search(search_parameters:dict):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    p = search_parameters
    
    if p['lot_or_not'] == None:
        p['lot_or_not'] = ''
    if p['pend'] == None:
        p['pend'] = ''

    property_info = []
    
    page_number = 1

    while True:

        custom_link = f"{p['buy_or_rent']}/{p['search']}/{p['beds']}/{p['baths']}/{p['lot_or_not']}/{p['price']}/{p['sqft']}/{p['lot']}/{p['pend']}/pg-{page_number}"
        search_link = f"https://www.realtor.com/{custom_link.replace('//','/')}"

        url = requests.get(url=search_link, headers=headers)

        soup = BeautifulSoup(url.text, 'html.parser')
        cards = soup.find_all(class_='jsx-1881802087 component_property-card')
        
        if cards:
            print(page_number)
            for item in cards:

                dict_ = {}

                try:
                    price = item.find(name='span', class_='Price__Component-rui__x3geed-0 gipzbd')
                    dict_['price'] = price.getText()
                except:
                    pass
                try:
                    address = item.find(name='div', class_='jsx-11645185 address ellipsis srp-page-address srp-address-redesign')
                    dict_['address'] = address.getText()
                except:
                    pass
                try:
                    details_list = []
                    details = item.find(class_='jsx-946479843 property-meta list-unstyled property-meta-srpPage')
                    for items in details:
                        for i in items:
                            details_list.append(i.getText())
                    dict_['details'] = details_list
                except:
                    pass
                try:
                    img = item.find(class_='fade top' ,name='img')
                    dict_['img'] = img['src']
                except:
                    pass
                try:
                    link = item.find('a')
                    dict_['link'] = f"https://www.realtor.com{link['href']}"
                except:
                    pass

                property_info.append(dict_)

        else:
            property_info.append({'count':len(property_info)})
            return property_info
        
        page_number += 1


