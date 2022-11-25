def get_channel_stats (youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_ids #grabs the channel that we want
    )
    response = request.execute() #exports the dictionary for that YouTube channel

    for item in response['items']: #for every channel in the response array pull the following data into a new array 
        data = {
            'channelName':item['snippet']['title'],
            'subscribers': item['statistics']['subscriberCount'],
            'views':item['statistics']['viewCount'],
            'totalVideos': item['statistics']['videoCount'],
            'playlistId':item['contentDetails']['relatedPlaylists']['uploads']
        }
        all_data.append(data)
    return (pd.DataFrame(all_data)) #grabbing tons of wanted stats and putting it into a dataframe. Utilizes the all_data array and puts it into a pandas DataFrame

def get_video_ids(youtube,playlist_id): #Grabs the video ids for every video in the channel
    
    video_ids = []

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults = 50 #The max for requests is 50
    )
    response = request.execute()
    
    for item in response['items']:  #Pulls the contentDetails for each video and puts it into the video_ids array
        video_ids.append(item['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken') #This continues requesting information while the next page is not empty
    while next_page_token is not None:
        request = youtube.playlistItems().list(
         part = 'contentDetails',
         playlistId = playlist_id,
            maxResults = 50,
            pageToken = next_page_token
        )
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        next_page_token = response.get('nextPageToken')
        
    return video_ids

def get_video_details(youtube, video_ids): #Gets the individual information from each video

    all_video_info = []
    
    for i in range (0, len(video_ids), 50):
        request = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=','.join(video_ids[i: i +50])
            )
        response = request.execute()

        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics':['viewCount', 'likeCount', 'favouriteCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)
    return pd.DataFrame(all_video_info)