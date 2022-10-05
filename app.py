from flask import Flask, request, render_template
from search import search

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def home():
    if request.method == 'POST':
        # getting input with name = fname in HTML form
        search_input = request.form.get('search')
        buy_or_rent = request.form.get('buy-or-rent')
        lot_or_not = request.form.get('type')
        price = request.form.get('price')
        beds = request.form.get('beds')
        baths = request.form.get('bath')
        sqft = request.form.get('sqft')
        lot = request.form.get('lot') # need cap of 1000 acres to avoid false results
        pend = request.form.get('hide-pend')

        search_parameters = {
            'search': search_input,
            'buy_or_rent': buy_or_rent,
            'lot_or_not': lot_or_not,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'lot': lot,
            'pend': pend
        }
        
        return render_template('results.html', results=search(search_parameters))
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)