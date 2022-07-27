# 需求说明

1. 给指定微信好友发消息

2. 获取所有微信好友的微信号

# 环境准备

Windows 10

Visual Studio Code 1.69.2

Clicknium 0.1.2

Python 3.10.5

微信 3.7.5.23

# 运行示例

- 参照[clicknium getting started](https://www.clicknium.com/documents) 设置开发环境

- 克隆[示例代码](https://github.com/automation9417/application-automation)

- 在Visual Studio Code打开WechatSearch文件夹

- 在Visual Studio Code中打开sample.py文件

- 按“F5”调试或者按“Ctrl+F5”运行代码



# 思路方案

## 1. 发送消息

1. 点击微信侧边栏**通讯录**  
   
   ![WechatSearch](/WechatSearch/.locator/wechat_img/ab13e383-64a6-43ae-9286-38c087cd220a.jpg)

2. 点击**搜索框**  
   
   ![](/WechatSearch/.locator/wechat_img/e9157cb1-1246-4f77-b239-4258d2c80ba1.jpg)

3. 点击**搜索结果第一条**  

4. 输入框输入消息

5. 点击**发送**按钮

## 2. 获取好友列表微信号

> 需要解决：怎么获取所有微信好友，因为好友列表需要鼠标滚动才能逐步显示完全，但是通过鼠标滚动的话，又存在一个问题，每次滚动显示好友列表数量不好控制？这时候可以利用先选中好友列表第一个，然后按键盘上 Down 键，就可以发现按一次，好友列表下移一次

1. 点击微信侧边栏**通讯录**  
   
   ![](/WechatSearch/.locator/wechat_img/ab13e383-64a6-43ae-9286-38c087cd220a.jpg)

2. 点击好友列表第一个  
   ![](/WechatSearch/.locator/wechat_img/91674ef2-101f-4b98-aa97-69d25369f63f.jpg)

3. 开始循环发送快捷键{DOWN}

4. 获取当前选中微信好友微信号
   
   > 通过[Recorder](https://www.clicknium.com/documents/developtools/vscode/recorder/) 我们可以很轻松定位到微信号，但是怎么获取相邻元素显示微信号呢？这时候可以通过 ui(locator.wechat.contact_id).parent.child(1).get_text()方式获取，逻辑就是定位到微信号元素后，再通过代码获取父一级元素即可；
   > ![](/WechatSearch/.locator/wechat_img/4c341dd1-38f7-44c4-ac10-7fafd25cbbce.jpg)

5. 判断当前选中是微信群还是企业微信号
   
   > 通过录制判断，我们可以发现只有微信好友才会显示**微信号**，所以通过这个特征来区分

6. 判断下移好友列表到底
   
   > 通过记录上一次微信和当前选中微信号，如果上一次微信号和当前微信号一致，就可以判断可以结束流程

# 知识准备

[Clicknium](https://www.clicknium.com/) 提供非常棒录制器方式和 Locator 理念，可以帮助你无需关注太多细节，非常轻松完成流程开发，所以有必要了解下。

1. [Locator](https://www.clicknium.com/documents/automation/locator)

2. [Recorder](https://www.clicknium.com/documents/developtools/vscode/recorder/)
   
   涉及到函数：

3. [click](https://www.clicknium.com/documents/api/python/uielement/click)

4. [set_text](https://www.clicknium.com/documents/api/python/uielement/set_text)

5. [is_existing](https://www.clicknium.com/documents/api/python/globalfunctions/is_existing)

6. [send_hotkey](https://www.clicknium.com/documents/api/python/globalfunctions/send_hotkey)

# 开始行动

1. 创建项目，新建文件夹，打开 Visual Studio Code，按下`Ctrl+Shift+P`快捷键，选择[Clicknium: Sample](https://www.clicknium.com/documents/developtools/vscode/project_management))，并且选择刚才新建文件即可；

2. 打开 sample.py 脚本文件,按照上述思路方案；
   
   #### 发送消息
   
   ```py
   def send_message(user, message):
       ui(locator.wechat.contact_button).click()
       ui(locator.wechat.search_user).set_text(
           user, InputTextBy.SendKeyAfterClick)
       ui(locator.wechat.search_result).click()
       ui(locator.wechat.message_input).set_text(
           message, InputTextBy.SendKeyAfterClick)
       ui(locator.wechat.message_send_button).click()
   ```
   
   #### 获取好友列表

```py
def get_contacts():
    ui(locator.wechat.contact_button).click()
    cc.find_element(locator.wechat.listitem_new_contact).click(
        mouse_button="left")
    preContactId = ''
    while True:
        cc.send_hotkey("{DOWN}")
        isContact = cc.is_existing(locator.wechat.contact_id)
        if isContact:
            curContactId = ui(
                locator.wechat.contact_id).parent.child(1).get_text()
            if curContactId == preContactId:
                break
            print('PreUserName:'+preContactId+' CurContactId:'+curContactId)
            preContactId = curContactId
```
