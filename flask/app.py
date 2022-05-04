from distutils.command.config import config
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sympy import content 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}" - {self.name}

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        data=Student(name=name,address=address)
        db.session.add(data)
        db.session.commit()
    alldata=Student.query.all()
    return render_template('index.html',datas=alldata)

@app.route('/delete/<int:id>')
def delete(id):
    data=Student.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:id>',methods=['GET', 'POST'])
def update(id):
    if request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        data=Student.query.filter_by(id=id).first()
        data.name=name
        data.address=address

        db.session.add(data)
        db.session.commit()
        return redirect('/')

    data=Student.query.filter_by(id=id).first()
    return render_template('update.html',form=data)

    






if __name__=="__main__":
    app.run(debug=True)