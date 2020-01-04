#!/usr/bin/env python

import base64
import random

from flask import Flask, render_template

from flags import flags
from draw_valknut import get_valknut_svg


app = Flask(__name__)


@app.template_filter("base64")
def encode_as_base64(xml_string):
    return base64.b64encode(xml_string.encode("ascii")).decode("ascii")


@app.route("/")
def index():
    selected_flags = random.sample(list(flags.values()), 3)

    svg_xml = get_valknut_svg(*selected_flags)

    return render_template("index.html", svg_xml=svg_xml)


if __name__ == "__main__":
    app.run(debug=True)