import pytest


def test_cant_run_execute_on_system_tasks(rollback_registry):
    registry = rollback_registry
    task = registry.System.Tasks.insert(code="abc")
    with pytest.raises(RuntimeError) as err:
        task.execute()
    assert "Creating task directly from System.Tasks class is Forbidden" in str(
        err
    )
