# testworkflow
Testing some Github Action workflows

## Repo Function

This repo has 2 text files and 2 scripts

Edits in `submit.txt` are appended to the end of `base.txt` if and only if
each line in `submit.txt` is able to be cast to an integer.

On a pull request with a valid edit to `submit.txt`, the additions will be added to `base.txt`
and `submit.txt` will be reset to blank via `script.py`. Then github actions will run `test.py`
to ensure that the changes completed successfully. If sucessful, github actions will then
commit the updated files, push, and automerge into main.

Edits to files other than `submit.txt` should result in standard github behavior (no build
and no auto-merge).

