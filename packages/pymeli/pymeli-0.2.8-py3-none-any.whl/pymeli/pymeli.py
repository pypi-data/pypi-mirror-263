import json
import requests

class Meli():
 def __init__(self, **kwargs):
  """Constructor for Meli class. The arguments can be passed as keywords
  Keyword arguments:
  - client_id: The Client ID of your MELI application
  - client_secret: The secret of your MELI application
  - access_token: Access token for user you are working with (optional)
  - refresh_token: Refresh token for user you are working with (optional)
  """
  if 'client_id' in kwargs:
   self.__client_id = kwargs['client_id']
  else:
   raise ValueError('client_id is required')
  if 'client_secret' in kwargs:
   self.__client_secret = kwargs['client_secret']
  else:
   raise ValueError('client_secret is required')
  self.__access_token = None
  self.__refresh_token = None
  if 'access_token' in kwargs and 'refresh_token' in kwargs:
   self.__access_token = kwargs['access_token']
   self.__refresh_token = kwargs['refresh_token']
  elif 'access_token' in kwargs or 'refresh_token' in kwargs:
   raise ValueError('Both access_token and refresh_token are required')
  
 def exchange_code_for_token(self, code, redirect_uri):
  """Exchange the code for a token
  Parameters:
  - code: The code obtained from the user grant
  - redirect_uri: The redirect_uri used in the user grant
  Return:
  - token: A dictionary containing the access_token and refresh_token
  """
  url = 'https://api.mercadolibre.com/oauth/token'
  data = {
   'grant_type':'authorization_code',
   'client_id':self.__client_id,
   'client_secret':self.__client_secret,
   'code':code,
   'redirect_uri':redirect_uri
  }
  response = requests.post(
   url=url,
   data=data
  )
  if response.status_code != 200:
   raise requests.exceptions.HTTPError(response.text)
  return json.loads(response.text)

 def refresh_token(self):
  """Refresh the current token. It saves it in memory for future use and also
  returns an object containing the new token for persistent storage
  Return:
  - token: A dictionary containing the access_token and refresh_token
  """
  url = 'https://api.mercadolibre.com/oauth/token'
  data = {
   'grant_type':'refresh_token',
   'client_id':self.__client_id,
   'client_secret':self.__client_secret,
   'refresh_token':self.__refresh_token
  }
  response = requests.post(
   url=url,
   data=data
  )
  response.raise_for_status()
  credentials = json.loads(response.text)
  self.__access_token = credentials['access_token']
  self.__refresh_token = credentials['refresh_token']
  return credentials
 
 def me(self):
  return self._get(resource='/users/me')

 def list_sites(self):
  return self._get(resource='/sites')

 def list_listing_types(self, **kwargs):
  return self._get(
   resource='/sites/{site_id}/listing_types'.format(**kwargs)
  )

 def get_listing_type(self, **kwargs):
  return self._get(
   resource='/sites/{site_id}/listing_types/{listing_type}'.format(**kwargs)
  )

 def get_listing_prices(self, **kwargs):
  parameters = {}
  if 'price' in kwargs:
   parameters['price'] = kwargs['price']
  if 'category_id' in kwargs:
   parameters['category_id'] = kwargs['category_id']
  return self._get(
   resource='/sites/{site_id}/listing_prices'.format(**kwargs),
   parameters=parameters
  )

 def list_categories(self, **kwargs):
  return self._get(
   resource='/sites/{site_id}/categories'.format(**kwargs)
  )

 def get_category(self, **kwargs):
  return self._get(
   resource='/categories/{category_id}'.format(**kwargs)
  )

 def search_category(self, **kwargs):
  #Check if searching for a query
  parameters = {'category':kwargs['category_id']}
  if 'query' in kwargs:
   parameters['q'] = kwargs['query']
  #Paginate
  response = self._get(
   resource='/sites/{site_id}/search'.format(**kwargs),
   parameters=parameters
  )
  results = response['results']
  total = response['paging']['total']
  for offset in range(50,total,50):
   results += self._get(
    resource='/sites/{site_id}/search'.format(**kwargs),
    parameters={
     **parameters,
     'limit':'50',
     'offset':offset
    }
   )['results']
  return results

 def get_item(self, **kwargs):
  return self._get(
   resource='/items/{item_id}'.format(**kwargs)
  )

 def get_item_description(self, **kwargs):
  return self._get(
   resource='/items/{item_id}/description'.format(**kwargs)
  )

 def list_user_items(self, **kwargs):
  #If no user, then get the ID for me
  if 'user_id' not in kwargs:
   user_id = self.me()['id']
  else:
   user_id = kwargs['user_id']

  response = self._get(
   resource='/users/{user_id}/items/search'.format(user_id=user_id),
   parameters={'limit':'100','offset':'0','search_type':'scan'}
  )
  total = response['paging']['total']
  scroll_id = response['scroll_id']
  results = response['results']
  
  for _ in range(100,total,100):
   results += self._get(
    resource='/users/{user_id}/items/search'.format(user_id=user_id),
    parameters={
     'limit':'100',
     'scroll_id':scroll_id,
     'search_type':'scan'
    }
   )['results']

  return results

 def publish_item(self, **kwargs):
  response = self._post(
    headers = {'Content-Type':'application/json'},
    resource = '/items',
    data = kwargs['item']
   )
  return response

 def update_item(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = kwargs['updates']
   )
  return response

 def upload_item_description(self, **kwargs):
  response = self._post(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}/description'.format(**kwargs),
    data = {'plain_text':kwargs['description']}
   )
  return response

 def update_item_description(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}/description'.format(**kwargs),
    data = {'plain_text':kwargs['description']}
   )
  return response

 def upload_image(self, **kwargs):
  response = self._post(
    headers = {'multipart':'form-data'},
    resource = '/pictures/items/upload',
    image = kwargs['image']
   )
  return response

 def update_available_quantity(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = {'available_quantity':kwargs['available_quantity']}
   )
  return response

 def pause_item(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = {'status':'paused'}
   )
  return response

 def activate_item(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = {'status':'active'}
   )
  return response

 def close_item(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = {'status':'closed'}
  )
  return response

 def delete_item(self, **kwargs):
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = {'deleted':'true'}
  )
  return response

 def set_free_shipping(self, **kwargs):
  payload = {
   "shipping": {
         "mode": "me2",
         "free_methods":
         [
             {
                 "id": 501245,
                 "rule":
                 {
                     "default": True,
                     "free_mode": "country",
                     "free_shipping_flag": True,
                     "value": None
                 }
             }
         ],
         "local_pick_up": False,
         "free_shipping": True,
         "logistic_type": "drop_off"
     }
  }
  response = self._put(
    headers = {'Content-Type':'application/json'},
    resource='/items/{item_id}'.format(**kwargs),
    data = payload
   )
  return response
 ##############################################################################
 ########### INTERNAL FUNCTIONS NOT TO BE IMPLEMENTED PUBLICALLY###############
 ##############################################################################
 def _get_authorization_header(self):
  #Get token
  return {"Authorization": "Bearer {}".format(
   self.__access_token)}

 def _get(self, **kwargs):
  headers = self._get_authorization_header()
  url = 'https://api.mercadolibre.com' + kwargs['resource']
  if 'parameters' not in kwargs:
   parameters = {}
  else:
   parameters = kwargs['parameters']
  #Issue request
  response = requests.get(url=url, headers=headers, params=parameters)
  if response.status_code != 200:
   raise requests.exceptions.HTTPError(response.text)
  return json.loads(response.text)

 def _post(self, **kwargs):
  #Most basic request
  request = {
   'url': 'https://api.mercadolibre.com' + kwargs['resource'],
   'headers': self._get_authorization_header()
  }
  #Enhance if additional headers
  if 'headers' in kwargs:
   request['headers'] = {**request['headers'], **kwargs['headers']}
  #Enhance if data
  if 'data' in kwargs:
   request['data'] = json.dumps(kwargs['data'])
  #Enhance if image
  elif 'image' in kwargs:
   from requests_toolbelt import MultipartEncoder
   request['data'] = MultipartEncoder(
    fields={'file': ('i.jpeg',kwargs['image'],'image/jpeg')})
   request['headers'] = {
    **request['headers'], 'Content-type': request['data'].content_type}
  #Issue request
  response = requests.post(**request)
  if response.status_code not in [200,201]:
   raise requests.exceptions.HTTPError(response.text)
  return json.loads(response.text)

 def _put(self, **kwargs):
  #Most basic request
  request = {
   'url': 'https://api.mercadolibre.com' + kwargs['resource'],
   'headers': self._get_authorization_header()
  }
  #Enhance if additional headers
  if 'headers' in kwargs:
   request['headers'] = {**request['headers'], **kwargs['headers']}
  #Enhance if data
  if 'data' in kwargs:
   request['data'] = json.dumps(kwargs['data'])
  #Issue request
  response = requests.put(**request)
  if response.status_code != 200:
   raise requests.exceptions.HTTPError(response.text)
  return json.loads(response.text)


