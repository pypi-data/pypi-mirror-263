from __future__ import annotations
import typing
__all__ = ['ColorFormat', 'Command', 'CommandExecutor', 'CommandSender', 'Logger', 'Permissible', 'PermissionAttachment', 'PermissionAttachmentInfo', 'PermissionDefault', 'Plugin', 'PluginCommand', 'PluginDescription', 'PluginLoader', 'PluginManager', 'Server']
class ColorFormat:
    AQUA: typing.ClassVar[str] = '§b'
    BLACK: typing.ClassVar[str] = '§0'
    BLUE: typing.ClassVar[str] = '§9'
    BOLD: typing.ClassVar[str] = '§l'
    DARK_AQUA: typing.ClassVar[str] = '§3'
    DARK_BLUE: typing.ClassVar[str] = '§1'
    DARK_GRAY: typing.ClassVar[str] = '§8'
    DARK_GREEN: typing.ClassVar[str] = '§2'
    DARK_PURPLE: typing.ClassVar[str] = '§5'
    DARK_RED: typing.ClassVar[str] = '§4'
    GOLD: typing.ClassVar[str] = '§6'
    GRAY: typing.ClassVar[str] = '§7'
    GREEN: typing.ClassVar[str] = '§a'
    ITALIC: typing.ClassVar[str] = '§o'
    LIGHT_PURPLE: typing.ClassVar[str] = '§d'
    MATERIAL_AMETHYST: typing.ClassVar[str] = '§u'
    MATERIAL_COPPER: typing.ClassVar[str] = '§n'
    MATERIAL_DIAMOND: typing.ClassVar[str] = '§s'
    MATERIAL_EMERALD: typing.ClassVar[str] = '§q'
    MATERIAL_GOLD: typing.ClassVar[str] = '§p'
    MATERIAL_IRON: typing.ClassVar[str] = '§i'
    MATERIAL_LAPIS: typing.ClassVar[str] = '§t'
    MATERIAL_NETHERITE: typing.ClassVar[str] = '§j'
    MATERIAL_QUARTZ: typing.ClassVar[str] = '§h'
    MATERIAL_REDSTONE: typing.ClassVar[str] = '§m'
    MINECOIN_GOLD: typing.ClassVar[str] = '§g'
    OBFUSCATED: typing.ClassVar[str] = '§k'
    RED: typing.ClassVar[str] = '§c'
    RESET: typing.ClassVar[str] = '§r'
    WHITE: typing.ClassVar[str] = '§f'
    YELLOW: typing.ClassVar[str] = '§e'
class Command:
    def execute(self, sender: CommandSender, args: list[str]) -> bool:
        """
        Executes the command, returning its success
        """
    def test_permission(self, target: CommandSender) -> bool:
        """
        Tests the given CommandSender to see if they can perform this command.
        """
    def test_permission_silently(self, target: CommandSender) -> bool:
        """
        Tests the given CommandSender to see if they can perform this command. No error is sent to the sender.
        """
    @property
    def aliases(self) -> list[str]:
        """
        List of aliases of this command
        """
    @aliases.setter
    def aliases(self, arg1: list[str]) -> None:
        ...
    @property
    def description(self) -> str:
        """
        Brief description of this command
        """
    @description.setter
    def description(self, arg1: str) -> Command:
        ...
    @property
    def name(self) -> str:
        """
        Name of this command.
        """
    @name.setter
    def name(self, arg1: str) -> bool:
        ...
    @property
    def permissions(self) -> list[str]:
        """
        The permissions required by users to be able to perform this command
        """
    @permissions.setter
    def permissions(self, arg1: list[str]) -> None:
        ...
    @property
    def registered(self) -> bool:
        """
        Returns the current registered state of this command
        """
    @property
    def usages(self) -> list[str]:
        """
        List of usages of this command
        """
    @usages.setter
    def usages(self, arg1: list[str]) -> None:
        ...
class CommandExecutor:
    def __init__(self) -> None:
        ...
    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        """
        Executes the given command, returning its success.
        """
