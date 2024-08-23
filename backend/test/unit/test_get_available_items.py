
import pytest
from src.controllers.RecipeController import RecipeController

import unittest
import unittest.mock as mock
from unittest.mock import patch

""" 
    tests for the exam
"""

@pytest.fixture
def recipe_controller_returns_ok():
    mocked_dao = mock.MagicMock()
    mocked_dao.get_all.return_value = { "spiskummin": 0}
    recipe_controller_returns_ok = RecipeController(mocked_dao)
    return recipe_controller_returns_ok

@pytest.fixture
def recipe_controller_returns_not_included():
    mocked_dao = mock.MagicMock()
    mocked_dao.get_all.return_value = { "spiskummin": 0, "kanel": -1}
    recipe_controller_returns_ok = RecipeController(mocked_dao)
    return recipe_controller_returns_ok

@pytest.fixture
def recipe_controller_returns_exception():
    mocked_dao = mock.MagicMock()
    mocked_dao.get_all.return_value = Exception
    recipe_controller_returns_exception = RecipeController(mocked_dao)
    return recipe_controller_returns_exception


@pytest.mark.unit
def test_get_available_items_one_item(recipe_controller_returns_ok):
    """ Tests  """
    result = recipe_controller_returns_ok.get_available_items()
    assert result == { "spiskummin": 0}


@pytest.mark.unit
def test_get_available_items_one_item_missing(recipe_controller_returns_not_included):
    """ Tests  """
    result = recipe_controller_returns_not_included.get_available_items()
    assert result == { "spiskummin": 0}



@pytest.mark.unit
def test_get_user_by_email_exception(recipe_controller_returns_exception):
    """ Tests that Exception gets raised """
    with pytest.raises(TypeError):
        recipe_controller_returns_exception.get_available_items()
