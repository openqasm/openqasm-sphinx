# Contributing to `openqasm-pygments`

Thanks for your interest in contributing!  Please make sure you follow our
[code of conduct](https://github.com/openqasm/openqasm-sphinx/blob/main/CODE_OF_CONDUCT.md)
at all times.

We're happy to accept help in a few forms:

- Bug reports (use [the bug tracker on GitHub](https://github.com/openqasm/openqasm-sphinx/issues)).
- Helping answer questions in [existing bug reports](https://github.com/openqasm/openqasm-sphinx/issues).
- Pull requests to fix bugs (but please file the bug report first).

For code changes, please make sure the code conforms to the code style of the
project (just run `tox -e black`), and that running the linter (`tox -e lint`)
doesn't show any errors.  All code changes should come with additional unit
tests if at all possible, and updated documentation if necessary.  Most
non-documentation changes will need a release note
(`reno new --edit <some identifier>'`) as well.

There are not currently any tests, mostly because I haven't looked into a good
way to test Sphinx domains yet.

When you make your first pull request, a bot will comment and ask you to sign
the contributor license agreement.  This certifies that you agree to license
your contributions under the [terms of the license in the repository
root](https://github.com/openqasm/openqasm-sphinx/blob/main/LICENSE), and
that we can distribute them for you.