class CommandSender(Permissible):
    def send_message(self, message: str) -> None:
        """
        Sends this sender a message
        """
    @property
    def name(self) -> str:
        """
        Gets the name of this command sender
        """
    @property
    def server(self) -> Server:
        """
        Returns the server instance that this command is running on
        """
class Logger:
    class Level:
        """
        Members:

          TRACE

          DEBUG

          INFO

          WARNING

          ERROR

          CRITICAL
        """
        CRITICAL: typing.ClassVar[Logger.Level]  # value = <Level.CRITICAL: 5>
        DEBUG: typing.ClassVar[Logger.Level]  # value = <Level.DEBUG: 1>
        ERROR: typing.ClassVar[Logger.Level]  # value = <Level.ERROR: 4>
        INFO: typing.ClassVar[Logger.Level]  # value = <Level.INFO: 2>
        TRACE: typing.ClassVar[Logger.Level]  # value = <Level.TRACE: 0>
        WARNING: typing.ClassVar[Logger.Level]  # value = <Level.WARNING: 3>
        __members__: typing.ClassVar[dict[str, Logger.Level]]  # value = {'TRACE': <Level.TRACE: 0>, 'DEBUG': <Level.DEBUG: 1>, 'INFO': <Level.INFO: 2>, 'WARNING': <Level.WARNING: 3>, 'ERROR': <Level.ERROR: 4>, 'CRITICAL': <Level.CRITICAL: 5>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    CRITICAL: typing.ClassVar[Logger.Level]  # value = <Level.CRITICAL: 5>
    DEBUG: typing.ClassVar[Logger.Level]  # value = <Level.DEBUG: 1>
    ERROR: typing.ClassVar[Logger.Level]  # value = <Level.ERROR: 4>
    INFO: typing.ClassVar[Logger.Level]  # value = <Level.INFO: 2>
    TRACE: typing.ClassVar[Logger.Level]  # value = <Level.TRACE: 0>
    WARNING: typing.ClassVar[Logger.Level]  # value = <Level.WARNING: 3>
    def critical(self, message: str) -> None:
        """
        Log a message at the CRITICAL level.
        """
    def debug(self, message: str) -> None:
        """
        Log a message at the DEBUG level.
        """
    def error(self, message: str) -> None:
        """
        Log a message at the ERROR level.
        """
    def info(self, message: str) -> None:
        """
        Log a message at the INFO level.
        """
    def is_enabled_for(self, level: Logger.Level) -> bool:
        """
        Check if the Logger instance is enabled for the given log Level.
        """
    def set_level(self, level: Logger.Level) -> None:
        """
        Set the logging level for this Logger instance.
        """
    def trace(self, message: str) -> None:
        """
        Log a message at the TRACE level.
        """
    def warning(self, message: str) -> None:
        """
        Log a message at the WARNING level.
        """
    @property
    def name(self) -> str:
        """
        Get the name of this Logger instance.
        """
class Permissible:
    @typing.overload
    def add_attachment(self, plugin: Plugin, name: str, value: bool) -> PermissionAttachment:
        """
        Adds a new PermissionAttachment.
        """
    @typing.overload
    def add_attachment(self, plugin: Plugin) -> PermissionAttachment:
        """
        Adds a new PermissionAttachment.
        """
    @typing.overload
    def has_permission(self, name: str) -> bool:
        """
        Checks if a permissions is available by name.
        """
    @typing.overload
    def has_permission(self, perm: ...) -> bool:
        """
        Checks if a permissions is available by permission.
        """
    @typing.overload
    def is_permission_set(self, name: str) -> bool:
        """
        Checks if a permissions is set by name.
        """
    @typing.overload
    def is_permission_set(self, perm: ...) -> bool:
        """
        Checks if a permissions is set by permission.
        """
    def recalculate_permissions(self) -> None:
        """
        Recalculates the permissions.
        """
    def remove_attachment(self, attachment: PermissionAttachment) -> bool:
        """
        Removes a given PermissionAttachment.
        """
    @property
    def effective_permissions(self) -> set[PermissionAttachmentInfo]:
        """
        Gets effective permissions.
        """
    @property
    def op(self) -> bool:
        """
        The operator status of this object
        """
    @op.setter
    def op(self, arg1: bool) -> None:
        ...
