# Create a Reminder

A user can create reminders in a couple of ways

1.  Start the message with `!remindme`
1.  Add a time to remind you
1.  Add the message to display when the reminder is resolved

## !remindme

The bot hook can be in any case.

* !remindme
* !REMINDME
* !rEmINdmE

## Time

You the bot can read any time format that Python's [dataparse](https://dateparser.readthedocs.io/en/latest/#) can.

Here are some common examples

* `!remindme in 2 days -m "Take the Turkey out of the oven!"`
* `!remindme tomorrow -m "Take the Roast out of the oven!"`
* `!remindme January 12, 2012 10:00 PM EST -m "Travel to the past and take the Turkey out of the oven!"`

## Message

The message should follow a `-m` flag surrounded in quotes.
This can be any string text that Discord can render.
