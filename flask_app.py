from flask import Flask, render_template, request, redirect, url_for,session,jsonify
app = Flask(__name__)
# DB 기본 코드
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete,ForeignKey
from hashlib import md5
import re

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

# 주의!!!! Secret_Key의 설정이 필요합니다. 추후에 추가 부탁드립니다!!
app.secret_key = "My_Secret_Key"
# 주의!!!! Secret_Key의 설정이 필요합니다. 추후에 추가 부탁드립니다!!

db = SQLAlchemy(app)

# DTO
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)

class Playlist(db.Model):  
    __tablename__ = 'Playlist'  
    plid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id = db.Column(db.String(30),ForeignKey('User.id'))
    name = db.Column(db.String(100), nullable=False)
    img = db.Column(db.String(100), nullable=False)

class Music(db.Model):    
    __tablename__ = 'Music' 
    mid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plid = db.Column(db.Integer,ForeignKey('Playlist.plid'))
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)

class Share(db.Model):    
    __tablename__ = 'Share'     
    index = db.Column(db.Integer,primary_key=True,autoincrement=True)
    id = db.Column(db.String(30),ForeignKey('User.id'))
    shareid = db.Column(db.String(30),ForeignKey('User.id'))



with app.app_context():
    db.create_all()

'''
_________________________________________________________
로그인 및 회원가입, 사용자 정보 관리를 위한 기능

'''
# 이승현 - index 페이지
@app.route("/")
def home():
    if "id" in session:
        return redirect(url_for('playlist', id=session['id']))
    else :        
        return render_template('index.html')

# 이승현 - 로그인 기능 : 사용자 입력을 받아 로그인 과정을 진행합니다.
@app.route("/login/",methods=['POST'])
def login():
    #form에서 보낸 데이터 받아오기
    id = request.form.get("id")    
    password = md5(request.form.get("password").encode('utf8')).hexdigest()
    user = db.session.query(User).filter_by(id=id,password=password).first()

    # 입력값이 없는 경우 오류 반환
    if(id == "" or password == ""):
        return jsonify(result = "fail",message="아이디 또는 비밀번호를 입력해주세요.")
    
    # 사용자 정보 확인
    if(user != None) :
        # 세션에 값을 저장
        session['id'] = id
        session['username'] = user.username
        # 플레이리스트 페이지로 이동 명령 전달
        return jsonify(result = "success",redirect='playlist/'+id)
    else :
        # 로그인 정보가 올바르지 않음 전달
        return jsonify(result = "fail",message="회원 정보가 일치하지 않습니다.")
    
# 이승현 - 회원가입 기능 : 사용자 정보를 받아 회원가입 과정을 진행합니다.
@app.route("/signup/",methods=['POST'])
def signup():
    #form에서 보낸 데이터 받아오기
    id = request.form.get("id")
    password = md5(request.form.get("password").encode('utf8')).hexdigest()
    name = request.form.get("name")

    # 이미 존재하는 계정인지 전달
    if(db.session.query(User).filter_by(id=id).first() != None) :
        return jsonify(result = "fail",message="이미 존재하는 아이디입니다.")
    else:            
        # 한 칸이라도 빈 칸이면 오류 전달
        if(id == "" or password == "" or name == "") :    
            return jsonify(result = "fail",message="모든 칸에 입력을 넣어주세요.")   

        # 아이디 조건 확인을 위한 정규식 확인
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,14}$',id): 
            # 비밀번호 조건 확인을 위한 정규식 확인
            if re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,20}$',request.form.get("password")):
                # 모든 조건 만족하면 유저 데이터 생성과 session 생성, 플레이리스트 페이지 이동
                user = User(id=id,password=password,username=name)
                db.session.add(user)
                db.session.commit()                
                session['id'] = id
                session['username'] = name
                return jsonify(result = "success",redirect='playlist/'+id)
            else :        
                # 비밀번호 정규식이 맞지 않을 경우
                return jsonify(result = "fail",message="적절하지 않은 비밀번호입니다.")
        else :
            # 아이디 정규식이 맞지 않을 경우
            return jsonify(result = "fail",message="적절하지 않은 아이디입니다.")

