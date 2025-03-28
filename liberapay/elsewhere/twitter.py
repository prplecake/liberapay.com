from liberapay.elsewhere._base import PlatformOAuth1
from liberapay.elsewhere._extractors import key, not_available
from liberapay.elsewhere._paginators import query_param_paginator


class Twitter(PlatformOAuth1):

    # Platform attributes
    name = 'twitter'
    display_name = 'Twitter'
    account_url = 'https://x.com/{user_name}'

    # Auth attributes
    auth_url = 'https://api.twitter.com'
    authorize_path = '/oauth/authenticate'

    # API attributes
    api_format = 'json'
    api_paginator = query_param_paginator('cursor',
                                          prev='previous_cursor',
                                          next='next_cursor')
    api_url = 'https://api.twitter.com/1.1'
    # api_user_info_path = '/users/show.json?user_id={user_id}&include_entities=false'
    # api_user_name_info_path = '/users/show.json?screen_name={user_name}&include_entities=false'
    api_user_self_info_path = '/account/verify_credentials.json?include_entities=false&skip_status=true'
    # api_follows_path = '/friends/list.json?user_id={user_id}&include_user_entities=false&skip_status=true'
    ratelimit_headers_prefix = 'x-rate-limit-'

    # User info extractors
    x_user_id = key('id_str')
    x_user_name = key('screen_name')
    x_display_name = key('name')
    x_email = not_available
    x_avatar_url = key('profile_image_url_https',
                       clean=lambda v: v.replace('_normal.', '.'))
    x_follows_count = key('friends_count')
    x_description = key('description')
