import dpath.util

option = {
    "artist": [
        "name",
        "followers/total",
        "genres",
        "images/0/url"
    ],
    "track": [
        "album/name",
        "album/artists/0/name",
        "album/album_type",
        "album/images/0/url",
        "album/release_date"
    ],
    "album": [
        "name",
        "images",
        "release_date",
        "total_tracks"
    ],
    "playlist": [
        "name",
        "external_urls/spotify",
        "images/0/url",
        "owner/display_name",
        "tracks/total"
    ]
}


def get_key_data_from(json_data, look_for):
    data = json_data[f"{look_for}s"]["items"]
    for item in data:
        for section in option[look_for]:
            try:
                data_to_show = dpath.util.get(item, section, separator='/')
                print(f"{section}: {data_to_show}")
            except KeyError:
                print(f"{section}: Key not found")