class PermissionAttachment:
    def __init__(self, plugin: Plugin, permissible: Permissible) -> None:
        ...
    def remove(self) -> bool:
        """
        Removes this attachment from its registered Permissible.
        """
    @typing.overload
    def set_permission(self, name: str, value: bool) -> None:
        """
        Sets a permission to the given value, by its fully qualified name.
        """
    @typing.overload
    def set_permission(self, perm: ..., value: bool) -> None:
        """
        Sets a permission to the given value.
        """
    @typing.overload
    def unset_permission(self, name: str) -> None:
        """
        Removes the specified permission from this attachment by name.
        """
    @typing.overload
    def unset_permission(self, perm: ...) -> None:
        """
        Removes the specified permission from this attachment.
        """
    @property
    def permissible(self) -> Permissible:
        """
        Gets the Permissible that this is attached to.
        """
    @property
    def permissions(self) -> dict[str, bool]:
        """
        Gets a copy of all set permissions and values contained within this attachment.
        """
    @property
    def plugin(self) -> Plugin:
        """
        Gets the plugin responsible for this attachment.
        """
    @property
    def removal_callback(self) -> typing.Callable[[PermissionAttachment], None]:
        """
        The callback to be called when this attachment is removed.
        """
    @removal_callback.setter
    def removal_callback(self, arg1: typing.Callable[[PermissionAttachment], None]) -> None:
        ...
class PermissionAttachmentInfo:
    def __init__(self, permissible: Permissible, permission: str, attachment: PermissionAttachment, value: bool) -> None:
        ...
    @property
    def attachment(self) -> PermissionAttachment:
        """
        Gets the attachment providing this permission.
        """
    @property
    def permissible(self) -> Permissible:
        """
        Get the permissible this is attached to
        """
    @property
    def permission(self) -> str:
        """
        Gets the permission being set
        """
    @property
    def value(self) -> bool:
        """
        Gets the value of this permission
        """
class PermissionDefault:
    """
    Members:

      TRUE

      FALSE

      OP

      OPERATOR

      NOT_OP

      NOT_OPERATOR
    """
    FALSE: typing.ClassVar[PermissionDefault]  # value = <PermissionDefault.FALSE: 1>
    NOT_OP: typing.ClassVar[PermissionDefault]  # value = <PermissionDefault.OP: 2>
    NOT_OPERATOR: typing.ClassVar[PermissionDefault]  # value = <PermissionDefault.NOT_OPERATOR: 3>
    OP: typing.ClassVar[PermissionDefault]  # value = <PermissionDefault.OP: 2>
    OPERATOR: typing.ClassVar[PermissionDefault]  # value = <PermissionDefault.OP: 2>
    TRUE: typing.ClassVar[PermissionDefault]  # value = <PermissionDefault.TRUE: 0>
    __members__: typing.ClassVar[dict[str, PermissionDefault]]  # value = {'TRUE': <PermissionDefault.TRUE: 0>, 'FALSE': <PermissionDefault.FALSE: 1>, 'OP': <PermissionDefault.OP: 2>, 'OPERATOR': <PermissionDefault.OP: 2>, 'NOT_OP': <PermissionDefault.OP: 2>, 'NOT_OPERATOR': <PermissionDefault.NOT_OPERATOR: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Plugin(CommandExecutor):
    def __init__(self) -> None:
        ...
    def _get_description(self) -> PluginDescription:
        ...
    def get_command(self, name: str) -> PluginCommand:
        """
        Gets the command with the given name, specific to this plugin.
        """
    def on_disable(self) -> None:
        """
        Called when this plugin is disabled
        """
    def on_enable(self) -> None:
        """
        Called when this plugin is enabled
        """
    def on_load(self) -> None:
        """
        Called after a plugin is loaded but before it has been enabled.
        """
    @property
    def enabled(self) -> bool:
        """
        Returns a value indicating whether this plugin is currently enabled
        """
    @property
    def logger(self) -> Logger:
        """
        Returns the plugin logger associated with this server's logger.
        """
    @property
    def name(self) -> str:
        """
        Returns the name of the plugin.
        """
    @property
    def plugin_loader(self) -> PluginLoader:
        """
        Gets the associated PluginLoader responsible for this plugin
        """
    @property
    def server(self) -> Server:
        """
        Returns the Server instance currently running this plugin
        """
