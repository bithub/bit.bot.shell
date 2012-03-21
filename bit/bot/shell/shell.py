from zope.interface import implementer
from zope.component import getUtility, getAllUtilitiesRegisteredFor

from twisted.manhole import telnet

from bit.core.interfaces import IConfiguration, IApplication, IServices
from bit.bot.common.interfaces import IShellVar


def getShellPort():
    return int(getUtility(IConfiguration).get('shell', 'port'))


def getShell():
    print 'creating shell'
    shell = telnet.ShellFactory()
    shell.username = getUtility(IConfiguration).get('shell', 'username')
    shell.password = getUtility(IConfiguration).get('shell', 'password')
    for k, v in getAllUtilitiesRegisteredFor(IShellVar):
        shell.namespace[str(k)] = v
    return shell


def shellVarApp():
    print 'setting shell app var'
    return getUtility(IApplication)


@implementer(IShellVar)
def shellVarServices():
    return getUtility(IServices)
