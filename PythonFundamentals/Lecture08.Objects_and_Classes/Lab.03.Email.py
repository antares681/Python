class Email():
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails_repository = []

command = input()

while not command == 'Stop':
    s, r, c = command.split()
    current_email = Email(s, r, c)
    emails_repository.append(current_email)

    command = input()

indexes_emails_to_send = [int(indexes) for indexes in input().split(', ')]

for index_to_send in indexes_emails_to_send:
    email = emails_repository[index_to_send]
    email.send()

for email in emails_repository:
    print(email.get_info())

