from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/form')
def new(): 
    return render_template('facts/form.html')