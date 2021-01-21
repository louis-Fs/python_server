#-*- coding:utf-8 -*-
import sys, os, subprocess
from http.server import BaseHTTPRequestHandler,HTTPServer
import time

#louis add  louis  loui  osui  louis   addad adadadadadada adda
from cgi import parse_header, parse_multipart
import cgi
from urllib import parse
import datetime

#+++++++++++++++++++%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import pymysql

def Login_SQL(usr,pwd):
   db = pymysql.connect(
      host='47.107.176.184',
      port=3306,
      user='root',
      password='root',
      db='webuser',
      charset='utf8')
   
   # 使用cursor()方法获取操作游标 
   cursor = db.cursor()
   
   # SQL 查询语句
   sql1 = "SELECT * FROM user WHERE name='%s' AND password='%s' " %(usr,pwd)
   sql2 = "SELECT * FROM user WHERE name='%s' "%(usr)
   try:
      # 执行SQL语句
      cursor.execute(sql2)
      # 获取所有记录列表
      results_1 = cursor.fetchall()
      if results_1:
         cursor.execute(sql1)
         results_2 = cursor.fetchall()
         if results_2:
            db.close()
            return 3 #正确
         else:
            db.close()
            return 4 #密码错误
      else:
         db.close()
         return 5 #无用户

   except:
      print ("Error: unable to fetch data")

def Register_SQL(usr,pwd):
   db = pymysql.connect(
      host='47.107.176.184',
      port=3306,
      user='root',
      password='root',
      db='webuser',
      charset='utf8')
   
   # 使用cursor()方法获取操作游标 
   cursor = db.cursor()
   
   # SQL 查询语句
   sql = "INSERT INTO user (name,password) VALUE ('%s','%s') " %(usr,pwd)
   print(sql)
   try:
      # 执行SQL语句
      
      cursor.execute(sql)
      db.commit()

   except:
      print ("Error: unable to fetch data")
   db.close()



import hashlib

md5_dict={}


#louis          ------------louis   lous    adaddad
ddir=os.getcwd()
print(ddir)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def get_file_md5(file_path):
    with open(file_path,'rb') as f:
        md5obj=hashlib.md5()
        md5obj.update(f.read())
        hashstr=md5obj.hexdigest()
    return hashstr    

def get_md5dict(dir):
    for root,dirs, files in os.walk(dir):
        for filename in files:
            md5_dict[filename]=get_file_md5(os.path.join(root, filename))

def print_log(address,log_date_time,reqline,status):
    output_dir =ddir+ "\log\\server"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H'))
    filename = os.path.join(output_dir, log_name)
    with open(filename,'a+') as f:
        f.write("%s - - [%s] %s %d\n" %(address,log_date_time,reqline,status))

def print_usrlog(usr,pws):
    output_dir =ddir+ "\log\\usr"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H'))
    current_time='{}'.format(time.strftime('%Y-%m-%d-%H-%M-%S'))
    filename = os.path.join(output_dir, log_name)
    with open(filename,'a+') as f:
        f.write("%s - - [用户:%s] 密码:%s 登录\n" %(current_time,usr,pws))

def print_filelog(fname,filesize):
    output_dir =ddir+ "\log\\usr"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H'))
    current_time='{}'.format(time.strftime('%Y-%m-%d-%H-%M-%S'))
    filename = os.path.join(output_dir, log_name)
    with open(filename,'a+') as f:
        f.write("%s - - 上传 文件:%s 文件大小:%s \n" %(current_time,fname,filesize))

def access_log(myCookie):
    #record_list = []
    #log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H'))
    #log_path = ddir + "/log/server/" + log_name
    #r = open(log_path,'r')
    #records = r.readlines()
    #for record in records:
    #    old_address = record.split()[0]
    #     record_list.append(old_address)
    
    if myCookie == None:
        num_path = os.getcwd() + '/Record/number.log'
        today = datetime.date.today()
        today_str = today.strftime('%Y-%m-%d')
        f = open(num_path,'r+')
        datas = f.readlines()
        f.close()
        w = open(num_path,'w')
        w.writelines([item for item in datas[:-1]])
        data = datas[len(datas)-1].split()
        lastDay = data[0]
        if lastDay == today_str:
            count = int(data[1])
            count = count + 1
            w.write("%s\t%d"%(today_str,count))
        else:
            if len(datas)==1:
                w.write("%s\t\t%s"%(data[0],data[1]))
            else:
                w.write("%s\t%s"%(data[0],data[1]))
            w.write("\n%s\t1"%today_str)
        w.close()
    else:
        pass

