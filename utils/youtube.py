import os
import html
from dotenv import load_dotenv
import googleapiclient.discovery

load_dotenv()


def search_youtube(user_input, number):
    """Search on Youtube.
    Args:
        user_input (str): search string
        number (int): number of search results
    Returns:
        list: list of results
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv('TOKEN')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY,
        cache_discovery=False)

    request = youtube.search().list(  # pylint: disable=no-member
        part="snippet",
        maxResults=number,
        q=user_input
    )
    response = request.execute()

    list = response["items"]

    out = []

    for l in list:
        title = html.unescape(l['snippet']['title'])
        try:
            if l['id']['kind'] == "youtube#channel":
                type = 'channel'
                id = l['id']['channelId']
            elif l['id']['kind'] == "youtube#playlist":
                type = 'playlist'
                id = l['id']['playlistId']
            elif l['id']['kind'] == "youtube#video":
                type = 'video'
                id = l['id']['videoId']
            else:
                type = 'unknown'
                id = "NoID"
        except KeyError:  # pragma: no cover
            type = 'unknown'
            id = "NoID"

        out.append({'title': title, 'type': type, 'id': id})

    return out
