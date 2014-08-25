# Mac notifier #
Send notifications to OS X Notification Center with python or shell.

## Usage ##
### Shell ###
'''Usage:'''
```
./notifier.py [-s] title text 

    -s will enable a sound notification.
```

'''Example:'''
```
./notifier.py -s "Title with four words" Message doesnt need to be encapsulated./notifier.py 'Notification iiik' 'Message about broken...'
```


### Python ###
```
from notifier import notify

notify('Notification iiik', 'Message about broken...')
```

All options:
```
notify(title, text, subtitle=False, delay=0, sound=False):
```
