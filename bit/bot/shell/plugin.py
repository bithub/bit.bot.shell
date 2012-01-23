
from zope.interface import implements
from zope.component import getUtility

from twisted.manhole import telnet

from twisted.application import internet

from bit.bot.common.interfaces import IPlugin, IApplication, IServices

from bit.bot.base.plugin import BotPlugin

class BotShell(BotPlugin):
    implements(IPlugin)
    name = 'bit.bot.shell'

    @property
    def services(self):
        shell = telnet.ShellFactory()
        shell.username = "x"
        shell.password = "x"
        shell.namespace['app'] = getUtility(IApplication)
        shell.namespace['services'] = getUtility(IServices)
        return {'shell': dict(args=[8081, shell]
                                     ,service=internet.TCPServer)}

