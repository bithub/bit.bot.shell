import zope

import bit

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('bit.bot.shell')


class IShellVarDirective(zope.interface.Interface):
    """
    Define a shell var
    """
    name = zope.schema.TextLine(
        title=_("Name"),
        description=_("The shell var name"),
        required=True,
        )
    factory = zope.configuration.fields.GlobalObject(
        title=_("Factory"),
        description=_("The shell var factory"),
        required=True,
        )


def shell_var(_context, name, factory):
    _context.action(
        discriminator=None,
        callable=zope.component.provideUtility,
        args=(factory(), bit.bot.common.interfaces.IShellVar, name)
        )