#-------------------------------------------------------------------------------

class ServerException(Exception):
    '''服务器内部错误'''
    pass

#-------------------------------------------------------------------------------

class base_case(object):
    '''条件处理基类'''

    def handle_file(self, handler, full_path, ):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
                handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)




    #add louis ///////////////////////////////////////////////////////louisLOUIS  LOUIS/\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def handle_file_post(self, handler, full_path,value):
        try:
            with open(full_path, 'rb') as reader:
                byte = reader.read()
                by=str(byte,encoding="utf-8")
                con=by.format(value[0],value[1])
                content=con.encode("utf-8")
                handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)


#^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%






    def index_path(self, handler):

        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        assert False, 'Not implemented.'

    def act(self, handler):
        assert False, 'Not implemented.'

#-------------------------------------------------------------------------------

class case_no_file(base_case):
    '''文件或目录不存在'''
    status=404
    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))

#-------------------------------------------------------------------------------

class case_cgi_file(base_case):
    '''可执行脚本'''
    status=200
    def run_cgi(self, handler):
        data = subprocess.check_output(["python", handler.full_path.replace('/','\\')],shell=False)
        handler.send_content(data)

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.py')

    def act(self, handler):
        self.run_cgi(handler)

class case_image_file(base_case):
    '''可执行脚本'''
    code=200
    def handle_file(self, handler, full_path ):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
                handler.send_content_image(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.png')

    def act(self, handler):
        self.handle_file(handler,handler.full_path)

class case_css_file(base_case):
    '''可执行脚本'''
    code=200
    def handle_file(self, handler, full_path ):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
                handler.send_content_css(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.css')

    def act(self, handler):
        self.handle_file(handler,handler.full_path)

class case_js_file(base_case):
    '''可执行脚本'''
    code=200

    def handle_file(self, handler, full_path ):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
                handler.send_content_js(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.js')

    def act(self, handler):
        self.handle_file(handler,handler.full_path)

#-------------------------------------------------------------------------------

class case_existing_file(base_case):
    '''文件存在的情况'''
    status=200
    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        self.handle_file(handler, handler.full_path)

#-------------------------------------------------------------------------------

class case_directory_index_file(base_case):
    '''在根路径下返回主页文件'''
    status=200
    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))

    def act(self, handler):
        self.handle_file(handler, self.index_path(handler))

#-------------------------------------------------------------------------------

class case_always_fail(base_case):
    '''默认处理'''
    status=404
    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))

#-------------------------------------------------------------------------------



#add louis############################################      louis    loOIS    LOUIS    LOUIS   LOUIS
class case_post_fileupload(base_case):
    '''文件上传'''
    status=200

    def act(self,handler):
        form = cgi.FieldStorage(
            fp=handler.rfile,
            headers=handler.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':handler.headers['Content-Type'],
                     }
        )
        for field in form.keys():

            field_item = form[field]
            filename = field_item.filename
            filevalue  = field_item.value
            filesize = len(filevalue)#文件大小(字节)
            #print len(filevalue)
            if_path=ddir+"/save"
            if not os.path.exists(if_path):
                os.mkdir(if_path)
            usr_path="/save/"+filename.encode('utf-8').decode('utf-8')
            base_path=ddir+"/save/"+filename.encode('utf-8').decode('utf-8')
            value=[filename,usr_path]

            print(filename,filesize)
            print_filelog(filename,filesize)
            
            with open(base_path,'wb') as f:
                f.write(filevalue)
        self.handle_file_post(handler, handler.full_path,value)



