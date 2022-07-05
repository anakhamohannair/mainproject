from flask import*
from DBConnection import  *
from newcnn import predictcnn
import uuid
app= Flask(__name__)
app.secret_key="qwerty"
@app.route('/')
def login():
    return render_template("LOG IN 1.html")

@app.route('/adminhome')
def adminhome():
    return render_template("admin home.html")


@app.route('/admin_resultview')
def admin_resultview():
    qry="SELECT * FROM `result` INNER JOIN `registration` ON`registration`.`LoginID`=`result`.`user_id`"
    res=select(qry)
    return render_template("admin_resultview.html",val=res)



@app.route('/addfeedback')
def addfeedback():
    return render_template("add feedback.html")
@app.route('/viewfeedback')
def viewfeedback():
    query="SELECT `feedback`.*,`registration`.`Fname`,`registration`.`Lname` FROM `feedback` JOIN `registration` ON `feedback`.`Userid`=`registration`.`regid`"
    res=select(query)
    return render_template("Feedback-4.html",value=res)
@app.route('/registration')
def registration():
    return render_template("registration.html")
@app.route('/managetips')
def managetips():
    query="select * from tip"
    res=select(query)
    return render_template("TIP.html",value=res)
@app.route('/addtip',methods=['post'])
def addtip():
    return render_template("TIPSS.html")
@app.route('/viewtip')
def viewtip():
    qry = "select * from tip"
    res = select(qry)
    return render_template("view tips.html",val=res)

@app.route('/viewuser')
def viewuser():
    qry="select * from registration"
    res=select(qry)
    return render_template("VIEWUSER.html",val=res)

@app.route('/logincode',methods=['post'])
def logincode():
    username=request.form['textfield']
    print(username)
    password=request.form['textfield2']
    print(password)
    query="select * from login where username=%s and password=%s"
    value=(username,password)
    res=selectone(query,value)
    print(res)
    if res is None:
        return '''<script> alert('Invalid username');window.location='/'</script>'''
    elif res[3]=='Admin':
        return '''<script> alert('Login Successful');window.location='adminhome'</script>'''
    elif res[3]=='user':
        session['lid']=res[0]
        return '''<script> alert('Login Successful');window.location='user'</script>'''

    else:
        return '''<script> alert('Invalid username');window.location='/'</script>'''


@app.route('/addfbk',methods=['post'])
def addfbk():
    fbk=request.form['textfield']
    qry="insert into feedback values(null,%s,%s,curdate())"
    val=(session['lid'],fbk)
    iud(qry,val)
    return '''<script> alert('Feedback added');window.location='user'</script>'''


@app.route('/user')
def user():
    return render_template("user index.html")



@app.route('/addtips',methods= ['post'])
def addtips():
    tips=request.form['textfield']
    query="insert into tip values(null,%s)"
    iud(query,tips)
    return '''<script> alert('Tip added');window.location='managetips'</script>'''





@app.route('/deletetip')
def deletetip():
    id=request.args.get('id')
    qry="delete from tip where Tipid=%s"
    iud(qry,id)
    return redirect("managetips")


@app.route('/register1',methods=['post'])
def register1():
    try:

        fname=request.form['textfield']
        lname=request.form['textfield2']
        place=request.form['textfield3']
        post=request.form['textfield4']
        pin=request.form['textfield5']
        phone=request.form['textfield6']
        email=request.form['textfield7']
        username=request.form['textfield8']
        password=request.form['textfield9']
        qry="insert into login values(NULL,%s,%s,'user')"
        val=(username,password)
        id=iud(qry,val)
        qry="insert into registration values(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(str(id),fname,lname,place,post,pin,phone,email)
        iud(qry,val)
        return '''<script> alert('Registration Successful');window.location='/'</script>'''
    except Exception as e:
        return '''<script> alert('Username already exists');window.location='/'</script>'''


@app.route('/docinfo',methods=['post'])
def docinfo():
    return render_template('docinfo.html')




@app.route('/vdocinfo')
def vdocinfo():
    qry="select * from doctor_info"
    res=select(qry)


    return render_template('viewdocinfo.html',val=res)




@app.route('/vdocinfo1')
def vdocinfo1():
    qry="select * from doctor"
    res=select(qry)


    return render_template('view doc.html',val=res)

@app.route('/browse')
def browse():
    if "upload" in request.form:
        i=request.files['i']
        # user_id=request.args['user_id']
        path="static/assets/img"+str(uuid.uuid4())+i.filename
        i.save(path)
        qry="insert into result values(null,%s,%s',curdate(),'0')"
        val=(session['lid'],path)
        iud(qry,val)
        return '''<script> alert('upload successfully');window.location='browse'</script>'''
    return render_template('browse.html')


@app.route('/deletedoc')
def deletedoc():
    id=request.args.get('id')
    qry="delete from doctor_info where id=%s"
    iud(qry,id)

    return redirect('vdocinfo')




