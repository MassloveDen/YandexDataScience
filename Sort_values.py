import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user

search_id = user_genres(genre_grouping)
music_user = df[ (df['user_id'] == search_id) & df['total_play_seconds'] != 0]
music_user.sort_values(by = 'genre_name')

#sum_music_user = music_user['total_play_seconds'].sum()
#sum_music_user = music_user.sort_values(by = 'genre_name').sum(music_user['total_play_seconds'])
sum_music_user = music_user.groupby("genre_name")['total_play_seconds'].sum()
#print(sum_music_user)

count_music_user =  music_user.groupby('genre_name')['genre_name'].count()
#print(count_music_user)

final_sum = sum_music_user.sort_values(ascending = False)
#print(final_sum)

final_count = count_music_user.sort_values(ascending = True)
print(final_count)
