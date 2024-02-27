import re
from string import Template
from typing import Callable

from onoff import OnOffMixin

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


class MqttMessages(OnOffMixin):
    def addSubscription(self, channel: str, method: Callable) -> str:
        self.router.add_route(channel, method)
        subscription = re.sub(r"\{(.+?)\}", "+", channel)
        self.subscriptions.append(subscription)
        return subscription

    def addBinding(self, channel: str, event: str, retain: bool = False, qos: int = 0, dup: bool = False) -> None:
        return self.on(event, lambda d: self.sendMessage(channel, d, retain, qos, dup))

    def onStateMsg(self, sender: str, val: str, method: Callable) -> str:
        route = Template('$base/$sender/state/$val').substitute(
            base=self.base, sender=sender, val=val)
        return self.addSubscription(route, method)

    def bindStateMsg(self, val: str, event: str) -> None:
        route = Template('$base/$name/state/$val').substitute(
            base=self.base, name=self.url_safe_plugin_name, val=val)
        return self.addBinding(route, event, True)

    def onStateErrorMsg(self, sender: str, val: str, method: Callable) -> str:
        route = Template('$base/$sender/error/$val').substitute(
            base=self.base, sender=sender, val=val)
        return self.addSubscription(route, method)

    def bindStateErrorMsg(self, val: str, event: str) -> None:
        route = Template('$base/$name/error/$val').substitute(
            base=self.base, name=self.url_safe_plugin_name, val=val)
        return self.addBinding(route, event)

    def onPutMsg(self, val: str, method: Callable) -> str:
        route = Template('$base/put/$name/$val').substitute(
            base=self.base, name=self.url_safe_plugin_name, val=val)
        return self.addSubscription(route, method)

    def bindPutMsg(self, receiver: str, val: str, event: str) -> None:
        route = Template('$base/put/$receiver/$val').substitute(
            base=self.base, receiver=receiver, val=val)
        return self.addBinding(route, event)

    def onNotifyMsg(self, sender: str, topic: str, method: Callable) -> str:
        route = Template('$base/$sender/notify/$name/$topic').substitute(
            base=self.base, sender=sender, name=self.url_safe_plugin_name, topic=topic)
        return self.addSubscription(route, method)

    def bindNotifyMsg(self, receiver: str, topic: str, event: str) -> None:
        route = Template('$base/$name/notify/$receiver/$topic').substitute(
            base=self.base, name=self.url_safe_plugin_name, receiver=receiver, topic=topic)
        return self.addBinding(route, event)

    def onStatusMsg(self, sender: str, method: Callable) -> str:
        route = Template('$base/status/$name').substitute(
            base=self.base, name=self.url_safe_plugin_name)
        return self.addSubscription(route, method)

    def bindStatusMsg(self, event: str) -> None:
        route = Template('$base/status/$name').substitute(
            base=self.base, name=self.url_safe_plugin_name)
        return self.addBinding(route, event)

    def onTriggerMsg(self, action: str, method: Callable) -> str:
        route = Template('$base/trigger/$name/$action').substitute(
            base=self.base, name=self.url_safe_plugin_name, action=action)
        return self.addSubscription(route, method)

    def bindTriggerMsg(self, receiver: str, action: str, event: str) -> None:
        route = Template('$base/trigger/$receiver/$action').substitute(
            base=self.base, receiver=receiver, action=action)
        return self.addBinding(route, event)

    def onSignalMsg(self, sender: str, topic: str, method: Callable) -> str:
        route = Template('$base/$sender/signal/$topic').substitute(
            base=self.base, sender=sender, topic=topic)
        return self.addSubscription(route, method)

    def bindSignalMsg(self, topic: str, event: str) -> None:
        route = Template('$base/$name/signal/$topic').substitute(
            base=self.base, name=self.url_safe_plugin_name, topic=topic)
        return self.addBinding(route, event)
