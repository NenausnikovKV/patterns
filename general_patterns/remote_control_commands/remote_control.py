"""
Пульт управления
"""
from general_patterns.remote_control_commands.commands import NoCommand


class SimpleRemoteControl:
    """Пульт управления с одним слотом управления"""
    def __init__(self):
        self.slot = None

    def set_command(self, command):
        """Занять слот командой"""
        self.slot = command

    def button_press(self):
        """Выполнить команду по нажатию на кнопку"""
        self.slot.execute()


class RemoteControl:
    """
    Пульт управления с несколькими слотами устройств
    """
    _SLOT_COUNT = 7

    def __init__(self):
        no_command = NoCommand()
        self.on_commands = [no_command for _ in range(self._SLOT_COUNT)]
        self.off_commands = [no_command for _ in range(self._SLOT_COUNT)]
        self.last_command = NoCommand()

    def set_commands(self, slot_num, on_command, off_command):
        """Установить команды включения и выключения для разъема с заданным номером"""
        self.on_commands[slot_num] = on_command
        self.off_commands[slot_num] = off_command

    def on_button_on_push(self, slot_num):
        """Нажатие на кнопку включить"""
        self.on_commands[slot_num].execute()
        self.last_command = self.on_commands[slot_num]

    def on_button_off_push(self, slot_num):
        """Нажатие на кнопку выключить"""
        self.off_commands[slot_num].execute()
        self.last_command = self.off_commands[slot_num]

    def undo_button_push(self):
        """undo las command"""
        self.last_command.undo()
