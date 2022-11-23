# Universal Copy/Paste

## Introduction

The purpose of this project is to send content copied from one computer to another computer, platform independently.

That way, you can copy for instance a text from a Windows PC and paste it to a Mac.

---

## How does it work?

Basically I'm using TCP connection by [socket library](https://docs.python.org/3/library/socket.html#creating-sockets) and clipboard feature by [pyperclip](https://pypi.org/project/pyperclip/) library.

I'm using the [pynput](https://pypi.org/project/pynput/) library in order to trigger the TCP sender.
