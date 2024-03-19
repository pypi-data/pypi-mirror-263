# notifications

Notify you that your code finished running.

# Slack

Steps to setup slack notifications:

1. Create a slack app and get the webhook URL (https://api.slack.com/messaging/webhooks)
2. Obtain the webhook URL such as `https://hooks.slack.com/services/XXXX/XXXXX/XXXXXX`, then run `python -m noti.auth` and paste the URL when prompted.
3. After that, you can either use:

```python
import noti

with noti.slack.watch("do some work..."):
    ...
```

to be notified when the code block finishes, or use:

```python
import noti
noti.slack("done!")
```
