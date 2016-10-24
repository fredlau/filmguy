#!/usr/bin/env python
#coding:utf-8

# updated by Fred Oct 24th 2016

import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import json
import requests
import torndb
from tornado.escape import json_decode
define("port", default=8000, help="Please send email to me", type=int)


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input_word):
        self.write(input_word[::-1])

#class DBHandler(tornado.web.RequestHandler):
#    def dbget(self):
#	db = tornado.Connection(host="localhost", database="saok",user="root", password="root")  
#	print db.execute("select * from kkk")
#	db.close()

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        #text = self.get_argument("text")
        #print self.request.body
	#DBHandler(self)
	data=eval(self.request.body)
	#print "*****************************"
	#print data
	#print data["username"],data["password"]
	usrname=data["username"]
	#print type(usrname)
	print "the name of the user is:"+usrname
	usrpass=data["password"]
	#print self.get_body_argument("params")
	#width = self.get_argument("width", 40)
	#password = self.get_argument("password", 40)
        #self.write(textwrap.fill(text, width))
	#self.write(textwrap.fill(data["username"]))
	#print textwrap.fill(password)
	#print res
	try:
	    print "connecting database"
	    db = torndb.Connection("localhost","saok","root","root")
	except Exception,e:
	    print "database connection Error !!!!"
	dbres = db.query("select * from kkk")
	print "====================="
	print dbres
	#userlist = []
	#for usr in dbres:
	#    #print "++++++++++++++"
	#    #print type(usr["username"])
	#    #print type(str(usr["username"]))
	#    userlist.append(str(usr["username"]))
	##print "user list is :"
	##print userlist
        ##for i in userlist:
        ##    print "DEBUG.........................................."
	##    print i
        ##    print usrname
	##    if usrname == i:
	##       print "OKOK"
	##    else:
        ##       print "something wrong!!!!"
	##if usrname in userlist and usrpass in:
	#if usrname in userlist:
	#    print "user already registered, login successfully"
	if data in dbres:
	    Loginsuccess = {"message":"login sucessfully",
                                "result":{"username":"default"},
                                "status":"1",
                                "errorcode":""}
	    Loginsuccess["result"]["username"] = usrname
	    self.write(Loginsuccess)
	    
	else:
	    print "########################"
	    print usrname
	    #print dbres
	    userlist = []
	    for usr in dbres:
		#print "++++++++++++++"
		#print type(usr["username"])
		#print type(str(usr["username"]))
		userlist.append(str(usr["username"]))
	    if usrname in userlist:
		LoginFailed = {"message":"login failed and password is incorrect",
                               "result":{"username":"default"},
                                "status":"0",
                                "errorcode":"103"}
		LoginFailed["result"]["username"] = usrname
		self.write(LoginFailed)
		print "user not found"
	    else:
		LoginFailed = {"message":"login failed and username not found",
                                "result":{"username":"default"},
                                "status":"0",
                                "errorcode":"106"}
		LoginFailed["result"]["username"] = usrname
		self.write(LoginFailed)
	    #self.write("user not found")
	#for usr in dbres:
	#    break;	  
	#    if usrname == usr["username"]:
	#	Loginsuccess = {"message":"login sucessfully",
        #                        "result":{"username":"default"},
        #                        "status":"1",
        #                        "errorcode":""}
	#	Loginsuccess["result"]["username"] = usrname
	#	print "Login Successfully!"
	#	self.write(Loginsuccess)
	#	break;
	#    else:
	#	self.write(textwrap.fill("User Not Found"))
	#	print "User not found "
	    #db.execute("insert into kkk(username,password) values('%s','%s')"%(usrname, usrpass))
	    #self.write("your username has been inserted into the database")
	db.close()

	#
	#self.write(textwrap.fill(usrname)
	
