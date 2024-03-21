import sys
import ctypes

if sys.platform == "win32":
    import win32file
else:
    import socket

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
        pipe_name = self.pipe_name + mmap_name
        print(f"Connecting to named pipe: {pipe_name}")
        try:
            if sys.platform == "win32":
                self.pipe = win32file.CreateFile(
                    pipe_name,
                    win32file.GENERIC_WRITE,
                    0,
                    None,
                    win32file.OPEN_EXISTING,
                    win32file.FILE_ATTRIBUTE_NORMAL,
                    None,
                )
            else:
                self.pipe = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.pipe.connect(pipe_name)

        except Exception as ex:
            print(ex)
            self.pipe = None

    def send_ping(self):
        ping_buffer = int.to_bytes(4, 4, sys.byteorder) + int.to_bytes(
            0, 4, sys.byteorder
        )
        try:
            self._send(ping_buffer)
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
            self._send(chat_buffer)
        except Exception as ex:
            print(ex)
            self.pipe = None

    def _send(self, buffer: bytes):
        if sys.platform == "win32":
            win32file.WriteFile(self.pipe, buffer)
        else:
            self.pipe.send(buffer)
