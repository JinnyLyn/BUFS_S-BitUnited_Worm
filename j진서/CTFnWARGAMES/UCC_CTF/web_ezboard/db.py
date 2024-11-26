import os
import re
from ast import literal_eval
from datetime import datetime
PATH = os.path.dirname(os.path.abspath(__file__))


def read_data():

    metadata = []
    content = []
    for file in sorted(os.listdir(f"{PATH}/db/metadata")):
        with open(f"{PATH}/db/metadata/{file}", "r") as f: metadata.append(literal_eval(f.read().strip()))
    for file in sorted(os.listdir(f"{PATH}/db/content")):
        with open(f"{PATH}/db/content/{file}", "r") as f: content.append(literal_eval(f.read().strip()))
    
    posts = []
    for x, y in list(zip(metadata, content)):
        x.update(y)
        posts.append(x)

    return posts


def write_data(post):

    if os.path.exists(f"{PATH}/db/metadata/{post['date']}.txt"): return False

    metadata = {"author":post["author"], "secret":post["secret"], "date":str(datetime.fromtimestamp(post["date"]//1000))}
    with open(f"{PATH}/db/metadata/{post['date']}.txt", "w") as f:
        f.write(str(metadata))

    body_sub = re.sub("\[(\w+)\]\((https?:\/\/(([\w]+)[\/\.\?\&\#\=]?)+)\)", lambda x: f"<a href='{x.group(2)}'>{x.group(1)}</a>", post['body'])
    body_sub = re.sub("\[(\w+)\]\(([a-z0-9]+[\-\_]?[a-z0-9]+\@[a-z0-9]+[\-\_\.]?[a-z0-9]+)\)", lambda x: f"<a href='mailto:{x.group(2)}'>{x.group(1)}</a>", body_sub)
    content = {"subject":post["subject"], "body":body_sub}
    with open(f"{PATH}/db/content/{post['date']}.txt", "w") as f:
        f.write(str(content))

    return True
