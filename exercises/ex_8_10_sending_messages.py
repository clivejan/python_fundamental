def send_messages(messages, sent_massages):
	"""display messages in separate lines"""
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_massages.append(current_message)

msgs = ['Python is interesting.', 'Python is omnipresent.', 'Python is omnipotent.']
sent_msgs = []
send_messages(msgs, sent_msgs)
print(f"Origin: {msgs}")
print(f"Executed: {sent_msgs}")
