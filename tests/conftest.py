"""Test configuration for Secrets Rotation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "secrets-rotation-agent", "category": "DevOps & Platform Engineering"}
