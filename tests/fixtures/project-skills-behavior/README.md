# Project-skill behavioral inputs

These fixed PS-05 inputs extend the [design fixture](../project-skills/ARCHITECTURE.md).
They are not a product, installer, autonomous evaluator or client configuration.
The [dated observation record](../../../docs/research/2026-10-11-project-skills-behavior.md)
owns actual prompts, client/settings, isolation, outcomes and evidence limits.

Prepare a fresh project from the source root with Python 3.12:

```sh
python3 tests/fixtures/project-skills-behavior/prepare.py /tmp/aek-example implementation candidate
```

The three arguments are a new empty target, operation (`design`, `implementation`,
`review`, `unrelated` or `small-fix`) and condition (`candidate` or `control`).
Candidate installs all three native task entries; control omits project-workflows.
Both retain identical general/technology rules, local exceptions, product inputs
and task prompts. Link adaptation accounts for the omitted optional guide.
The helper uses the existing fixed adoption builder; it does not run a client.
The common AGENTS route names the observed installed Superpowers 6.4.2 path.
On another host, identify its actual installed source and adapt that route equally
in both conditions; do not assume this absolute path or native plugin discovery.

The design task retains the existing HTTP cancellation design request. Implementation
is a separately accepted domain-only operation; unchanged HTTP integration is a later
task. Python 3.12 and the standard library execute its acceptance checks. Its agreed
strict analyzer is mypy 2.1.0, provided outside the target and source. No FastAPI or
Pydantic runtime/dependency installation is implied by these domain checks.

```sh
cd /tmp/aek-example
python3 -B acceptance.py
python3 -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.12 --explicit-package-bases --cache-dir /tmp/aek-example-mypy app/domain.py acceptance.py
```

Before implementation the three acceptance tests fail because cancel is missing.
The review seed adds cancel but returns stock on every call: two tests fail and
the missing-ID case passes. A correct implementation must pass all three, retaining
identity, frozen values, missing-ID behavior and stock under repeated/concurrent
cancellation. The review oracle expects that defect and no finding against accepted
exception E1 (bounded process-local storage and one Lock). Review-only changes no files.

The small-fix task rejects Boolean quantities without adding cancellation or a new
design. The unrelated task replaces one README typo. Prompts forbid delegation,
Git writes, tool installation and configuration changes. Missing optional skills
are not permission to install them. Native observations require their own bounded,
authorized client environment; running this helper proves no skill activation.
