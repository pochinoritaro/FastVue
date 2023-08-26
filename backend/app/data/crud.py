from .decorator import *
from .logics import varidate_password, makehash
from .models import Base, session, engine
from .models import User, UserInfo
from .models import LoginUser

def create_db():
	Base.metadata.create_all(bind=engine)
	
def get_user(user_name, password):
	pass

def read_userdata(name):
	data = session.query(User).filter(User.user_name==name).first()
	return data

@auto_commit
def set_user(user_name, password):
	if varidate_password(password):
		user_data = User(user_name=user_name, user_password=makehash(password))
		session.add(user_data)
	
	else:
		raise ValueError('lol')
