# Go example: publication invariant

Read when the example clarifies the linked rule; it is not required on every Go task.
Return to [contracts](../contracts.md).

For example, an empty title is permitted while drafting but not when publishing.
This original example defines publication as a single transition; choose retry
and idempotency semantics from the real operation's contract.

```go
package practices

import (
	"errors"
	"strings"
)

type documentStatus uint8

const (
	draft documentStatus = iota
	published
)

var ErrEmptyTitle = errors.New("empty title")
var ErrInvalidTransition = errors.New("invalid document transition")

type Document struct {
	title  string
	status documentStatus
}

func NewDraft(title string) Document {
	return Document{title: title, status: draft}
}

func (d *Document) Publish() error {
	if d.status != draft {
		return ErrInvalidTransition
	}

	if strings.TrimSpace(d.title) == "" {
		return ErrEmptyTitle
	}

	d.status = published
	return nil
}
```

The zero value is an empty draft, not a publishable document. Failure leaves
state unchanged. Callers provide a non-nil receiver and own synchronization;
this method alone cannot prevent two requests updating the same database row.
Do not add arbitrary setters that bypass the transition rules.

This is an original standard-library-only example. Save its Go block as a
`.go` file in package `practices`; it can be compiled with the other Go examples
in one module. The recorded `go test -race` and `go vet` run used a temporary
module whose tests are not retained here
([practice record](../../../docs/plans/2026-09-21-engineering-practices.md#k01-result-and-verification));
reproduction needs a new module and tests.