class case_post_login(base_case):
    ''' 用户登录'''
    status=200
    def act(self,handler):
        form = cgi.FieldStorage(
            fp=handler.rfile,
            headers=handler.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':handler.headers['Content-Type'],
                     }
        )
        
        pws=form['password'].value
        usr=form['username'].value
        print(Login_SQL(usr,pws))
        if Login_SQL(usr,pws)==3:
            value=['success,hello,dear: '+usr,'your pws is: '+pws]
            self.handle_file_post(handler, handler.full_path,value)
            print('9999')
        elif Login_SQL(usr,pws)==4:
               value=['failed,hello,dear: '+usr,'your pws: '+pws+' is wrong']
               self.handle_file_post(handler, handler.full_path,value)
        elif Login_SQL(usr,pws)==5:
               value=['failed,no user: '+usr,'no pws: '+pws]
               self.handle_file_post(handler, handler.full_path,value)
        print("用户:",usr,"密码:",pws)


class case_post_reg(base_case):
    ''' 用户注册'''
    status=200
    def act(self,handler):
        form = cgi.FieldStorage(
            fp=handler.rfile,
            headers=handler.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':handler.headers['Content-Type'],
                     }
        )
        
        pws=form['password'].value
        usr=form['username'].value
        value=['your name is:  '+usr,'your pws is:  '+pws]
        Register_SQL(usr,pws)
        print("用户:",usr,"密码:",pws)
        print_usrlog(usr,pws)
        self.handle_file_post(handler, handler.full_path,value)
#+++++++%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5%%%%%%%%%%%%%%%%%



class RequestHandler(BaseHTTPRequestHandler):
    '''
    请求路径合法则返回相应处理
    否则返回错误页面
    '''
    Cases = [case_no_file(),
             case_css_file(),
             case_js_file(),
             case_cgi_file(),
             case_image_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_always_fail()]
    
    #add louis-------------------------------------------add ouis louis louis  louis
    post_case =[case_post_fileupload(),case_post_login(),case_post_reg()]
#+++++%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
    # 错误页面模板
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """


    def do_GET(self):
        try:
            # 得到完整的请求路径
            self.full_path = os.getcwd() + "/WWW" +self.path
            if self.full_path.endswith('.html'):
                key=get_file_md5(self.full_path)
                if  key == md5_dict[self.path[1:]]:
                    pass
                else:
                    raise Exception("页面已被更改")
            else:
                pass
                
            # 遍历所有的情况并处理
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break
                
            print_log(self.address_string(),self.log_date_time_string(),self.requestline,case.status)
            access_log(self.getMyCookie())

            
        # 处理异常
        except Exception as msg:
            print_log(self.address_string(),self.log_date_time_string(),self.requestline,404)
            access_log(self.getMyCookie())

            


        
    #add lou  LOUIS LOUIS LOUIS LOUIS#######################@@@@@@@@@@@@@@@@@@  luis louis louis

            
    ####处理post请求########处理POST请 POS################
    def do_POST(self):
        try:
            # 得到完整的请求路径
            self.full_path = (os.getcwd() + "/WWW" + self.path)
            
        # 处理异常
        except Exception as msg:
            print_log(self.address_string(),self.log_date_time_string(),self.requestline,404)
            self.handle_error(msg)


        ############判断请求类型###########类型。诶新###########

        if self.path=="/upload.html":
            print_log(self.address_string(),self.log_date_time_string(),self.requestline,self.post_case[0].status)
            self.post_case[0].act(self)
        elif self.path=="/login.html":
            print_log(self.address_string(),self.log_date_time_string(),self.requestline,self.post_case[1].status)
            self.post_case[1].act(self)
        elif self.path=="/reg.html":
            print_log(self.address_string(),self.log_date_time_string(),self.requestline,self.post_case[2].status)
            self.post_case[2].act(self)



#++%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"), 404)

    # 发送数据到客户端

    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html;charset=utf-8")
        self.send_header("Set-Cookie","myCookie=alreadyaccess")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)
 
    def send_content_css(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/css;charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def send_content_js(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/javascript;charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def send_content_jpg(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "image/png;charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def getMyCookie(self):
        cookies = self.headers.get_all("Cookie")
        if cookies != None:
            return cookies[0].split('=')[1]
        else:
            return None

       

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    
    get_md5dict(ddir)
    serverAddress = ('localhost', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
