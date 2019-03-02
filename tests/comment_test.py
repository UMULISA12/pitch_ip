import unittest
from app.models import Comment, User

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_Alice = User(username='alice', password='12345', email='umuli@gmail.com')
        self.new_comment = Comment(title='Test',comment='Test Comment',user=self.user_Alice)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.title, 'Test')
        self.assertEquals(self.new_comment.comment, 'Test Comment'),
        self.assertEquals(self.new_comment.user, self.user_Alice)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)