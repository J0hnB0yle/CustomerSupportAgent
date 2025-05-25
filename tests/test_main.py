import unittest
from src.customer_support_agent.main import get_claude_response

class TestClaudeAgent(unittest.TestCase):

    def test_get_claude_response_success(self):
        """
        Test successful response from get_claude_response with a valid API key and query.
        """
        api_key = "DUMMY_API_KEY"
        query = "Hello"
        expected_response = "This is a mock response from Claude."
        actual_response = get_claude_response(api_key, query)
        self.assertEqual(actual_response, expected_response)

    def test_get_claude_response_api_key_error(self):
        """
        Test error response when the placeholder API key is used.
        """
        api_key = "YOUR_CLAUDE_API_KEY_HERE"
        query = "Hello"
        expected_response = "Error: API key not configured."
        actual_response = get_claude_response(api_key, query)
        self.assertEqual(actual_response, expected_response)

    def test_get_claude_response_empty_query_error(self):
        """
        Test error response when an empty query is provided.
        """
        api_key = "DUMMY_API_KEY"
        query = ""
        expected_response = "Error: Query cannot be empty."
        actual_response = get_claude_response(api_key, query)
        self.assertEqual(actual_response, expected_response)

    def test_get_claude_response_whitespace_query_error(self):
        """
        Test error response when a whitespace-only query is provided.
        """
        api_key = "DUMMY_API_KEY"
        query = "   "
        expected_response = "Error: Query cannot be empty."
        actual_response = get_claude_response(api_key, query)
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
