from flask import Flask, request, render_template
from search import search, detailed_search

app = Flask(__name__)
@app.route('/')
@app.route('/results', methods =['GET', 'POST'])
async def home():

    # getting input from form
    if request.method == 'POST':
        
        s = request.form.get('search')
        search_input = s.replace(' ','')
        lot_or_not = request.form.get('type')
        price = request.form.get('price')
        beds = request.form.get('beds')
        baths = request.form.get('bath')
        sqft = request.form.get('sqft')
        lot = request.form.get('lot')
        pend = request.form.get('hide-pend')

        # Creating dictionary from form data
        search_parameters = {
            'search': '/' + str(search_input.replace(',','_')),
            'lot_or_not': '/' + str(lot_or_not),
            'price': '/' + str(price),
            'beds': '/' + str(beds),
            'baths': '/' + str(baths),
            'sqft': '/' + str(sqft),
            'lot': '/' + str(lot),
            'pend': '/' + str(pend)
        }
        
        # Serves reults page and calls search function to get results
        return render_template('results.html', results=await search(search_parameters))
    
    # Serves index page
    return render_template('index.html')


@app.route('/')
@app.route('/property/<string:site_url>', methods =['GET', 'POST'])
async def property(site_url):

    # Serves property details page and calls detailed search function
    return render_template('property.html', details=await detailed_search(site_url.replace('%','/')))

if __name__ == '__main__':
    app.run(debug=True)