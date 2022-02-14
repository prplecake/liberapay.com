from liberapay.elsewhere._base import PlatformOAuth2

class Sourcehut(PlatformOAuth2):
    
    # Platform attributes
    name = 'sourcehut'
    display_name = 'Sourcehut'
    account_url = 'https://meta.sr.ht/{user_name}'
    repo_url = 'https://git.sr.ht/{slug}'

    # Auth attributes
    auth_url = 'https://meta.sr.ht/oauth2/authorize'
    oauth_default_scope = ['git.sr.ht/PROFILE:RO']
    access_token_url = 'https://meta.sr.ht/oauth2/access-token'

    # API attributes
    api_format = 'json'
    api_url = 'https://git.sr.ht/api'

