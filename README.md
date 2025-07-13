# Pytest Testiny Integration Example

This projects shows how to create JUnit-style XML reports with pytest and how to report results to Testiny.

Run tests locally with:

```
python -m venv venv
source venv/bin/activate
pytest --junitxml=results/report.xml
```

In `.github/workflows/pytest.yml` you'll see how to run your tests with pytest with GitHub actions, generate a JUnit report and upload results to Testiny.