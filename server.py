from flask import Flask, render_template, request
import mymodule

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    name="Aleksander"
    return render_template('index.html',name=name)

#retunrs all data
@app.route("/data/")
def alldata():
    return mymodule.process()


#an example of 1 paramter pass
@app.route("/data/date=<date>")
def data(date=0):
    return str(date)
    #return mymodule.process()
      
#an example of x paramter pass
@app.route("/datapost", methods=['GET','POST'])
def datapost():
    arguemtns = request.get_json()
    return "DATA:"
        
if __name__ == "__main__":
    app.run()
    
    