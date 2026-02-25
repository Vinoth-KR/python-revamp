import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A survey about language preferences, fixture available to all tests."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)


def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('Kannada')

    assert 'Kannada' in language_survey.responses


def test_store_three_responses(language_survey):
    """Test that three individual reponses are stored properly."""
    responses = ['Kannada', 'Hindi', 'English']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
