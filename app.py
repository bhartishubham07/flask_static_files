from flask import Flask,render_template

FAI = Flask(__name__)

@FAI.route('/static_files')
def static_files():
    return render_template('static_files.html')

@FAI.route('/navigation')
def navigation():
    return render_template('navigation.html')


if __name__ == '__main__':
    FAI.run(debug=True)