import os
import requests

api_key = os.environ['USDA_KEY']

SEARCH_URL='https://api.nal.usda.gov/ndb/search'
NUTRIENT_URL='https://api.nal.usda.gov/ndb/nutrients'

def search_foods(query, tolerance=3, logger=None):
    ''' Searches for the foods by the string given, and returns the top n results
    @param query: the query
    @param tolerance: the number of entries to return
    '''

    payload={'format': 'json', 'api_key': api_key, 'q': query, 'ds':'Standard Reference' ,'max': tolerance}
    req = requests.get(SEARCH_URL, params=payload)
    req = req.json()
    ndbno = []
    for i in range(tolerance):
        ndbno.append(req['list']['item'][i]['ndbno'])

    logger.info(ndbno)
    nutrition = get_nutrition(ndbno)
    return nutrition

def get_nutrition(ndbno):
    ''' Queries the item to return the desired nutriiton information
        Currently only collecting calories, carbohydrates, protein and fats
    '''

    results = []
    for dbno in ndbno:
        payload={'format': 'json', 'api_key': api_key, 'ndbno': dbno, 'nutrients':[208, 205, 204, 203]}
        req = requests.get(NUTRIENT_URL, params=payload).json()
        results.append(clean_data(req))
    return results

def clean_data(nut_report):
    ''' Cleans the data from the usda (only one ndbno) for return to the front-end
    @param nut_report: the data returned from the usda api
    '''
    entry = {'name':'', 'calories': 0, 'carbohydrates': 0, 'fat': 0, 'protein': 0}
    nut_report = nut_report['report']['foods'][0]
    entry['name'] = nut_report['name']
    entry['calories'] = nut_report['nutrients'][0]['gm']
    entry['carbohydrates'] = nut_report['nutrients'][3]['gm']
    entry['fat'] = nut_report['nutrients'][2]['gm']
    entry['protein'] = nut_report['nutrients'][1]['gm']
    return entry

