from google_images_download import google_images_download

happy_man_queries = ["cheerful man", "happy man", "happy men face", "smiling man", "довольный мужчина", "радостный мужчина", "счастливый мужчина", "улыбающийся мужчина"]
sad_man_queries = ["sad man", "sad men face", "sad young man", "sad young man face", "грустный мужчина", "лицо грустного мужчины"]
happy_woman_queries = ["cheerful woman", "grinning woman", "happy woman", "happy woman face", "smiling woman", "довольная женщина", "счастливая женщина", "улыбающаяся женщина"]
sad_woman_queries = ["sad girl", "sad qirl face", "sad woman", "грустная девушка", "грустная женщина", "лицо грустной женщины"]

queries = happy_man_queries + sad_man_queries + happy_woman_queries + sad_woman_queries

for query in queries:
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":query,"limit":100,"print_urls":True}
    paths = response.download(arguments)
    print(paths)
