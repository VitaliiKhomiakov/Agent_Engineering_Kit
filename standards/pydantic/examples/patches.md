# Pydantic example: partial input, validated replacement, public output

Read when absence, false/null, aliasing, update validation, and output visibility
interact. Return to [serialization](../serialization.md) and [lifecycle](../lifecycle.md).
Requires Python 3.11+ and the executed Pydantic **2.13.4** / core **2.46.4** pair;
the alias configuration used here was added in Pydantic 2.11.

These models belong to a configuration adapter: a stored snapshot, writable patch,
and public projection have different contracts. Enabling delivery requires a
channel. `deliveryChannel:null` clears it, and `enabled:false` is an explicit
change. Omitting a field leaves it unchanged. The server-owned token is never
writable through this patch and is absent from public output.

Save as `preferences.py`:

```python
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, Field, SecretStr, model_validator


Channel = Literal["email", "sms"]


class StoredPreferences(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    enabled: bool
    channel: Channel | None
    api_token: SecretStr

    @model_validator(mode="after")
    def check_delivery(self) -> Self:
        if self.enabled and self.channel is None:
            raise ValueError("enabled delivery requires a channel")
        return self


class PreferencesPatch(BaseModel):
    model_config = ConfigDict(
        strict=True, extra="forbid", frozen=True, validate_default=True,
        validate_by_alias=True, validate_by_name=False,
    )

    enabled: bool = False
    channel: Channel | None = Field(default=None, validation_alias="deliveryChannel")


class PublicPreferences(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    enabled: bool
    channel: Channel | None = Field(serialization_alias="deliveryChannel")


def apply_preferences_patch(
    current: StoredPreferences, raw: object
) -> StoredPreferences:
    patch = PreferencesPatch.model_validate(raw)
    supplied = patch.model_fields_set
    return StoredPreferences(
        enabled=patch.enabled if "enabled" in supplied else current.enabled,
        channel=patch.channel if "channel" in supplied else current.channel,
        api_token=current.api_token,
    )


def public_json(current: StoredPreferences) -> str:
    response = PublicPreferences(enabled=current.enabled, channel=current.channel)
    return response.model_dump_json(by_alias=True)
```

Defaults let patch fields be omitted; presence tracking prevents those defaults
from overwriting stored values. Explicit null is permitted only for the nullable
channel. Construction validates the complete replacement, including the existing
enabled state. Rejection leaves the prior snapshot intact. `model_copy(update=...)`
would not perform that validation, even on a frozen model.

For larger generic mappings, `exclude_unset=True` preserves the same presence
distinction; `exclude_none` and `exclude_defaults` do not. This small adapter
selects named fields directly, so no model dump becomes a business contract.
The public model deliberately projects fields instead of relying on SecretStr's
masking or a growing denylist. Model separation is justified by visibility and
writability, not merely by three folders.

Save as `test_preferences.py` beside the module:

```python
import json
import unittest

from pydantic import SecretStr, ValidationError

from preferences import (
    PreferencesPatch, PublicPreferences, StoredPreferences,
    apply_preferences_patch, public_json,
)


def stored() -> StoredPreferences:
    return StoredPreferences(
        enabled=True, channel="email", api_token=SecretStr("fixture-private-token")
    )


class PreferencesTests(unittest.TestCase):
    def test_omission_preserves_values_despite_patch_defaults(self) -> None:
        current = stored()
        self.assertEqual(apply_preferences_patch(current, {}), current)
        self.assertEqual(PreferencesPatch.model_validate({}).model_fields_set, set())

    def test_false_and_null_are_real_changes(self) -> None:
        current = stored()
        changed = apply_preferences_patch(
            current, {"enabled": False, "deliveryChannel": None}
        )
        self.assertFalse(changed.enabled)
        self.assertIsNone(changed.channel)
        self.assertEqual(changed.api_token, current.api_token)
        self.assertTrue(current.enabled)
        self.assertEqual(current.channel, "email")

    def test_invalid_full_state_leaves_original_unchanged(self) -> None:
        current = stored()
        with self.assertRaises(ValidationError):
            apply_preferences_patch(current, {"deliveryChannel": None})
        self.assertTrue(current.enabled)
        self.assertEqual(current.channel, "email")

    def test_alias_updates_channel_and_tracks_its_field_name(self) -> None:
        raw: dict[str, object] = {"deliveryChannel": "sms"}
        self.assertEqual(PreferencesPatch.model_validate(raw).model_fields_set, {"channel"})
        changed = apply_preferences_patch(stored(), raw)
        self.assertEqual(changed.channel, "sms")
        self.assertTrue(changed.enabled)

    def test_unwritable_unknown_and_wrong_alias_inputs_are_rejected(self) -> None:
        invalid: tuple[dict[str, object], ...] = (
            {"api_token": "injected"}, {"surprise": True}, {"channel": "sms"},
        )
        for raw in invalid:
            with self.subTest(raw=raw), self.assertRaises(ValidationError):
                apply_preferences_patch(stored(), raw)

    def test_invalid_types_and_channel_are_rejected(self) -> None:
        invalid: tuple[dict[str, object], ...] = (
            {"enabled": "false"}, {"enabled": None}, {"deliveryChannel": "fax"},
        )
        for raw in invalid:
            with self.subTest(raw=raw), self.assertRaises(ValidationError):
                apply_preferences_patch(stored(), raw)

    def test_public_json_contains_only_the_public_contract(self) -> None:
        payload: object = json.loads(public_json(stored()))
        self.assertEqual(payload, {"enabled": True, "deliveryChannel": "email"})

    def test_output_schema_uses_public_alias_and_omits_secret(self) -> None:
        schema = PublicPreferences.model_json_schema(mode="serialization", by_alias=True)
        self.assertEqual(set(schema["properties"]), {"enabled", "deliveryChannel"})
        self.assertEqual(set(schema["required"]), {"enabled", "deliveryChannel"})
```

Run `python -W error -m unittest -v test_preferences`, and use the pinned analyzer
with the settings in [verification](../verification.md). The shared example checks
include both implementation modules and tests; schema API data remains local to
the schema tests.

This is validated in-memory replacement, not a database update or a notification
sender. An application still owns authorization, transaction/concurrent-write
checks, persistence, and resource lifetime; its independent core need not import
these adapter DTOs. The snapshot's frozen fields do not prove arbitrary objects
are immutable or trusted. Map validation errors safely at the outer boundary.
Execution evidence is recorded in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).
