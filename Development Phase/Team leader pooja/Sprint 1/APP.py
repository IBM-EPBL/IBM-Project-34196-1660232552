from flask import Flask, render_template,request,redirect,url_for,session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=LAPTOP-OT7NNJQR.databases.appdomain.cloud;VERSION=[10.0.19043.2130];PORT=32536;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ot7nnjqr;PWD=eENReIXIS7xOOBBa",'','')

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    session['msg']=""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['newpassword']
        
        sql = "SELECT * FROM Members WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            session['DETAILS']= 'Account already exists'
            return redirect(url_for("login"))  
        else:
            insert_sql = "INSERT INTO Members VALUES (?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.execute(prep_stmt)
            session['msg']= 'Account created Successfully '
            return redirect(url_for("login"))
     
    
    return render_template('register.html') 


@app.route('/login',methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['newpassword']
        
        
        sql = "SELECT * FROM Members WHERE Email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_both(stmt)
        
        accounts=account
        
        
        if (account):
             (password == accounts['PASSWORD'] ):
             
                return render_template('LOGIN.html',msg='wrong Password')
        else :
            return render_template('LOGIN.html',msg='wrong credentials')

            
    else:
        return  render_template('LOGIN.html',msg=session['msg'])
)          

@app.route('/about')
def about():
    return render_template('ABOUT.html')    from flask import Flask, render_template,request,redirect,url_for,session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=LAPTOP-OT7NNJQR.databases.appdomain.cloud;VERSION=[10.0.19043.2130];PORT=32536;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ot7nnjqr;PWD=eENReIXIS7xOOBBa",'','')

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    session['msg']=""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['newpassword']
        
        sql = "SELECT * FROM Members WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            session['DETAILS']= 'Account already exists'
            return redirect(url_for("login"))  
        else:
            insert_sql = "INSERT INTO Members VALUES (?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.execute(prep_stmt)
            session['msg']= 'Account created Successfully '
            return redirect(url_for("login"))
     
    
    return render_template('register.html') 


@app.route('/login',methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['newpassword']
        
        
        sql = "SELECT * FROM Members WHERE Email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_both(stmt)
        
        accounts=account
        
        
        if (account):
             (password == accounts['PASSWORD'] ):
             
                return render_template('LOGIN.html',msg='wrong Password')
        else :
            return render_template('LOGIN.html',msg='wrong credentials')

            
    else:
        return  render_template('LOGIN.html',msg=session['msg'])
)          

@app.route('/about')
def about():
    return render_template('ABOUT.html')    