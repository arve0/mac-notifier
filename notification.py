#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Foundation
import objc
import sys


def notify(title, text, subtitle=False, delay=0, sound=False, userInfo={}):
    """
    Notifies through OSX Notification Center.
    From: http://stackoverflow.com/questions/17651017/python-post-osx-notification
    """
    NSUserNotification = objc.lookUpClass('NSUserNotification')
    NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    if subtitle:
        notification.setSubtitle_(subtitle)
    notification.setInformativeText_(text)
    notification.setUserInfo_(userInfo)
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        notify(title=sys.argv[1], text=sys.argv[2], sound=True)
    else:
        usage = ('Notifies through OS X Notification Center with given title and text.\n\n' +
                 'Usage: \n{} title text \n'.format(sys.argv[0]))
        print(usage)
