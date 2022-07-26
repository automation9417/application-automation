from clicknium import clicknium as cc, locator, ui
from clicknium.common.enums import InputTextBy, PreAction
import time


def main():
    get_contacts()
    send_message('文件传输助手', 'hello clicknium')


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


def send_message(user, message):
    ui(locator.wechat.contact_button).click()
    ui(locator.wechat.search_user).set_text(
        user, InputTextBy.SendKeyAfterClick)
    ui(locator.wechat.search_result).click()
    ui(locator.wechat.message_input).set_text(
        message, InputTextBy.SendKeyAfterClick)
    ui(locator.wechat.message_send_button).click()


if __name__ == "__main__":
    main()
