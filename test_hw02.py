import pytest
import hw02_main  # Import the module here

# Part 1
# ===========
def test_1_1_read_two_ints(capsys, monkeypatch):

    # Create a list of input values
    user_inputs = iter(["10", "15"])
    exp1a, exp1b = 10, 15
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))

        #   import hw01_main  # Import the module here

        ret1a, ret1b = hw02_main.read_two_ints()
        captured = capsys.readouterr()

        assert ret1a == exp1a, "Tip: Did you cast the x value to int?"
        assert ret1b == exp1b, "Tip: Did you cast the y value to int?"

def test_1_2_read_two_ints(capsys, monkeypatch):

    # Create a list of input values
    user_inputs = iter(["8", "2"])
    exp1a, exp1b = 8, 2
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))

        #   import hw01_main  # Import the module here

        ret1a, ret1b = hw02_main.read_two_ints()
        captured = capsys.readouterr()

        assert ret1a == exp1a, "Tip: Did you cast the x value to int?"
        assert ret1b == exp1b, "Tip: Did you cast the y value to int?"

def test_2_1_compute_multadd(capsys, monkeypatch):

    # Create a list of input values
    user_inputs = iter(["10", "15"])
    exp2 = 6.0
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))

        #   import hw01_main  # Import the module here

        ret2 = hw02_main.compute_multadd(10, 15)
        captured = capsys.readouterr()

        assert ret2 == exp2, "Tip: Is the expression correct (value and type)?"
        assert "mult result: 150" in captured.out, "Tip: is your mult printout correctly formatted (case, spaces)?"
        assert "add result: 25" in captured.out, "Tip: is your add printout correctly formatted (case, spaces)?"

def test_2_2_compute_multadd(capsys, monkeypatch):

    # Create a list of input values
    user_inputs = iter(["8", "2"])
    exp2 = 1.6
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))

        #   import hw01_main  # Import the module here

        ret2 = hw02_main.compute_multadd(8, 2)
        captured = capsys.readouterr()

        assert ret2 == exp2, "Tip: Is the expression correct (value and type)?"
        assert "mult result: 16" in captured.out, "Tip: is your mult printout correctly formatted (case, spaces)?"
        assert "add result: 10" in captured.out, "Tip: is your add printout correctly formatted (case, spaces)?"


def test_3_1_print_fancy(capsys):
    hw02_main.print_fancy(10, 15, 6.0)
    captured = capsys.readouterr()
    assert 16*"*" in captured.out, "Tip: does your fancy printout begin with 16 asteriscs '*' (check spaces)?"
    assert "RESULTS:" in captured.out, "Tip: does your fancy printout have the string 'RESULTS:' (check spaces, colon)?"
    assert f"first number: {10}" in captured.out, "Tip: does your fancy printout print the first number line (check spaces, colon)?"
    assert f"second number: {15}" in captured.out, "Tip: does your fancy printout print the second number line (check spaces, colon)?"
    assert f"multadd result: {6.0}" in captured.out, "Tip: does your fancy printout print the multadd result line (check spaces, colon)?"
    assert 16*"=" in captured.out, "Tip: does your fancy printout end with 16 equal signs '=' (check spaces)?"

def test_3_2_print_fancy(capsys):
    hw02_main.print_fancy(8, 2, 1.6)
    captured = capsys.readouterr()
    assert 16*"*" in captured.out, "Tip: does your fancy printout begin with 16 asteriscs '*' (check spaces)?"
    assert "RESULTS:" in captured.out, "Tip: does your fancy printout have the string 'RESULTS:' (check spaces, colon)?"
    assert f"first number: {8}" in captured.out, "Tip: does your fancy printout print the first number line (check spaces, colon)?"
    assert f"second number: {2}" in captured.out, "Tip: does your fancy printout print the second number line (check spaces, colon)?"
    assert f"multadd result: {1.6}" in captured.out, "Tip: does your fancy printout print the multadd result line (check spaces, colon)?"
    assert 16*"=" in captured.out, "Tip: does your fancy printout end with 16 equal signs '=' (check spaces)?"
