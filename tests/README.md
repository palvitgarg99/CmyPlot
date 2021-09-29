# Test

This file contains information about running tests.

## Running tests

To run tests locally on your machine, run

```bash
pip install -e .
pytest
```

## Notes

To test the callback functions, we must use the `__wrapped__` function. This simulates the Python decorator and ignores the extra steps used when shown in the UI

```python
def test_example_callback():
    param1 = 0
    param2 = 0
    expected = 2
    output = example_callback.__wrapped__(param1, param2)
    assert output == expected
```