# 이승현 - 로그아웃 기능 : 사용자 세션 제거
@app.route("/logout/")
def logout():
    # 현재 저장된 세션 값을 비워준다.
    if "id" in session:
        session.pop('username', None)
        session.pop('id', None)
    return redirect(url_for('home'))

# 이승현 - 비밀번호 변경 : 사용자 비밀번호 변경
@app.route("/changePassword/",methods=['POST'])
def changePassword():
    # 입력 값을 전달
    password = md5(request.form.get("password").encode('utf8')).hexdigest()
    newpassword = md5(request.form.get("newpassword").encode('utf8')).hexdigest()
    newpasswordCheck = md5(request.form.get("newpasswordCheck").encode('utf8')).hexdigest()   
    
    # 한 칸이라도 비어있을 경우
    if(newpassword == "" or password == "" or newpasswordCheck == "") :
        return jsonify(result = "fail",message="모든 칸에 입력을 넣어주세요.")     
    else:
        user = db.session.query(User).filter_by(id=session['id'],password=password).first()
        # 비밀번호가 틀린 경우
        if(user != None) :
            # 비밀번호 확인 값이 다른 경우
            if(request.form.get("newpassword") != request.form.get("newpasswordCheck")):
                return jsonify(result = "fail",message="새 비밀번호가 일치하지 않습니다.")
            else:           
                # 새 비밀번호가 정규식에 맞지 않는 경우
                if re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,20}$',request.form.get("newpassword")):
                    # 비밀번호 변경 후 DB에 적용
                    user.password = newpassword                    
                    db.session.commit()
                    return jsonify(result = "success",redirect='/playlist/'+session['id'])
                else:
                    return jsonify(result = "fail",message="적절하지 않은 비밀번호입니다.")    
        else :
            return jsonify(result = "fail",message="비밀번호가 일치하지 않습니다.")


# 이승현 - 이름 변경 : 사용자 이름 변경
@app.route("/changeName/",methods=['POST'])
def changeName():
    newname = request.form.get("newname")
    user = db.session.query(User).filter_by(id=session['id']).first()
    user.username = newname
    db.session.commit()
    session['username'] = newname
    return jsonify(result = "success",redirect='/playlist/'+session['id'])

# 이승현 - 회원 탈퇴 : 회원 정보 삭제
@app.route("/withdraw/",methods=['POST'])
def withdraw():    
    user = db.session.query(User).filter_by(id=session['id']).first()
    # 해당 객체에 해당하는 delete 명령어를 통해 삭제 쿼리를 적용합니다.
    db.session.delete(user)
    db.session.commit()
    session.pop('username', None)
    session.pop('id', None)
    return jsonify(result = "success",redirect='/')



@app.route("/playlist/<id>/")
def playlist(id):
    playlists = Playlist.query.filter_by(id=id).all()    
    return render_template('playlists.html', playlists=playlists)

@app.route("/playlist/")
def playlist_call():
    return render_template('playlists.html', playlists=playlists)


@app.route("/music/create/")
def music_create():
    #form에서 보낸 데이터 받아오기
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_receive = request.args.get("image_url")

    # 데이터를 DB에 저장하기
    song = Song(username=username_receive, title=title_receive, artist=artist_receive, image_url=image_receive)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for('render_music_filter', username=username_receive))

# 음악 삭제 부분 구현됨 : 2024-06-11 / 이승현
@app.route("/music/delete/")
def music_delete():
    #form에서 보낸 데이터 받아오기
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")

    # 쿼리를 통해 조건에 해당하는 객체 song을 찾아냅니다.
    song = db.session.query(Song).filter_by(username=username_receive,title=title_receive, artist=artist_receive).first()
    # 해당 객체에 해당하는 delete 명령어를 통해 삭제 쿼리를 적용합니다.
    db.session.delete(song)
    #적용한 쿼리에 해당하는 커밋을 실행합니다. 
    db.session.commit()
    # 사용자의 음악이 하나인 경우에 대비해 모든 음악을 확인할 수 있는 music.html로 이동합니다.
    return redirect(url_for('music'))

if __name__ == "__main__":
    app.run(debug=True)