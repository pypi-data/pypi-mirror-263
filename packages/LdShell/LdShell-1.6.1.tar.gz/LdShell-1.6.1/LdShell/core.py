import requests
import json
class LdType() :
        none=0
        Click=1;       #点击
        Swipe=2      #滑动
        Long=3       #长按
        Exists=4     #是否存在
        Start=5      #启动包名
        Kill=6       #关闭包名
        Input=7      #输入文字
        Pull=8       #文件到电脑
        Push=9       #文件到手机
        Keyevent=10  #按键
        adb=11       #ADB命令
        shell=12       #Shell命令
        text=13
        content=14
        child=15
        Tap=16
class InitLdPlayer :
     index=0
     def __init__(self, index=None):
          InitLdPlayer.index=index
    
      
class d() :

    # 下面定义了一个类变量
    lds=None
    resourceid =None
    text=None
    _class=None
    package=None
    contentdesc=None
    index=None
    input_text=None
     
    def __init__(self, resourceid=None,text=None,cls=None,package=None,contentdesc=None,index=None):
        # 下面为Person对象增加2个实例变量
        self.resourceid = resourceid;
        self.text = text;
        self._class = cls;
        self.package = package;
        self.contentdesc = contentdesc;
        self.index = index;
    
    def initJson(self,type):
          self.lds = {
                "index":InitLdPlayer.index,
                "type":type,
                "txt":self.input_text,
                "cmd":{
                    "resourceid":self.resourceid,
                    "text":self.text,
                    "_class":self._class,
                    "package":self.package,
                    "contentdesc":self.contentdesc,
                    "index":self.index,
                }

            }
    def IniPost(self,ldtype):
        try:
            self.initJson(ldtype);
            url = 'http://127.0.0.1:33221/ldshell/'
            res = requests.post(url,json.dumps(self.lds))
            return bool(res.text)
        except:
             pass
        return False;
    def InistrPost(self,ldtype):
        try:
            self.initJson(ldtype);
            url = 'http://127.0.0.1:33221/ldshell/'
            res = requests.post(url,json.dumps(self.lds))
            return res.text
        except:
             pass
        return "";

    # 下面定义了一个CLick方法
    def Click(self):
        return self.IniPost(LdType.Click)



    # 下面定义了一个Input方法
    def Input(self,txt):
        self.input_text=txt
        return self.IniPost(LdType.Input)

    
    # 下面定义了一个Exists方法
    def Exists(self):
        return self.IniPost(LdType.Exists)


    # 下面定义了一个 Swipe 方法
    def Swipe(self,xy):
        self.input_text=xy
        return self.IniPost(LdType.Swipe)

    # 下面定义了一个 Keyevent 方法
    def Keyevent(self,key):
        self.input_text=key
        return self.IniPost(LdType.Keyevent)
    

    # 下面定义了一个 Start 方法
    def StartApp(self,pke):
        self.input_text=pke
        return self.IniPost(LdType.Start)
    
    # 下面定义了一个 Start 方法
    def StopApp(self,pke):
        self.input_text=pke
        return self.IniPost(LdType.Kill)
    

    # 下面定义了一个 UpFile 方法
    def UpFile(self,source,mubiao):
        self.input_text=source+" "+mubiao
        return self.IniPost(LdType.Push)
    

    # 下面定义了一个 Adb 方法
    def Adb(self,adb):
        self.input_text=adb
        return self.IniPost(LdType.adb)
    
    # 下面定义了一个 Shell 方法
    def Shell(self,shell):
        self.input_text=shell
        return self.IniPost(LdType.shell)
    
    # 下面定义了一个 Text 方法
    def Text(self):
        return self.InistrPost(LdType.text)
    
    # 下面定义了一个 Content 方法
    def Content(self):
        return self.InistrPost(LdType.content)

    # 下面定义了一个 Child 方法
    def Child(self):
        return self.InistrPost(LdType.child)
    

    # 下面定义了一个 Content 方法
    def Tap(self,xy):
        self.input_text=xy
        return self.IniPost(LdType.Tap)