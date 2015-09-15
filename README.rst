About
=====

``kahuna`` is a Python library for using the `Kahuna
<http://kahuna.com/>`_ web service API for push notifications.

Requirements
============

Python 2.6, 2.7, 3.3 or 3.4 is required.
Requests module

Usage
=====

Simple iOS Push
---------------

    >>> from kahuna import Kahuna
    >>> kahuna = Kahuna(url, username, password)
    >>> push = kahuna.create_push()
    >>> push.target = [user_ids]
    >>> push.send()


Curl test: curl https://secret:secret@tap-nexus.appspot.com/api/push?env=s -H "Content-Type: application/json" -X POST -d "{'push_array': [{'notification': {'alert': 'This the test'}, 'target': {'email': 'fevertesting5@feverup.com'}}]}"
