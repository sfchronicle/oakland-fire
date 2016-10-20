from flask import render_template, redirect, url_for, request

from app import app, freezer

@app.route('/')
def index():
    return render_template('index.html',
    	slug='',
    	title="",
    	description="",
    	twitter_text="")