# Go: formatting and readability

Read when writing or meaningfully changing Go code, reviewing readability, or
choosing formatting conventions. Return to the [Go entry](../go.md).
Apply these conventions within the task; do not turn a local change into a
repository-wide rewrite. [Verification](verification.md#formatting-and-lint-adoption)
owns tooling adoption and checks; the [tooling example](examples/style-tooling.md)
owns the inactive configuration, version pins, and reproduction commands.

## Formatting and imports

- Require `gofmt`-compatible output. Prefer `goimports` for format-on-save and
  import maintenance, with reproducible output from the chosen CI toolchain.
- Put standard-library imports first and other imports in the following group.
  A separate project-local group is optional: configure the actual module prefix
  explicitly and keep editor and CI settings consistent.
- Avoid dot imports and aliases that add no clarity. Retain a justified exception,
  such as resolving a package-name collision, rather than mechanically removing it.

## Names and declarations

- Apply the shared [purpose and scope rules](../core.md#names-and-evolving-responsibilities)
  using Go's mixed-capitalization conventions: `userID`, `HTTPClient`, and `URL`.
  Avoid repeating a package name in its exported declarations.
- Short names such as `i`, `err`, and `ctx` are appropriate where their meaning is
  immediately clear. Use more descriptive names as scope or ambiguity grows.
- Use short, consistent receiver names reflecting the type, such as `c` for
  `Client`; avoid `this` and `self`. Receiver pointer/value semantics remain in
  [contracts](contracts.md).
- Keep related declarations together. Follow the existing
  [package/file boundaries](architecture.md#packages-and-files) and shared
  [size/cohesion policy](../core.md#size-and-cohesion). Do not impose one type per
  file, a universal declaration order, or another function/file-size limit.

## Readable flow and spacing

- Handle failures with guard clauses where they make the normal path easy to
  scan. Follow [simple control flow](../core.md#simple-control-flow); no additional
  nesting quota is introduced here.
- Separate successive meaningful steps inside a function with one blank line.
  Typical boundaries are input preparation/validation, application or domain
  work, and output construction. In a Gin handler, visually separate binding
  and validation, the application call with its error handling, and the success
  response when those steps are present.
- Keep an operation and its immediate error/result check together. Short setup
  used only by that operation belongs in the same group. After the completed
  group, use a blank line before the next independent step; this includes the
  transition from a rejecting guard to normal work.
- Consecutive guards validating the same input may stay together. Do not insert
  a blank line after every statement or closing brace, or mechanically before
  every `return`; a return may stay with the operation it completes. Avoid
  leading/trailing blank lines inside blocks and multiple blank lines between steps.
- Review this grouping separately from mechanical formatting. Formatter/linter
  success does not establish that meaningful steps are visually separated.
- Split unwieldy calls or composite literals, or name a complex predicate, when
  doing so clarifies intent. There is no fixed line-length gate and no automatic
  extraction solely to satisfy a line count. Preserve clear, cohesive code.

For example, this function-body excerpt from the
[dependency example](examples/dependencies.md) keeps reading and its error check
together, then separates the transformation that follows:

```go
text, err := source.ReadText(ctx)
if err != nil {
	return "", fmt.Errorf("prepare text: %w", err)
}

return normalize(text), nil
```

Use blank lines to expose the steps without adding comments that merely label
each operation.

## Comments and errors

- Document exported declarations and non-obvious contracts. Declaration comments
  identify the declaration and read as sentences; implementation comments explain
  reasons, constraints, or invariants. Avoid narrating the statement beneath them.
- Error strings normally begin lowercase and omit terminal punctuation; proper
  names and acronyms can require capitalization. Error wrapping, classification,
  and handling remain owned by [contracts](contracts.md#dependencies-and-errors); a formatter
  cannot establish those semantics.

## Compatibility and basis

Preserve wire names, intentionally stable exported APIs, error contracts, and
generated/vendor code. A style edit must not silently change a JSON tag, serialized
identifier, or public name. Handle a necessary compatibility change explicitly.

[Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) supplies the
Go-specific naming, comment, error-string, and readability basis.
[Effective Go formatting](https://go.dev/doc/effective_go#formatting) explains
mechanical formatting; Effective Go is historical core-language guidance, not a
complete guide to modern Go features. The scope, grouping, and adoption choices
above are local policy. The optional
[dated evidence](../../docs/research/2026-10-13-go-gin-gorm-style-evidence.md)
separates source review from executed checks.
