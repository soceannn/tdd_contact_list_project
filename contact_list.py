class ContactList:
    def __init__(self, db=None):
        self.contacts = []
        self.current_id = 1
        self.db = db
    def __init__(self):
        self.contacts = []
        self.current_id = 1

    def add_contact(self, name, phone):
        if not name or not phone:
            raise ValueError("Name and phone number cannot be empty")
        contact = {'id': self.current_id, 'name': name, 'phone': phone}
        self.contacts.append(contact)

        if self.db:
            self.db.save(contact)

        self.current_id += 1

        self.current_id += 1
        return contact

    def get_contacts(self):
        return self.contacts

    def update_contact(self, contact_id, name=None, phone=None):
        contact = next((c for c in self.contacts if c['id'] == contact_id), None)
        if not contact:
            raise ValueError("Contact not found")
        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        return contact

    def delete_contact(self, contact_id):
        contact = next((c for c in self.contacts if c['id'] == contact_id), None)
        if not contact:
            raise ValueError("Contact not found")
        self.contacts.remove(contact)
