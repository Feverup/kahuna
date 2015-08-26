# -*- coding: utf-8 -*-

import requests
import logging
import copy
import json


logger = logging.getLogger('kahuna')

class Push(object):
    """A push notification. Set audience, message, etc, and send.
    
    Config Attributes: 
        "start_time" - Desired start time of the Push to be sent to the target user. Specified as seconds from the Epoch UTC time. You may specify at start_time up to 7 days in the future. If NOT specified defaults to the current time. Start times specified in the past will also default to the current time and shall be sent IMMEDIATELY. (Default = immediately)
        "optimal_hours" - Hours allowed to finish sending the Push message based on user behavior. For instance, if set to 4, we will attempt to find the best time over the 4 hour window to deliver the Push based on when the user is most likely to use your app. Valid values are 1-24. (Default = 0, aka Default = ASAP)
        "influence_rate_limiting" - Boolean flag used to determine if this Push should influence the Push cooldown for your Kahuna account. For instance, if you have another campaign scheduled to fire immediately after this push message, the other campaign Push will be rate-limited and not sent since the Push from this API will have already counted toward the Push cooldown under your account. (Default = true, aka Default = Will affect rate-limiting on your other campaigns)
        "observe_rate_limiting" - Boolean flag used to determine if this Push should be subject to rate limiting. For instance, if you have a Push cooldown of 8 hours and you schedule an API Push within 8 hours after your user has already received a Push from another one of your campaigns, this Push will be rate-limited and NOT get sent. (Default = true, aka Default = This push will may get rate-limited depending on what other campaigns you may have already sent for the day and what your cooldown is)

    """

    MAX_PUSH_PER_REQUEST = 100

    def __init__(self, kahuna):
        self._kahuna = kahuna
        self.options = None
        self.message = None
        self.params = {}
        self.target = []

        self._config = None
        self.start_time = None
        self.optimal_hours = None
        self.influence_rate_limiting = None
        self.observe_rate_limiting = None

    def _generate_config(self):
        self._config = {}
        if self.start_time:
            self._config['start_time'] = self.start_time
        if self.optimal_hours:
            self._config['optimal_hours'] = self.optimal_hours
        if self.influence_rate_limiting:
            self._config['influence_rate_limiting'] = self.influence_rate_limiting
        if self.start_time:
            self._config['start_time'] = self.start_time
        return self._config

    def send(self):
        """ Send the notification
        :returns: json: 
            "success" ­- true/false
            "error" -­ Optional human readable description of the error.
            "error_code" -­ Optional code identifying the specific error condition.
            "error_detail" -­ Optional details of the specific error condition. 
        """
        if not self._kahuna.url: # Tweak for testing purpose
            return {'success':True}

        push_template = {
            'notification': self.message,
            "target" : {
                "user_id" : "12345",
            }
        }

        # Split the pushes in batches, due to Kahuna constrain. 
        for i in range(len(self.target))[::self.MAX_PUSH_PER_REQUEST]:
            push_array = []
            target_subset = self.target[i:i+self.MAX_PUSH_PER_REQUEST]
            for user_id in target_subset:
                push_payload = copy.deepcopy(push_template)
                push_payload['target']['user_id'] = user_id
                push_array.append(push_payload)
            
            payload = { 'push_array': push_array,
                        'default_config': self._generate_config(),
                        'default_params': self.params
            }

            req = requests.post(
                self._kahuna.url,
                auth=(self._kahuna.username,
                      self._kahuna.password,
                ),
                data=json.dumps(payload),
            )

        logger.info('Push successful. push_ids: %s',
                    str(self.target))

        return req.json()


