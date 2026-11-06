# Authentication and token verification

Read when changing authentication, session validation or token verification.
Use the project's established scheme and supported library/provider; this topic
does not select JWT, OAuth, a provider, token lifetime or native skill.

## Boundary and ownership

Identify the server-side verifier and the trusted configuration it consumes.
Framework dependencies, middleware and guards connect that verifier to actual
entry points; parsing a credential or decoding its payload does not establish
identity. Construct the authenticated principal only after required checks pass.
Use established cryptographic implementations and check the installed library's
validation options rather than writing signing or verification primitives.

Pass the necessary principal to the application operation, which still enforces
action, object and tenant authorization. Preserve the selected transport's
cookie/CSRF, credential-storage and redaction rules. Verification failures must
not expose raw credentials or become a successful identity through a fallback.

## JWT acceptance contract

When JWT is selected, define its purpose and validation policy before accepting
tokens. Separate access, identity and refresh purposes through the selected
profile's mutually exclusive rules; verify `typ` when that profile uses it.
Bind verification keys to their trusted issuer; validate issuer/subject claims
under the selected profile, including their presence where required.
Require and check `aud` when the issuer serves multiple recipients; reject tokens
addressed elsewhere. A header or claim cannot define its own trust policy.
[JWT BCP, sections 3.8-3.12](https://www.rfc-editor.org/rfc/rfc8725.html#section-3.8).

Configure the application's allowed algorithms and key/algorithm pairing in the
verifier. For signed credentials, require a valid signature/MAC; reject malformed
tokens, disallowed algorithms, `none`, wrong keys and invalid signatures. Decoding
the payload is insufficient. Use the library's complete JOSE validation path,
including required header handling, rather than checking only selected fields.
[JWS validation](https://www.rfc-editor.org/rfc/rfc7515.html#section-5.2).
For encrypted/nested JWTs, validate every required cryptographic layer; successful
decryption cannot waive an inner signature check.
[JWT cryptographic validation](https://www.rfc-editor.org/rfc/rfc8725.html#section-3.3).

Declare required claims, their types and expected values explicitly. RFC 7519
does not require every registered claim for every application. A library's
validate-if-present option does not establish required presence. Check `exp` and
`nbf` when present, and require them where the selected profile does. NumericDate
values use seconds since the Unix epoch; reject invalid types rather than coercing
strings or treating zero as absence. With zero leeway, reject at `now >= exp` and
before `nbf`; configure any small clock-skew allowance deliberately. `iat` alone
is not expiry. Keep audience string/list handling consistent with the contract.
[Claims and time semantics](https://www.rfc-editor.org/rfc/rfc7519.html#section-4).

## Trusted keys and availability

Use configured issuer metadata/key sources. Treat `kid` only as an untrusted lookup
hint within that trust boundary, never as a path or query to execute. Token-supplied
`jku`, `x5u`, issuer URLs or embedded keys cannot authorize arbitrary fetches or
introduce a trusted key. Apply the selected client's destination/TLS controls.
[Untrusted lookup inputs](https://www.rfc-editor.org/rfc/rfc8725.html#section-3.10).

For remote key discovery, bound fetches and refresh attempts, including unknown-key
requests. Define cache lifetime, rotation overlap and outage behavior for the
selected provider. A still-permitted cached key may verify a token; a failed lookup
must not disable verification or revive a retired key. These capacity and failure
rules are this library's policy, not a universal cache duration or `kid` requirement.

## Session, revocation and refresh conditions

Define logout, revocation and replay behavior where the chosen protocol needs it.
A valid signature does not establish current session or permission state. Reuse
the provider's mechanisms and keep verification caches within their validity rules;
do not add a revocation database to every JWT use merely because it is possible.

For OAuth public clients receiving refresh tokens, the authorization server must
use sender-constrained tokens or rotation with replay detection. Follow that
provider contract, including invalidation and concurrent refresh behavior. Rotation
must not leave an old token independently reusable; handle detected reuse under
the selected grant's revocation policy. Token lifetimes follow the actual protocol
and risk requirements, not a shared numeric default.
[OAuth refresh protection](https://www.rfc-editor.org/rfc/rfc9700.html#section-4.14).

## Focused verification

Apply [shared verification](../verification.md) to the changed boundary, using the
actual library/configuration and a controlled clock when time matters. Select
applicable cases; do not substitute mocked identity for verifier evidence.

| Scenario | Required observation |
| --- | --- |
| Valid credential | Intended principal established; operation authorization still applies |
| Malformed, tampered or algorithm/key mismatch | Rejected before protected effects |
| Wrong purpose, issuer, subject or audience | Rejected under the configured application contract |
| Missing required claim or invalid claim type | Rejected even if payload decoding succeeds |
| Expiry/not-before boundary and configured skew | Exact accepted/rejected time boundaries observed |
| Untrusted lookup destination or unknown key | No unauthorized fetch or verification bypass |
| Rotation, cache expiry or provider outage | Only permitted verification paths remain usable |
| Revocation or refresh reuse, when applicable | The selected protocol's refusal/invalidation occurs |

The RFC contracts above were reviewed on 2026-11-06. Source inspection and artifact
checks do not prove a consumer's authentication behavior; executable changes need
their relevant positive and negative checks with recorded library versions.
