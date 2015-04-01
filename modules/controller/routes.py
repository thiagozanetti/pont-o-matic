#! /usr/bin/env python

from flask import Flask, render_template
import jinja2
from modules.utils import settings

app = Flask(__name__, static_folder=settings.assets_path, template_folder=settings.template_path)

#little hack to make custom template folder works
app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([settings.assets_path, settings.template_path]),])

@app.route("/")
def index():
#    return app.template_folder
    return render_template("index.tpl")
