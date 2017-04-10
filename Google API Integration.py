from oauth2client import client

flow = client.flow_from_clientsecrets(
    'client_secrets.json',
    scope='https://www.googleapis.com/auth/drive.metadata.readonly',
    redirect_uri='http://www.example.com/oauth2callback')
flow.params['access_type'] = 'offline'         # offline access
flow.params['include_granted_scopes'] = True   # incremental auth

auth_uri = flow.step1_get_authorize_url()

print(auth_uri)

from oauth2client.client import flow_from_clientsecrets

flow = flow_from_clientsecrets('path_to_directory/client_secrets.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')
from oauth2client.client import OAuth2WebServerFlow

flow = OAuth2WebServerFlow(client_id='your_client_id',
                           client_secret='your_client_secret',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://example.com/auth_return')