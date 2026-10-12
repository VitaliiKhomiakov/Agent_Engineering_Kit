# Disposable update and recovery exercise — 2026-10-13

## Scope and evidence boundary

The [migration procedure](../../MIGRATION.md#repeat-and-update) is a manual
instruction contract. This exercise applies explicitly selected decisions to
temporary files; it does not test a general installer, automatic merge policy,
client activation or an agent's ability to choose the decisions unaided.
The [follow-up task](../plans/2026-10-13-review-follow-up.md) owns progress.

No files in the existing AEK_TEST adoption or its historical evidence were changed.
No application stack or paid model run was started. The targets here are small
instruction fixtures, not replacements for the earlier adopted project's evidence.

Raw artifacts from this run:
`/tmp/aek-followup-20261013-wr1d79ho/update-recovery-probe.py`,
`update-recovery-results.json`, and the sibling `update-recovery/` directory.
The script executes the decisions listed below using ordinary file operations and
`git merge-file --stdout`; it is not shipped as adoption automation. Temporary
evidence can expire. The fixture definitions and observed outcomes below are
retained for reproduction, not a durable accepted base for any real project.
Execution environment: Python 3.12.3 and Git 2.43.0. Probe script SHA-256:
`59d9a494f07ed189dcf16a8a8d13570a63dbb9ab2f44f3811aedc1750a3cb87d`.

## Fixtures and observed decisions

The exact B fixture is the following UTF-8 text, ending in a newline:

```md
# Project

Runtime: Python 3.11

## Local policy

Checks: smoke
```

C changes only `Checks: smoke` to `Checks: smoke and domain` unless a case says
otherwise. N changes only `Runtime: Python 3.11` to `Runtime: Python 3.12`.
Each case also has `unrelated.txt` containing `Existing unrelated content` plus
a newline. That sentinel remained byte-identical in every case. The version
change is synthetic fixture text; it authorizes no actual runtime upgrade.

| Case | Inputs and selected action | Executed outcome |
| --- | --- | --- |
| Unchanged | B = C = N; do not write | C's bytes and nanosecond mtime retained |
| Local only | N = B; C adds the domain check | Local edit and accepted B retained |
| Source only and repeat | C = B; apply N after rechecking C, then compare the identical next candidate | First write contains N; repeat performs no write and retains mtime |
| Independent edits | C changes checks; N changes runtime | `git merge-file --stdout C.md B.md N.md` exits 0; prepared output contains both changes; C remains unchanged during preparation |
| Overlapping edits | C changes runtime to Python 3.10; N changes it to Python 3.12 | The same merge command exits 1 with conflict markers; dependent write is withheld and C retains 3.10 |
| Missing base | B contents unavailable; C and N differ | C retained; no three-way merge claimed, reconciliation remains unresolved |
| Interrupted operation | See the recovery fixture below | Safe original restored; newer edits and untouched files retained; accepted B retained and outcome remains partial |

Seven scenarios completed with assertions on actual bytes, merge exit codes and
no-write mtimes. The results JSON records SHA-256 identities of all final fixture
files. Assertions support these concrete outcomes; they do not prove semantic
conflict detection across arbitrary documents or repeatability of an autonomous
adoption workflow.

## Recovery fixture

Before the simulated operation, `restore.md` and `newer.md` both contain B.
Their originals and the adoption record are copied to a sibling directory outside
the simulated discovery root. `created.md` is initially absent. The record is
`accepted=B\nstatus=verified\n`.

The interrupted operation writes N to both existing files and
`operation-created\n` to `created.md`, retaining those exact written identities.
An intervening user then appends `New user edit\n` to `newer.md` and `created.md`.
The record is safely marked `accepted=B\nstatus=partial\n`.

Recovery compares each actual file with its recorded operation result:

- `restore.md` still equals the operation result and is restored byte-for-byte to B.
- `newer.md` differs; it retains N plus the newer user edit instead of being restored.
- `created.md` differs; it remains present with the newer edit instead of being deleted.
- Untouched `C.md` and the unrelated sentinel retain their original contents.
- Accepted B is retained, and the outcome stays partial with two unresolved paths.

This deliberately does not report full recovery or a successful adoption. A fresh
run can reproduce the decisions using the B/C/N text above in a new temporary
directory, recording originals outside it and comparing exact written bytes before
each restore/removal decision. Do not run the experiment in an existing target.

## Routing cross-check

The separate read-only command was also executed against the existing target:

```sh
python3 -B tools/check_model_routing.py --root /home/vitalii/Documents/Local_Projects/AEK_TEST/runs/specialized-agents-2026-10-13/project --default-role implementer
```

It exited 0: the saved coordinator/architect/reviewer pairs are
`gpt-6-astra / high`, implementer is `gpt-6.1-sol / high`, the direct delegation
graph is valid, and the native ceiling is 2. Worker defaults match implementer.
This newly checks agreement only; it neither reruns nor upgrades the historical
native smoke evidence. Provider model/effort telemetry, effective child permissions,
other-client support and general update/recovery behavior remain outside this evidence.
