#Exercice
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        print(f"{self.phone_number} a appelé {other_phone.phone_number}")
        self.call_history += [other_phone.phone_number]
        other_phone.call_history += [self.phone_number]

    def show_call_history(self):
        print(f"Historique d'appels de {self.phone_number} : {self.call_history}")

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages += [message]
        other_phone.messages += [message]
        print(f"Message envoyé de {self.phone_number} à {other_phone.phone_number} : {content}")

    def show_outgoing_messages(self):
        print(f"\nMessages envoyés par {self.phone_number} :")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"  À {msg['to']} : {msg['content']}")

    def show_incoming_messages(self):
        print(f"\nMessages reçus par {self.phone_number} :")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"  De {msg['from']} : {msg['content']}")

    def show_messages_from(self, other_phone):
        print(f"\nMessages de {other_phone.phone_number} à {self.phone_number} :")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number:
                print(f"  {msg['content']}")

phone1 = Phone("123-456-7890")
phone2 = Phone("098-765-4321")
phone3 = Phone("555-555-5555")

phone1.call(phone2)
phone2.call(phone3)
phone1.call(phone3)

phone1.show_call_history()
phone2.show_call_history()

phone1.send_message(phone2, "Salut, ça va?")
phone2.send_message(phone1, "Oui, et toi?")
phone3.send_message(phone1, "Bonjour!")

phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone2)