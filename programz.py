import requests
import json

def get_boards_json():
    list_return = []
    x = json.loads(requests.get("http://api.4chan.org/boards.json").text)
    for board in x["boards"]:
        list_return.append([board["board"], board["title"]])
    return list_return


def get_threads_from_board(board):
    list_with_threads = []
    json_threads = json.loads(requests.get("http://api.4chan.org/" + board + "/catalog.json").text)
    position = 0
    for thread in json_threads:
        for x in thread["threads"]:
            if "sub" in x:
                leng = x["sub"]
            elif "com" in x:
                leng = x["com"][:50] if len(x["com"]) >= 50 else x["com"]
            else:
                leng = "NONE"

            list_with_threads.append([x["no"], leng, position])
            position += 1
    return list_with_threads

def get_files_from_thread(key, values):
    num_images = 0
    deliver_list = []
    add_between_threads = []
    add_between_threads.append(values[1])
    json_thread = json.loads(requests.get("http://a.4cdn.org/" + key +"/thread/" +str(values[0]) + ".json").text)
    imgs = []
    for post in json_thread["posts"]:
        if "filename" in post:
            #name of the file, link to imagem, extention of the image, extention for the folders
            imgs.append([post["filename"], "http://i.4cdn.org/" + key +"/" + str(post["tim"]) + post["ext"], post["ext"][1:]])
            num_images += 1
    add_between_threads.append(imgs)
    deliver_list += add_between_threads
    return [deliver_list, num_images]
