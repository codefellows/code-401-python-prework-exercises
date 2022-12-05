# 401 Python Prework Exercises

## Welcome! Let's do some Python

- Fork this Repl
- Run supplied tests by clicking `Run` button at top of screen.
- Notice that tests have run but are all `skipped`.
- Open `tests/test_functions.py`
- Comment out line above `hello_test` function
  - To comment out a line add `#` to beginning of line
  - E.g. `# @pytest.mark.skip("comment out to enable test")`
- Click `Run` button again.
  - See the test fail.
- Let's analyze the test code.
  - `test_hello` function is saying:
    - store the return value of invoking `hello` function in local variable named `actual`.
      - In other words, `actual` holds the result of `actually` running the function we are testing.
    - Then store the expected result in local variable named `expected`.
    - The last line makes an assertion that the actual and expected results match using the `assert` statement.
    - If the assertion is `falsy` then the test fails.
- Your job is to make the test pass.
- Open `exercises/functions.py`
- Make `hello` function pass by returning the the expected result.
- Test passing?
  - If not then modify exercise code and re-run test until it passes.
- If so, congratulations!
  - Follow same process for remaining tests in `tests/test_functions.py`
- When you're all done with `test_functions.py` then move on to the remaining files in `tests` folder in the order you like.