class PluginCommand(Command):
    def __init__(self, plugin: Plugin, name: str, description: str | None = None, usages: list[str] | None = None, aliases: list[str] | None = None, permissions: list[str] | None = None) -> None:
        ...
    def _get_executor(self) -> CommandExecutor:
        ...
    def _set_executor(self, executor: CommandExecutor) -> None:
        ...
    @property
    def plugin(self) -> Plugin:
        """
        Gets the owner of this PluginCommand
        """
class PluginDescription:
    def __init__(self, name: str, version: str, description: str | None = None, authors: list[str] | None = None, prefix: str | None = None, *args, **kwargs) -> None:
        ...
    @property
    def authors(self) -> list[str]:
        """
        Gives the list of authors for the plugin.
        """
    @property
    def description(self) -> str:
        """
        Gives a human-friendly description of the functionality the plugin provides.
        """
    @property
    def full_name(self) -> str:
        """
        Returns the name of a plugin, including the version.
        """
    @property
    def name(self) -> str:
        """
        Gives the name of the plugin. This name is a unique identifier for plugins.
        """
    @property
    def prefix(self) -> str:
        """
        Gives the token to prefix plugin-specific logging messages with.
        """
    @property
    def version(self) -> str:
        """
        Gives the version of the plugin.
        """
class PluginLoader:
    def __init__(self, server: Server) -> None:
        ...
    def disable_plugin(self, plugin: Plugin) -> None:
        """
        Disables the specified plugin
        """
    def enable_plugin(self, plugin: Plugin) -> None:
        """
        Enables the specified plugin
        """
    def load_plugins(self, directory: str) -> list[Plugin]:
        """
        Loads the plugin contained within the specified directory
        """
class PluginManager:
    def clear_plugins(self) -> None:
        """
        Disables and removes all plugins
        """
    def disable_plugin(self, plugin: Plugin) -> None:
        """
        Disables the specified plugin
        """
    def disable_plugins(self) -> None:
        """
        Disables all the loaded plugins
        """
    def enable_plugin(self, plugin: Plugin) -> None:
        """
        Enables the specified plugin
        """
    def enable_plugins(self) -> None:
        """
        Enable all the loaded plugins
        """
    def get_plugin(self, name: str) -> Plugin:
        """
        Checks if the given plugin is loaded and returns it when applicable.
        """
    @typing.overload
    def is_plugin_enabled(self, plugin: str) -> bool:
        """
        Checks if the given plugin is enabled or not
        """
    @typing.overload
    def is_plugin_enabled(self, plugin: Plugin) -> bool:
        """
        Checks if the given plugin is enabled or not
        """
    def load_plugins(self, directory: str) -> list[Plugin]:
        """
        Loads the plugin contained within the specified directory
        """
    @property
    def plugins(self) -> list[Plugin]:
        """
        Gets a list of all currently loaded plugins
        """
class Server:
    def get_plugin_command(self, name: str) -> PluginCommand:
        """
        Gets a PluginCommand with the given name or alias.
        """
    def register_plugin_command(self, command: PluginCommand) -> PluginCommand:
        """
        Registers a new PluginCommand.
        """
    @property
    def logger(self) -> Logger:
        """
        Returns the primary logger associated with this server instance.
        """
    @property
    def minecraft_version(self) -> str:
        """
        Gets the Minecraft version that this server is running.
        """
    @property
    def name(self) -> str:
        """
        Gets the name of this server implementation.
        """
    @property
    def plugin_manager(self) -> PluginManager:
        """
        Gets the plugin manager for interfacing with plugins.
        """
    @property
    def version(self) -> str:
        """
        Gets the version of this server implementation.
        """
