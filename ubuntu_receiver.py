#!/usr/bin/env python3
import argparse
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run a small HTTP server on Ubuntu to receive text snippets."
    )
    parser.add_argument("--host", default="0.0.0.0", help="Bind host, default: 0.0.0.0")
    parser.add_argument("--port", type=int, default=8765, help="Bind port, default: 8765")
    parser.add_argument(
        "--output",
        default="received_messages.txt",
        help="File used to store received text, default: received_messages.txt",
    )
    parser.add_argument(
        "--token",
        default="",
        help="Optional shared token. If set, sender must provide the same token.",
    )
    return parser.parse_args()


def build_handler(output_file: Path, token: str):
    class ReceiverHandler(BaseHTTPRequestHandler):
        def _send_json(self, status: int, payload: dict):
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path != "/":
                self._send_json(404, {"ok": False, "error": "Not found"})
                return
            self._send_json(
                200,
                {
                    "ok": True,
                    "message": "Ubuntu receiver is running",
                    "output_file": str(output_file.resolve()),
                },
            )

        def do_POST(self):
            if self.path != "/send":
                self._send_json(404, {"ok": False, "error": "Not found"})
                return

            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length)

            try:
                payload = json.loads(raw_body.decode("utf-8"))
            except json.JSONDecodeError:
                self._send_json(400, {"ok": False, "error": "Body must be valid JSON"})
                return

            if token and payload.get("token") != token:
                self._send_json(403, {"ok": False, "error": "Invalid token"})
                return

            text = (payload.get("text") or "").rstrip()
            if not text:
                self._send_json(400, {"ok": False, "error": "Field 'text' cannot be empty"})
                return

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            block = f"[{now}]\n{text}\n\n{'-' * 40}\n"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with output_file.open("a", encoding="utf-8") as f:
                f.write(block)

            self._send_json(
                200,
                {
                    "ok": True,
                    "saved_to": str(output_file.resolve()),
                    "chars": len(text),
                },
            )

        def log_message(self, format, *args):
            return

    return ReceiverHandler


def main():
    args = parse_args()
    output_file = Path(args.output)
    handler_cls = build_handler(output_file, args.token)
    server = HTTPServer((args.host, args.port), handler_cls)

    print(f"Receiver listening on http://{args.host}:{args.port}")
    print(f"Messages will be saved to: {output_file.resolve()}")
    if args.token:
        print("Token check: enabled")
    else:
        print("Token check: disabled")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nReceiver stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
