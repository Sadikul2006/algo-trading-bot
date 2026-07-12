from telegram.notifier import TelegramNotifier

if __name__ == "__main__":
    notifier = TelegramNotifier()
    success = notifier.send_message("🤖 Hello from Algo Trading Bot! This is a test message.")
    print(f"Message sent: {success}")