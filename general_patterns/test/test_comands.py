"""
Тестирование паттерна команда
"""
import pytest

from general_patterns.remote_control_commands.commands import LightOnCommand, GarageDoorOpenCommand, FanOnCommand, \
    FanOffCommand, GarageDoorCloseCommand, StereoOffCommand, StereoOnWithCDCommand, LightOffCommand
from general_patterns.remote_control_commands.control_subjects import Light, GarageDoor, CeilingFan, Stereo
from general_patterns.remote_control_commands.remote_control import SimpleRemoteControl, RemoteControl

# disable for fixture using
# pylint: disable=redefined-outer-name


def test_simple_remote_control():
    """Тестирование удаленного управления с одним слотом управления"""
    simple_remote_control = SimpleRemoteControl()

    light = Light()
    light_on = LightOnCommand(light)
    simple_remote_control.set_command(light_on)
    simple_remote_control.button_press()

    garage_door = GarageDoor()
    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    simple_remote_control.set_command(garage_door_open_command)
    simple_remote_control.button_press()


@pytest.fixture(scope='module')
def light_commands():
    """light_on_command and light_off_command"""
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)
    return light_on_command, light_off_command


@pytest.fixture(scope='module')
def stereo_commands():
    """stereo_on_command and stereo_off_command"""
    stereo = Stereo()
    cd_stereo_command = StereoOnWithCDCommand(stereo)
    stereo_off_command = StereoOffCommand(stereo)
    return cd_stereo_command, stereo_off_command


@pytest.fixture(scope='module')
def garage_commands():
    """garage_on_command and garage_off_command"""
    garage_door = GarageDoor()
    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    garage_door_close_command = GarageDoorCloseCommand(garage_door)
    return garage_door_open_command, garage_door_close_command


@pytest.fixture(scope='module')
def fan_commands():
    """fan_on_command and fan_off_command"""
    ceiling_fan = CeilingFan()
    fan_on_command = FanOnCommand(ceiling_fan)
    fan_off_command = FanOffCommand(ceiling_fan)
    return fan_on_command, fan_off_command


@pytest.fixture(scope='module')
def remote_control_with_commands(light_commands, stereo_commands, garage_commands, fan_commands):
    """A remote control created and filled in with commands"""
    remote_control = RemoteControl()

    light_on_command, light_off_command = light_commands
    fan_on_command, fan_off_command = fan_commands
    garage_door_open_command, garage_door_close_command = garage_commands
    cd_stereo_command, stereo_off_command = stereo_commands

    remote_control.set_commands(0, light_on_command, light_off_command)
    remote_control.set_commands(1, fan_on_command, fan_off_command)
    remote_control.set_commands(2, garage_door_open_command, garage_door_close_command)
    remote_control.set_commands(3, cd_stereo_command, stereo_off_command)
    return remote_control


def test_remote_control(remote_control_with_commands):
    """Тестирование удалённого управления с несколькими слотами управления"""
    remote_control = remote_control_with_commands
    remote_control.on_button_on_push(0)
    remote_control.on_button_off_push(0)
    remote_control.on_button_on_push(1)
    remote_control.on_button_off_push(1)
    remote_control.on_button_on_push(2)
    remote_control.on_button_off_push(2)
    remote_control.on_button_on_push(3)
    remote_control.on_button_off_push(3)


def test_no_command_slots(remote_control_with_commands):
    """test push to slot without commands"""
    remote_control = remote_control_with_commands
    remote_control.on_button_on_push(5)
    remote_control.on_button_off_push(5)


def test_undo_commands(remote_control_with_commands):
    """Тестирование удалённого управления с несколькими слотами управления"""

    remote_control = remote_control_with_commands
    for slot_num in range(5):
        _push_button_on_undo_and_push_again(remote_control, slot_num)
        _push_button_off_undo_and_push_again(remote_control, slot_num)


def _push_button_on_undo_and_push_again(remote_control, slot_num):
    remote_control.on_button_on_push(slot_num)
    remote_control.undo_button_push()
    remote_control.on_button_on_push(slot_num)


def _push_button_off_undo_and_push_again(remote_control, slot_num):
    remote_control.on_button_off_push(slot_num)
    remote_control.undo_button_push()
    remote_control.on_button_off_push(slot_num)