class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        #text = self.get_argument("text")
        #print self.request.body
	#DBHandler(self)
	data=eval(self.request.body)
	#print data["username"],data["password"]
	usrname=data["username"]
	#print type(usrname)
	print "the name of the user is:"+usrname
	usrpass=data["password"]
	#print self.get_body_argument("params")
	#width = self.get_argument("width", 40)
	#password = self.get_argument("password", 40)
        #self.write(textwrap.fill(text, width))
	#self.write(textwrap.fill(data["username"]))
	#print textwrap.fill(password)
	#print res
	try:
	    print "connecting database"
	    db = torndb.Connection("localhost","saok","root","root")
	except Exception,e:
	    print "database connection Error !!!!"
	dbres = db.query("select * from kkk")
	#print "====================="
	#print dbres
	userlist = []
	for usr in dbres:
	    #print "++++++++++++++"
	    #print type(usr["username"])
	    #print type(str(usr["username"]))
	    userlist.append(str(usr["username"]))
	#print "user list is :"
	#print userlist
        #for i in userlist:
        #    print "DEBUG.........................................."
	#    print i
        #    print usrname
	#    if usrname == i:
	#       print "OKOK"
	#    else:
        #       print "something wrong!!!!"
	if usrname in userlist:
	    print "user already registered"
	    RegisterFailed = {"message":"register failed, user already exist",
                                "result":{"username":"default"},
                                "status":"0",
                                "errorcode":"102"}
	    RegisterFailed["result"]["username"] = usrname
	    self.write(RegisterFailed)
	else:
	    RegisterSuccess = {"message":"register successfully",
                                "result":{"username":"default"},
                                "status":"1",
                                "errorcode":""}
	    RegisterSuccess["result"]["username"] = usrname
	    self.write(RegisterSuccess)
	    print "Register successfully"
	    #self.write("user not found")
	#for usr in dbres:
	#    break;	  
	#    if usrname == usr["username"]:
	#	Loginsuccess = {"message":"login sucessfully",
        #                        "result":{"username":"default"},
        #                        "status":"1",
        #                        "errorcode":""}
	#	Loginsuccess["result"]["username"] = usrname
	#	print "Login Successfully!"
	#	self.write(Loginsuccess)
	#	break;
	#    else:
	#	self.write(textwrap.fill("User Not Found"))
	#	print "User not found "
	    try:
		db.execute("insert into kkk(username,password) values('%s','%s')"%(usrname, usrpass))
	    except Exception,e:
		print "database connection Error !!!!"
	    #self.write("your username has been inserted into the database")
	db.close()

	#
	#self.write(textwrap.fill(usrname)
	
class UpgradeHandler(tornado.web.RequestHandler):
    def post(self):
	try:
	    data=eval(self.request.body)
	except Exception, e:
	    print "data format is incorrect:"
	    print e
	    self.write("data format is incorrect!!")
	print "Current Version is :"
	print data["curVersion"]
	UpgradeSuccess = {"message":"","result":
					{"newVersion":"1",
					"isNeedUpdate":"1",
					"updateType":"0",
					"updateMessage":""},
					"status":"1","errorcode":""}
	if data["curVersion"] == UpgradeSuccess["result"]["newVersion"]:
		
		self.write(UpgradeSuccess)
	else:
		UpgradeSuccess["result"]["errorcode"] = 105
		print UpgradeSuccess["result"]["errorcode"]
		self.write(UpgradeSuccess)

	
	
if __name__ == "__main__":
    try:
    	tornado.options.parse_command_line()
    	#app = tornado.web.Application(handlers = [(r"/reverse/(\w+)", ReverseHandler),(r"/wrap", WrapHandler),(r"/wrap", DBHandler)])
    	#app = tornado.web.Application(handlers = [(r"/reverse/(\w+)", ReverseHandler),(r"/wrap", WrapHandler)])
	app = tornado.web.Application(handlers = [(r"/reverse/(\w+)", ReverseHandler),(r"/login", LoginHandler),(r"/register", RegisterHandler),(r"/upgrade", UpgradeHandler)])
    	http_server = tornado.httpserver.HTTPServer(app)
    	http_server.listen(options.port)
    	tornado.ioloop.IOLoop.instance().start()
    except Exception, e:
	print e
	
