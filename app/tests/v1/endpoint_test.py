"""Unit tests for search endpoints."""
import pytest

from tests.utils_test import inject_test_data

search_test_data = inject_test_data("tests/v1/_search_data.json")


class TestSearchBooks:
    """Unit tests for gutenberg book search api."""

    @pytest.mark.parametrize("valid_search", search_test_data["valid_search"])
    def test_search_with_filters(self, client, valid_search):
        """Test books search with filters."""

        response = client.get("/books/search", params=valid_search["filters"])
        data = response.json()

        assert response.status_code == 200
        assert valid_search["results"]["books"] in data["books"]
