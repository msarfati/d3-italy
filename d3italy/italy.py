from flask import (
    Blueprint, render_template
)

bp = Blueprint('italy', __name__)

@bp.route('/')
def index():
    return render_template('italy/index.html')
