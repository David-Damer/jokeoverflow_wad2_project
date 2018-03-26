# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
from googleapiclient.discovery import build


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyAFFq5O7JLSDNpYL0KK6URb4v_XozqWoHA'  # Should be kept secret but not as grader needs access to test
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(q):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=q,
        part='id, snippet',
        maxResults=5,
        type='video',
        videoEmbeddable='true'
    ).execute()

    results = []

    try:
        for item in search_response['items']:
            videoId = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail = item['snippet']['thumbnails']['default']
            results.append({'id': videoId, 'title': title, 'description': description, 'thumbnail': thumbnail})

    except:
        print('error')
    return results


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--q', help='Search term', default='Google')
#     parser.add_argument('--max-results', help='Max results', default=25)
#     args = parser.parse_args()
#
#     try:
#         youtube_search(args)
#     except HttpError as e:
#         print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
