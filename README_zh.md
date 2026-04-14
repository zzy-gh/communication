# Ubuntu 文本接收小工具

这是一个最简单的 Python 方案：

- `ubuntu_receiver.py` 跑在你的 Ubuntu 上，负责接收文本
- `send_to_ubuntu.py` 跑在你当前电脑上，负责把文本或剪贴板内容发过去

不依赖第三方库，Python 3 自带模块就能运行。

## 1. 在 Ubuntu 上启动接收服务

先把 `ubuntu_receiver.py` 放到 Ubuntu 上，然后运行：

```bash
python3 ubuntu_receiver.py --host 0.0.0.0 --port 8765 --output received_messages.txt --token mysecret
```

说明：

- `--host 0.0.0.0` 表示允许局域网内其他设备访问
- `--port 8765` 是监听端口，可以自己改
- `--output` 是保存收到文本的文件
- `--token` 是简单口令，建议保留

如果 Ubuntu 开了防火墙，需要放行端口，例如：

```bash
sudo ufw allow 8765
```

再确认 Ubuntu 的局域网 IP，例如：

```bash
hostname -I
```

假设它的 IP 是 `192.168.1.20`。

## 2. 从你的电脑发送文本

### 发送一段文字

```bash
python3 send_to_ubuntu.py --host 192.168.1.20 --port 8765 --token mysecret 你好 这是一段测试文本
```

### 把当前剪贴板内容直接发过去

```bash
python3 send_to_ubuntu.py --host 192.168.1.20 --port 8765 --token mysecret --clipboard
```

### 从管道发送

```bash
echo "这是我要传过去的内容" | python3 send_to_ubuntu.py --host 192.168.1.20 --port 8765 --token mysecret
```

## 3. 收到的内容在哪里

Ubuntu 端会把内容追加写入：

```text
received_messages.txt
```

每一条都会自动带时间戳。

## 4. 常见问题

### 连不上 Ubuntu

检查这几项：

- 两台设备是否在同一个网络里
- Ubuntu IP 是否正确
- 端口是否放行
- 接收端程序是否正在运行

### 想更方便地一键发送剪贴板

你可以在本机做一个别名，例如：

```bash
alias sendclip='python3 /你的路径/send_to_ubuntu.py --host 192.168.1.20 --port 8765 --token mysecret --clipboard'
```

之后每次复制完内容，只要执行：

```bash
sendclip
```

## 5. 安全提醒

这个程序适合你自己的局域网环境临时使用。

如果你要跨公网使用，建议至少再加上：

- HTTPS 或 SSH 隧道
- 更强的鉴权方式
- 只绑定内网地址
