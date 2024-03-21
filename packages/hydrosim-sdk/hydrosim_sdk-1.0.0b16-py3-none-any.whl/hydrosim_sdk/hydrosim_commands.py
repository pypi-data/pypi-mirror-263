import sys
import ctypes
import win32file
import asyncio
from .hydrosim_structs import ChatMessageIPC


class CommandTypes:
    ServerSettings = 1
    Rules = 2
    Chat = 3


class HydroSimCommands:
    pipe = None
    pipe_name = ""
    mmap_name = ""

    def __init__(self, pipe_name, mmap_name=""):
        self.pipe_name = pipe_name
        self.mmap_name = mmap_name

    async def connect(self):
        while True:
            self.init_pipe()

            # Need to send a ping due to issues with closing
            # the named pipe server.
            if self.pipe:
                self.send_ping()
            else:
                print("Failed to connect to named pipe.")

            await asyncio.sleep(1)

    def init_pipe(self):
        if self.pipe:
            return

        mmap_name = ""
        if self.mmap_name:
            mmap_name = f".{self.mmap_name}"
        print(mmap_name)
        try:
            pipe_name = r"\\.\pipe\HydroSim" + mmap_name
            print(f"Connecting to named pipe: {pipe_name}")
            self.pipe = win32file.CreateFile(
                r"\\.\pipe\HydroSim" + mmap_name,
                win32file.GENERIC_WRITE,
                0,
                None,
                win32file.OPEN_EXISTING,
                win32file.FILE_ATTRIBUTE_NORMAL,
                None,
            )
        except Exception as ex:
            print(ex)
            self.pipe = None

    def send_ping(self):
        ping_buffer = int.to_bytes(4, 4, sys.byteorder) + int.to_bytes(
            0, 4, sys.byteorder
        )
        try:
            win32file.WriteFile(self.pipe, ping_buffer)
        except Exception as ex:
            print(ex)
            self.pipe = None

    def send_chat(self, message: str):
        chat = ChatMessageIPC()
        chat.message = message
        chat_len = ctypes.sizeof(chat) + 4
        chat_buffer = (
            int.to_bytes(chat_len, 4, sys.byteorder)
            + int.to_bytes(CommandTypes.Chat, 4, sys.byteorder)
            + bytes(chat)
        )
        try:
            win32file.WriteFile(self.pipe, chat_buffer)
        except Exception as ex:
            print(ex)
            self.pipe = None
