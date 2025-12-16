from flask import Flask , render_template ,url_for,redirect,request

app = Flask(__name__)

users={'testuser':'password123','bilal':'bilal123'}

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form ['Username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for ('home'))
        else:
            error_message = "Invalid username or password"
            return render_template('login.html', error=error_message)
    return render_template('login.html')   

     
@app.route('/signup',methods=["GET","POST"])
def signup(): 
    if request.method == 'POST':
        username = request.form ['Username']
        email = request.form['Email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        print(f"New user signup details:\nUsername: {username}\nEmail: {email}\nPassword: {password}\nConfirm Password: {confirm_password}")

        if username in users:
            error_message = "Username already exists. Please choose a different one."
            return render_template('signup.html', error=error_message)

        if password != confirm_password:
            error_message = "Passwords do not match."
            return render_template('signup.html', error=error_message)
        users[username] = password
        print("Updated Users List:", users)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/contact')
def contact(): 
    return render_template('contact.html') 

@app.route('/textiles')
def textiles():
    return render_template('textiles.html')
    
@app.route('/sketches')
def sketches():
    return render_template('sketches.html')

@app.route('/calligraphy')
def calligraphy():
    return render_template('calligraphy.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/painting')
def painting():
    return render_template('painting.html')

@app.route('/product1')
def product1():
    return render_template('product1.html')

@app.route('/product2')
def product2():
    return render_template('product2.html')

@app.route('/product3')
def product3():
    return render_template('product3.html')

@app.route('/product4')
def product4():
    return render_template('product4.html')

@app.route('/product5')
def product5():
    return render_template('product5.html')

@app.route('/product6')
def product6():
    return render_template('product6.html')

@app.route('/product7')
def product7():
    return render_template('product7.html')

@app.route('/product8')
def product8():
    return render_template('product8.html')

@app.route('/product9')
def product9():
    return render_template('product9.html')

@app.route('/product10')
def product10():
    return render_template('product10.html')

@app.route('/product11')
def product11():
    return render_template('product11.html')

@app.route('/product12')
def product12():
    return render_template('product12.html')

@app.route('/product13')
def product13():
    return render_template('product13.html')

@app.route('/product14')
def product14():
    return render_template('product14.html')

@app.route('/product15')
def product15():
    return render_template('product15.html')

@app.route('/product16')
def product16():
    return render_template('product16.html')

@app.route('/product17')
def product17():
    return render_template('product17.html')

@app.route('/product18')
def product18():
    return render_template('product18.html')

@app.route('/product19')
def product19():
    return render_template('product19.html')

@app.route('/product20')
def product20():
    return render_template('product20.html')

@app.route('/product21')
def product21():
    return render_template('product21.html')

@app.route('/product22')
def product22():
    return render_template('product22.html')

@app.route('/product23')
def product23():
    return render_template('product23.html')

@app.route('/product24')
def product24():
    return render_template('product24.html')

@app.route('/product25')
def product25():
    return render_template('product25.html')

@app.route('/product26')
def product26():
    return render_template('product26.html')

@app.route('/product27')
def product27():
    return render_template('product27.html')

@app.route('/product28')
def product28():
    return render_template('product28.html')

@app.route('/product29')
def product29():
    return render_template('product29.html')

@app.route('/product30')
def product30():
    return render_template('product30.html')

@app.route('/product31')
def product31():
    return render_template('product31.html')

@app.route('/product32')
def product32():
    return render_template('product32.html')

@app.route('/product33')
def product33():
    return render_template('product33.html')

@app.route('/product34')
def product34():
    return render_template('product34.html')

@app.route('/product35')
def product35():
    return render_template('product35.html')

@app.route('/product36')
def product36():
    return render_template('product36.html')

@app.route('/product37')
def product37():
    return render_template('product37.html')

@app.route('/product38')
def product38():
    return render_template('product38.html')

@app.route('/product39')
def product39():
    return render_template('product39.html')

@app.route('/product40')
def product40():
    return render_template('product40.html')

@app.route('/product41')
def product41():
    return render_template('product41.html')

@app.route('/product42')
def product42():
    return render_template('product42.html')

@app.route('/product43')
def product43():
    return render_template('product43.html')

@app.route('/product44')
def product44():
    return render_template('product44.html')

@app.route('/product45')
def product45():
    return render_template('product45.html')

@app.route('/product46')
def product46():
    return render_template('product46.html')

@app.route('/product47')
def product47():
    return render_template('product47.html')

@app.route('/product48')
def product48():
    return render_template('product48.html')

@app.route('/product49')
def product49():
    return render_template('product49.html')

@app.route('/product50')
def product50():
    return render_template('product50.html')

@app.route('/product51')
def product51():
    return render_template('product51.html')

@app.route('/product52')
def product52():
    return render_template('product52.html')

@app.route('/product53')
def product53():
    return render_template('product53.html')

@app.route('/product54')
def product54():
    return render_template('product54.html')

@app.route('/product55')
def product55():
    return render_template('product55.html')

@app.route('/product56')
def product56():
    return render_template('product56.html')

@app.route('/product57')
def product57():
    return render_template('product57.html')

@app.route('/product58')
def product58():
    return render_template('product58.html')

@app.route('/product59')
def product59():
    return render_template('product59.html')

@app.route('/product60')
def product60():
    return render_template('product60.html')

@app.route('/product61')
def product61():
    return render_template('product61.html')

@app.route('/product62')
def product62():
    return render_template('product62.html')

@app.route('/product63')
def product63():
    return render_template('product63.html')

@app.route('/product64')
def product64():
    return render_template('product64.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)