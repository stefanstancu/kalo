import os
import requests

api_key = os.environ['USDA_KEY']

SEARCH_URL='https://api.nal.usda.gov/ndb/search'
REPORT_URL='https://api.nal.usda.gov/ndb/reports'

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
        try:
            ndbno.append(req['list']['item'][i]['ndbno'])
        except Exception as ke:
            break

    logger.info(ndbno)
    nutrition = get_nutrition(ndbno, logger)
    return nutrition

def get_nutrition(ndbno, logger=None):
    ''' Queries the item to return the desired nutriiton information
        Currently only collecting calories, carbohydrates, protein and fats
    '''

    results = []
    for dbno in ndbno:
        # , 'nutrients':[208, 205, 204, 203]
        payload={'format': 'json', 'api_key': api_key, 'ndbno': dbno}
        req = requests.get(REPORT_URL, params=payload).json()
        results.append(clean_data(req, logger))
    return results

def clean_data(nut_report, logger=None):
    ''' Cleans the data from the usda (only one ndbno) for return to the front-end
    @param nut_report: the data returned from the usda api
    '''
    logger.info("NUT REPORT \n ")
    logger.info(nut_report)
    entry = {'name':'', 'calories': 0, 'carbohydrates': 0, 'fat': 0, 'protein': 0}
    nut_report = nut_report['report']['food']
    entry['name'] = nut_report['name'].split('(Inc')[0]
    entry['calories'] = nut_report['nutrients'][1]['value']
    entry['carbohydrates'] = nut_report['nutrients'][5]['value']
    entry['fat'] = nut_report['nutrients'][3]['value']
    entry['protein'] = nut_report['nutrients'][2]['value']
    return entry

