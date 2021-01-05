from django.test import TestCase
import datetime
from django.urls import reverse
from django.utils import timezone
from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently returns False for a question in the future"""
        future_question = Question(pub_date=timezone.now()+datetime.timedelta(days=30))
        #was it published recently?
        future_question.was_published_recently()
        self.assertIs(future_question.was_published_recently(),False)
        
    def test_was_published_recently_with_old_question(self):
        """was_published_recently returns False for a question older than 1 day"""
        old_question = Question(pub_date=timezone.now()+datetime.timedelta(days=1,seconds=1))
        self.assertIs(old_question.was_published_recently(),False)
        
    def test_was_published_recently_with_recent_question(self):
        """was_published_recently returns True for a question within 1 day"""
        recent_question = Question(pub_date=timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59))
        self.assertIs(recent_question.was_published_recently(),True)

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    no_polls_text = "No polls are available"

    def test_no_questions(self):
        """if no appropriate questions exist, show a message"""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.no_polls_text)
    
    def test_past_questions(self):
        """questions with a pub_date in the past are displayed on the index page"""
        create_question("do we show past questions?", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: do we show past questions?>'])
    
    def test_future_questions(self):
        """questions in the future are not shown"""
        create_question("do we show future questions?",days=1)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, self.no_polls_text)
        
    def test_future_and_past_questions(self):
        """even if both future and past questions exist, only past questinos show"""
        create_question("do we show past questions?", days=-30)
        create_question("do we show future questions?", days=1)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: do we show past questions?>'])
    
    def test_two_past_questions(self):
        """two past questions show well"""
        create_question("do we show past questions?", days=-30)
        create_question("do we show older past questions?", days=-300)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: do we show past questions?>','<Question: do we show older past questions?>'])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)