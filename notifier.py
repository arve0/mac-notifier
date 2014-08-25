#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Foundation
import objc
import sys


def notify(title, text, subtitle=False, delay=0, sound=False):
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
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

def bold(msg):
    return u'\033[1m%s\033[0m' % msg


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        if '-s' in sys.argv:
            sound = True
            sys.argv.remove('-s')
        else: sound = False
        title = sys.argv[1]
        text = ' '.join(sys.argv[2:])
        notify(title=title, text=text, sound=sound)
    else:
        usage = ('Notifies through OS X Notification Center with given title and text.\n\n' +
                 bold('Usage: ') + '\n{} [-s] title text \n\n'.format(sys.argv[0]) + 
                 '    ' + bold('-s') + ' will enable a sound notification.\n\n' +
                 bold('Example:') + '\n{} -s "Title with four words" Message doesnt need to be encapsulated'
                    .format(sys.argv[0]))
        print(usage)
