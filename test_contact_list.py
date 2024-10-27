import unittest
from unittest.mock import MagicMock
from contact_list import ContactList

class TestContactList(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.contact_list = ContactList(db=self.mock_db)
        self.contact_list = ContactList()

    def test_add_contact(self):
        contact = self.contact_list.add_contact("Alice", "123456")
        self.assertEqual(self.contact_list.get_contacts(), [{"id": 1, "name": "Alice", "phone": "123456"}])
        self.mock_db.save.assert_called_once_with(contact)
        print("Test 'test_add_contact' passed.")

    def test_add_contact_empty_name(self):
        with self.assertRaises(ValueError):
            self.contact_list.add_contact("", "123456")
        self.mock_db.save.assert_not_called()
        print("Test 'test_add_contact_empty_name' passed.")

    def test_update_contact(self):
        self.contact_list.add_contact("Alice", "123456")
        updated_contact = self.contact_list.update_contact(1, name="Alicia", phone="654321")
        self.assertEqual(updated_contact, {"id": 1, "name": "Alicia", "phone": "654321"})
        print("Test 'test_update_contact' passed.")

    def test_delete_contact(self):
        self.contact_list.add_contact("Alice", "123456")
        self.contact_list.delete_contact(1)
        self.assertEqual(self.contact_list.get_contacts(), [])
        print("Test 'test_delete_contact' passed.")

    def test_delete_nonexistent_contact(self):
        with self.assertRaises(ValueError):
            self.contact_list.delete_contact(99)
        print("Test 'test_delete_nonexistent_contact' passed.")

if __name__ == "__main__":
    unittest.main()
