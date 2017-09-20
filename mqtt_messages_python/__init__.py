import re
from string import Template

from onoff import OnOffMixin


class MqttMessages(OnOffMixin):
    def addSubscription(self, channel, method):
        self.router.add_route(channel, method)
        self.subscriptions.append(re.sub(r"\{(.+?)\}", "+", channel))

    def addBinding(self, channel, event, retain=False, qos=0, dup=False):
        self.on(event, lambda d: self.sendMessage(channel,
                                                  d, retain, qos, dup))

    def onStateMsg(self, sender, val, method):
        route = Template('$base/$sender/state/$val').substite(
            base=self.base, sender=sender, val=val)
        self.addSubscription(route, method)

    def bindStateMsg(self, val, event):
        route = Template('$base/$name/state/$val').substitute(
            base=self.base, name=self.url_safe_plugin_name, val=val)
        self.addBinding(route, event, True)

    def onStateErrorMsg(self, sender, val, method):
        route = Template('$base/$sender/error/$val').substitute(
            base=self.base, sender=sender, val=val)
        self.addSubscription(route, method)

    def bindStateErrorMsg(self, val, event):
        route = Template('$base/$name/error/$val').substitute(
            base=self.base, name=self.url_safe_plugin_name, val=val)
        self.addBinding(route, event)

    def onPutMsg(self, val, method):
        route = Template('$base/put/$name/$val').substitute(
            base=self.base, name=self.url_safe_plugin_name, val=val)
        self.addSubscription(route, method)

    def bindPutMsg(self, receiver, val, event):
        route = Template('$base/put/$recevier/$val').substitute(
            base=self.base, receiver=receiver, val=val)
        self.addBinding(route, event)

    def onNotifyMsg(self, topic, method):
        route = Template('$base/notify/$name/$topic').substitute(
            base=self.base, name=self.url_safe_plugin_name, topic=topic)
        self.addSubscription(route, method)

    def bindNotifyMsg(self, receiver, topic, event):
        route = Template('$base/notify/$receiver/$topic').substitute(
            base=self.base, receiver=receiver, topic=topic)
        self.addBinding(route, event)

    def onStatusMsg(self, sender, method):
        route = Template('$base/status/$name').substitute(
            base=self.base, name=self.url_safe_plugin_name)
        self.addSubscription(route, method)

    def bindStatusMsg(self, event):
        route = Template('$base/status/$name').substitute(
            base=self.base, name=self.url_safe_plugin_name)
        self.addBinding(route, event)

    def onTriggerMsg(self, action, method):
        route = Template('$base/trigger/$name/$action').substitute(
            base=self.base, name=self.url_safe_plugin_name, action=action)
        self.addSubscription(route, method)

    def bindTriggerMsg(self, receiver, action, event):
        route = Template('$base/trigger/$receiver/$action').substitute(
            base=self.base, receiver=receiver, action=action)
        self.addBinding(route, event)

    def onSignalMsg(self, sender, topic, method):
        route = Template('$base/$sender/signal/$topic').substitute(
            base=self.base, sender=sender, topic=topic)
        self.addSubscription(route, method)

    def bindSignalMsg(self, topic, event):
        route = Template('$base/$name/signal/$topic').substitute(
            base=self.base, name=self.url_safe_plugin_name, topic=topic)
        self.addBinding(route, event)
