from bs4 import BeautifulSoup
import requests
import time as t
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

async def search(search_parameters:dict):
    

    p = search_parameters

    # Creates list of properties
    property_info = []
    
    page_number = 1

    while True:

        # Beautiful Soup setup with form dictionary info
        custom_link = f"/realestateandhomes-search{p['search']}{p['beds']}{p['baths']}{p['lot_or_not']}{p['price']}{p['sqft']}{p['lot']}{p['pend']}/pg-{page_number}"
        search_link = f"https://www.realtor.com{custom_link.replace('/None','')}"
        print(search_link)
        url = requests.get(url=search_link, headers=headers)

        soup = BeautifulSoup(url.text, 'html.parser')
        cards = soup.find_all(class_='jsx-1881802087 component_property-card')
        
        # Scrapes data from website property card
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
                    a = dict_['link'].replace('https://www.realtor.com/','')
                    dict_['address_url'] = a.replace('/','%') 
                except:
                    pass

                property_info.append(dict_)

        else:
            
            # Adds number of results and returns list of properties
            property_info.append({'count':len(property_info)})
            return property_info
        
        page_number += 1

async def detailed_search(url:str):

    # Beautiful soup setup
    search_link = f'https://www.realtor.com/{url}'
    print(search_link)

    url = requests.get(url=search_link, headers=headers)
    soup = BeautifulSoup(url.text, 'html.parser')

    home_details = {}

    bed_bath_area = soup.find(class_="PropertyMetastyles__StyledPropertyMeta-rui__sc-1g5rdjn-0 dAKbvN")
    b = []

    for i in bed_bath_area:
        for a in i:
            b.append(a.getText())
    
    img_div = soup.find(name='div', class_="main-carousel")
    for i in img_div:
        img = i.find(name='img')
        home_details['img'] = img['src']


    home_details['price'] = soup.find(class_='Price__Component-rui__x3geed-0 gipzbd').getText()
    home_details['address'] = soup.find(class_='Text__StyledText-rui__sc-19ei9fn-0 dEYYQ TypeBody__StyledBody-rui__sc-163o7f1-0 gVxVge').getText()
    home_details['details'] = b
    try:
        home_details['desc'] = soup.find(class_='jsx-355086517 desc').getText()
    except:
        home_details['desc'] = 'This property has no description.'
    home_details['link'] = search_link
    
    address = home_details['address'].replace(' ','-')
    address = address.replace(',','-')
    home_details['risk_factor_link'] = f'https://riskfactor.com/'
    home_details['internet_link'] = 'https://broadband477map.fcc.gov/#/'
    return home_details
    
