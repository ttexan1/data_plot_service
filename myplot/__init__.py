from flask import Flask
app = Flask(__name__)

import myplot.views
import myplot.sample
import myplot.form
import myplot.plot_template
