# Contributing

Issues and pull requests are welcome, especially test results: which model and frontend, the prompt you sent, and the output that broke a rule.

## Changing the prompt

1. Edit `system_prompt.txt` (or `meta_prompt.txt`).
2. Run `python3 scripts/check.py --fix` to copy `system_prompt.txt` into `a_little_more_human.json`.
3. Run `python3 scripts/check.py`; CI runs the same check on every pull request.

One rule change per pull request, with a sentence on the failure it fixes. Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `ci:`).
