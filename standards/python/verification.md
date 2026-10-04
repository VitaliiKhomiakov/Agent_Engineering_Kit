# Python: verification, exposed boundaries, and compatibility

Read when choosing Python checks or changing security-sensitive boundaries,
performance, interpreter versions, or dependencies. Return to the
[Python entry](../python.md). The shared
[verification policy](../verification.md) owns testing/review scope.

## Match checks to changed behavior

- Run the existing affected tests and required project checks. Verify observable
  results, meaningful error cases, and effects; avoid tests asserting a private
  helper layout or the presence of a pattern-named class. A documentation-only
  edit does not require inventing a test suite.
- For state transitions, cover permitted incomplete states, successful transitions,
  rejection without partial mutation/effects, and calls that bypass the HTTP
  boundary. For parsers, distinguish absent/empty/false values when the contract
  requires it; static typing does not prove input validation.
- For async changes, verify success, meaningful failures, and any affected timeout,
  cancellation, or cleanup behavior. Coordinate tests with events/barriers and
  bound waits; arbitrary sleeps are poor evidence of ordering. Use the existing
  async test setup or stdlib `IsolatedAsyncioTestCase` rather than adding a runner
  solely for an example. Debug mode can reveal unawaited coroutines and leaked
  tasks; passing one run is not proof of race freedom.
- Test owned behavior with typed doubles at real seams. Use an actual adapter
  or integration check when the risk is query, transaction, serialization, or
  dependency compatibility; mocks cannot establish those guarantees. Do not
  perform real external side effects just to exercise an internal branch.
- Run the agreed formatter/linter and pinned analyzer for changed code and its
  affected contracts, including relevant tests. See the [typing baseline](typing-contracts.md).
  A successful type check, compilation, and a successful runtime test establish
  different things; report the interpreter and checked scope accurately.
- When packaging/exports change, verify imports, resource inclusion, and entry
  points from the installed artifact outside the source checkout. When upgrading
  Python, check the supported runtime matrix required by the project; parsing a
  file with an older grammar is not execution on that interpreter.

## Security and operational behavior when exposed

These checks apply to the boundary the task touches, not every Python edit.

- Do not deserialize untrusted `pickle` data or execute untrusted text with
  `eval`/`exec`. Choose a data format and explicit schema for external input, with
  limits on body size and expensive parsing where required. Encoding/JSON alone
  does not establish trust or authorize an operation.
- Use subprocess argument sequences without a shell when sufficient; validate
  allowed executable/options and handle option injection, timeout, exit status,
  and output limits. `shell=False` alone does not make arbitrary commands safe;
  Windows batch-file behavior needs its documented platform-specific treatment.
- For untrusted paths/archives, constrain access to the intended root and account
  for traversal, symlinks, and races. Use appropriate secure file/directory APIs;
  a string-prefix check is not containment. Keep secrets and sensitive payloads
  out of logs and public exceptions. Preserve installed-library TLS/auth defaults
  unless the required deployment contract explicitly changes them.
- Give caches, queues, workers, and clients bounds and a shutdown owner when they
  exist. Measure operation latency/errors and resource pressure where needed;
  logging every input or retry can expose secrets and amplify load.

## Measure before optimizing

Profile a representative workload before changing execution model, data
structures, caching, slots, or serialization. `cProfile` helps attribute execution
time; `tracemalloc` attributes traced Python allocations, not all native/process
memory. Use timing/benchmark tools for a focused hypothesis and realistic
integration measurements for end-to-end latency. Consider repeated I/O and query
volume before micro-optimizing Python syntax. Preserve correctness, memory bounds,
and cancellation while comparing results; no universal speedup follows from
async, generators, threads, or a new interpreter build.

## Version-sensitive decisions

Preserve the project's supported minimum and actual deployed interpreter.
Check release notes and the installed dependency's compatibility for the affected
feature; do not upgrade merely to adopt the latest example syntax.

| Feature or change | Applicability and migration check |
| --- | --- |
| `TaskGroup`, `asyncio.timeout`, exception groups / `except*` | Python 3.11+; adopting them changes failure/cancellation contracts, not just syntax |
| Type parameter and `type Alias = ...` syntax | Python 3.12+; use older supported forms where needed; `typing_extensions` cannot backport grammar |
| `TypeIs` | In `typing` from 3.13; a compatible `typing_extensions` can provide it earlier if needed; incorrect narrowing predicates can make a checker trust false claims |
| Free-threaded CPython | Optional from 3.13, officially supported in 3.14; still check extensions, actual GIL state, synchronization, memory, and workload results |
| Deferred annotation evaluation | Python 3.14 changes runtime evaluation; libraries/decorators that inspect annotations need compatibility checks, including `TYPE_CHECKING` imports and existing future imports |
| Process start methods | In 3.14 the default changes from `fork` to `forkserver` on Unix other than macOS; check picklability, import-safe startup, resources, and the actual target OS |

The [Python version status](https://devguide.python.org/versions/) is a moving
source; check it when selecting/upgrading a runtime. Research dated 2026-09-21
found 3.14 in bugfix support and 3.15 in prerelease. This is not a universal
minimum or an instruction to adopt a prerelease. Stage examples use 3.11-compatible
syntax and were executed only on the interpreter recorded in the
[practice plan](../../docs/plans/2026-09-21-engineering-practices.md).

Sources: [unittest](https://docs.python.org/3.11/library/unittest.html),
[pickle](https://docs.python.org/3.11/library/pickle.html),
[subprocess security](https://docs.python.org/3.11/library/subprocess.html#security-considerations),
[profiling](https://docs.python.org/3.11/library/profile.html),
[traced allocations](https://docs.python.org/3.11/library/tracemalloc.html),
[PEP 695](https://peps.python.org/pep-0695/),
[PEP 742](https://peps.python.org/pep-0742/),
[3.14 changes](https://docs.python.org/3.14/whatsnew/3.14.html).
