from LdShell import d
from LdShell import InitLdPlayer


#声明雷电模拟序号
InitLdPlayer("2");

#坐标点击
#d().Tap("10 10")


#元素点击
#d(resourceid="jp.naver.line.android:id/lds_box_button_container").Click()

#判断元素是否存在
#if(d(resourceid="jp.naver.line.android:id/lds_box_button_container").Exists()==True):
#    print("存在")
#    pass
#else:
#    print("不存在")
#    pass


#输入文字
#d().Input("한국")

#在屏幕上做划屏操作，前四个数为坐标点，后面是滑动的时间（单位毫秒）
#d().Swipe("50 50 500 500 20")

#按键代码参考https://blog.51cto.com/u_16099257/7853577
#d().Keyevent("4") #返回键

#启动APP,设置包名
#d().StartApp("in.zhaoj.shadowsocksr")


#停止APP,设置包名
#d().StopApp("in.zhaoj.shadowsocksr")

#上传文件
#d().UpFile("C:\\aaa.whl","/sdcard/")

#Adb命令
#d().Adb("shell input keyevent 4") #执行返回命令


#Shell命令
#d().Shell("input keyevent 4") #执行返回命令


#获取Text文本
#str=d(resourceid="jp.naver.line.android:id/lds_box_button_container").Text();
#print(str);

#获取Content文本
#str=d(resourceid="jp.naver.line.android:id/lds_box_button_container").Content();
#print(str);

#获取Child 子元素
##str=d(resourceid="jp.naver.line.android:id/lds_box_button_container").Child();
#print(str);


d(text="雷电游戏中心").Click()