@app.route('/predictfn',methods=['post'])
def predictfn():
    fn=request.files['fileField']
    # fn.save("sample.jpg")
    path="static/uploads/"+str(uuid.uuid4())+fn.filename
    fn.save(path)

    res=predictcnn(path)

    print(res,"++++++++++++++++++++++++++++++++++++++++++++++++")


    result="Normal"
    status=0
    # if status==0:
    #     qry="insert into result values(null,%s)"
    #     iud(qry,'normal')

    if str(res)=="1":
        result="The result is positive. Cell is Malignant"
        
        

        # qry="insert into result values(null,%s)"
        # iud(qry,'cell is Malignant')

    elif str(res)=="2":
        result = "Invalid Image"
        
    qry="insert into result values(null,%s,%s,%s)"
    val=(session['lid'],path,result)
    iud(qry,val)


    # qry = "select * from doctor_info"
    # res = select(qry)

    return render_template("bc.html",val=result,s=status)








@app.route('/adddocinfo',methods=['post'])
def adddocinfo():
    name=request.form['textfield']
    qual=request.form['textfield2']
    hospital = request.form['textfield3']
    Contact = request.form['textfield4']
    Email = request.form['textfield6']
    qry="insert into doctor_info values(null,%s,%s,%s,%s,%s)"
    val=(name,qual,hospital,Contact,Email)
    iud(qry,val)
    return '''<script> alert('Doctor Added');window.location='adminhome'</script>'''









@app.route('/adminmanagedoctors',methods=['get','post'])
def adminmanagedoctors():
    data={}
    if "add" in request.form:
        f=request.form['n']
        p=request.form['p']
        ph=request.form['ph']
        h=request.form['h']
        em=request.form['e']
            
        qry="insert into doctor values(null,%s,%s,%s,%s,%s)"
        val=(f,p,h,ph,em)
        iud(qry,val)
        return '''<script> alert('Doctor Added');window.location='adminmanagedoctors'</script>'''
    if "action" in request.args:
        action=request.args['action']
        id=request.args.get('id')
    else:
        action=None    
    
    if action=="delete":
        qry="delete from doctor  where doctor_id=%s"
        iud(qry,id)
        return '''<script> alert('delete successfully');window.location='adminmanagedoctors'</script>'''

      

    qry="SELECT * FROM doctor "
    res=select(qry)
    return render_template('adminmanagedoctors.html',val=res,data=data)


@app.route('/adminmanagedisease',methods=['get','post'])
def adminmanagedisease():
    data={}
    id=request.args.get('id')
    if "add" in request.form:
        title=request.form['title']
        qry="insert into disease values(null,%s)"
        val=(title)
        iud(qry,val)
        return '''<script> alert('added successfully');window.location='adminmanagedisease'</script>'''
    if "action" in request.args:
        action=request.args['action']
        id=request.args.get('id')
    else:
        action=None    
    if action=="delete":
        qry="delete from disease  where disease_id=%s"
        iud(qry,id)
        return '''<script> alert('delete successfully');window.location='adminmanagedisease'</script>'''

    qry="SELECT * FROM `disease` "
    res=select(qry)
    return render_template("adminmanagedisease.html",data=data,val=res)

@app.route('/adminmanagesymptoms',methods=['get','post'])
def adminmanagesymptoms():
    data={}
    id=request.args.get('id')
    if "add" in request.form:
        title=request.form['title']
        qry="insert into symptoms values(null,%s,%s)"
        val=(id,title)
        iud(qry,val)
        return '''<script> alert('added successfully');window.location='adminmanagesymptoms'</script>'''
    if "action" in request.args:
        action=request.args['action']
        ids=request.args.get('ids')
    else:
        action=None    
    if action=="delete":
        qry="delete from symptoms  where symptoms_id=%s"
        iud(qry,ids)
        return '''<script> alert('delete successfully');window.location='adminmanagesymptoms'</script>'''

    qry="SELECT * FROM `symptoms` "
    res=select(qry)
    return render_template("adminmanagesymptoms.html",data=data,val=res)

@app.route('/usersendcomplaint',methods=['get','post'])
def usersendcomplaint():
    data={}
    login_id=session['lid']

    qry="select * from complaint where LoginID='%s'"%(login_id)
    res=select(qry)
    if "send" in request.form:
        complaint=request.form['com']
        login_id=session['lid']
        qry="insert into complaint values(null,%s,%s,'reply-pending',curdate())"
        val=(login_id,complaint)
        iud(qry,val)
        return '''<script> alert('send successfully');window.location='usersendcomplaint'</script>'''
        return redirect(url_for('app.usersendcomplaint'))
    return render_template('usersendcomplaint.html',data=data,val=res)




@app.route('/userviewdisease')
def userviewdisease():
    qry="select * from disease"
    res=select(qry)


    return render_template('userviewdisease.html',val=res)


@app.route('/userviewsymptoms')
def userviewsymptoms():
    id=request.args.get('id')
    qry="select * from symptoms where disease_id=%s"  
    res=selectall(qry,id)
    return render_template('userviewsymptoms.html',val=res)




@app.route('/adminviewcomplaint',methods=['get','post'])
def adminviewcomplaint():
    qry="SELECT * FROM complaint INNER JOIN registration using (LoginID)"
    res=select(qry)
    return render_template('adminviewcomplaint.html',val=res)

@app.route('/adminsendreply',methods=['get','post'])
def adminsendreply():
    if "send" in request.form:
        r=request.form['r']
        cid=request.args['cid']
        qry="update complaint set reply=%s where complaint_id=%s"
        val=(r,cid)
        iud(qry,val)
        return '''<script> alert('send successfully');window.location='adminviewcomplaint'</script>'''

    return render_template('adminsendreply.html')



app.run(debug=True,port=5990)