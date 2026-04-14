#!/usr/bin/env python3
import argparse
import json
import platform
import shutil
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def parse_args():
    parser = argparse.ArgumentParser(
        description="Send text or clipboard content to another machine."
    )
    parser.add_argument("--host", required=True, help="Target IP or hostname")
    parser.add_argument("--port", type=int, default=8765, help="Receiver port")
    parser.add_argument("--token", default="", help="Optional shared token")
    parser.add_argument(
        "--sender",
        default=platform.node() or "unknown-sender",
        help="Sender name shown on the receiver side",
    )
    parser.add_argument("--clipboard", action="store_true", help="Send clipboard content")
    parser.add_argument("text", nargs="*", help="Text to send")
    return parser.parse_args()


def read_clipboard():
    clipboard_commands = [
        ["pbpaste"],
        ["wl-paste", "-n"],
        ["xclip", "-selection", "clipboard", "-o"],
        ["xsel", "--clipboard", "--output"],
    ]

    for cmd in clipboard_commands:
        if shutil.which(cmd[0]):
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout

    raise RuntimeError("No supported clipboard command found.")


def read_text(args):
    if args.clipboard:
        return read_clipboard()
    if args.text:
        return " ".join(args.text)
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise RuntimeError("Provide text, stdin, or use --clipboard.")


def main():
    args = parse_args()
    text = read_text(args).strip()
    if not text:
        raise RuntimeError("Nothing to send.")

    url = f"http://{args.host}:{args.port}/send"
    payload = json.dumps(
        {"text": text, "token": args.token, "sender": args.sender},
        ensure_ascii=False,
    ).encode("utf-8")

    request = Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=10) as response:
            body = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Server returned HTTP {exc.code}: {message}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not connect to receiver: {exc}") from exc

    print("Send complete")
    print(f"Receiver: {body.get('device_name')}")
    print(f"Saved to: {body.get('saved_to')}")
    print(f"Characters: {body.get('chars')}")


if __name__ == "__main__":
    main()
