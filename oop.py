class LoggerTerminal:

	def writer(self, message):
		print(f'Message for terminal: {message}')

class LoggerFile:

	def writer(self, message):
		with open('log.txt', 'w', encoding='utf-8') as f:
			f.write(message)


class Logger:
	def __init__(self, message):
		self.message = message

	def log_to_file(self, method):
		method.writer(self.message)

	def log_to_terminal(self, method):
		method.writer(self.message)


lg = Logger('404')
lg.log_to_terminal(LoggerTerminal())