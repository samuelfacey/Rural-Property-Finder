from flask import Flask, request, render_template
from search import search, detailed_search, storage

app = Flask(__name__)
@app.route('/')
@app.route('/results', methods =['GET', 'POST'])
async def home():
    if request.method == 'POST':
        # getting input with name = fname in HTML form
        s = request.form.get('search')
        search_input = s.replace(' ','')
        buy_or_rent = request.form.get('buy-or-rent')
        lot_or_not = request.form.get('type')
        price = request.form.get('price')
        beds = request.form.get('beds')
        baths = request.form.get('bath')
        sqft = request.form.get('sqft')
        lot = request.form.get('lot') # need cap of 1000 acres to avoid false results
        pend = request.form.get('hide-pend')

        search_parameters = {
            'search': search_input.replace(',','_'),
            'buy_or_rent': buy_or_rent,
            'lot_or_not': lot_or_not,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'lot': lot,
            'pend': pend
        }
        
        return render_template('results.html', results=await search(search_parameters))
        
    return render_template('index.html')



@app.route('/property/<string:site_url>', methods =['GET', 'POST'])
async def property(site_url):

    return render_template('property.html', details=await detailed_search(site_url.replace('%','/')))

if __name__ == '__main__':
    app.run(debug=True)