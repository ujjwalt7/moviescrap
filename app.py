import json
import os
from flask import Flask, render_template, jsonify, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route("/cat/<cat>/<page>")
def catpage(cat,page):
    spider_name = "mem"
    os.system("cd movies && scrapy crawl "+ spider_name+ ' -a cat="'+cat+'?page='+page+'" -O output.json')
    print(os.system('ls'))
    # os.system("cd movies && scrapy crawl "+ spider_name+ ' -a cat="'+cat+'" -O output.json')
    with open("./movies/output.json") as items_file:
        return json.load(items_file)
    

@app.route("/page/<type>/<link>")
def pageHome(type,link):
    spider_name = "moviepage"
    # print("cd firstproj && scrapy "+ "crawl "+ spider_name+ " -a page='"+type+"/"+link +"' -O output.json")
    os.system("cd movies && scrapy crawl "+ spider_name+ ' -a page="'+type+"/"+link +'" -O output.json')
    # os.system("cd movies && scrapy crawl "+ spider_name+ ' -a page="'+type+"/"+link +'" -O output.json')
    with open("./movies/output.json") as items_file:
        return json.load(items_file)
    # return {'hello':'yo'}


if __name__ == "__main__":
    app.run(debug=True)
