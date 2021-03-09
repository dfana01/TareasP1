import unittest
from main import Mail, MailerHandler, get_epoch

MAX_PRIORITY_MAIL = Mail(get_epoch(days=1))


class MailerHandlerTest(unittest.TestCase):
    def test_deque(self):
        handler = MailerHandler()
        handler.queue(MAX_PRIORITY_MAIL)
        handler.queue(Mail(get_epoch(days=5)))
        handler.queue(Mail(get_epoch(days=4)))
        handler.queue(Mail(get_epoch(days=6)))
        handler.queue(Mail(get_epoch(days=4)))
        handler.queue(Mail(get_epoch(days=5)))
        self.assertEqual(handler.dequeue(), MAX_PRIORITY_MAIL)


if __name__ == '__main__':
    unittest.main()
