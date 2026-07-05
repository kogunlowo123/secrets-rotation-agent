"""Secrets Rotation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_rotate_secret():
    """Test Rotate a secret according to its rotation policy."""
    tools = AgentTools()
    result = await tools.rotate_secret(secret_id="test", rotation_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_scan_for_leaks():
    """Test Scan repositories and logs for exposed secrets."""
    tools = AgentTools()
    result = await tools.scan_for_leaks(scan_target="test", scan_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_audit_secret_age():
    """Test Audit secrets approaching or exceeding rotation deadline."""
    tools = AgentTools()
    result = await tools.audit_secret_age(max_age_days=1, severity="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_emergency_rotate():
    """Test Emergency rotation of potentially compromised credentials."""
    tools = AgentTools()
    result = await tools.emergency_rotate(secret_id="test", reason="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.secrets_rotation_agent_agent import SecretsRotationAgentAgent
    agent = SecretsRotationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
