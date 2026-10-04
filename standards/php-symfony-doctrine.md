# PHP / Symfony / Doctrine

Compatibility entry for existing `php-symfony-doctrine` selections. New imports
select [PHP](php.md), [Symfony](symfony.md) and [Doctrine](doctrine.md) for the
actual stack. This aggregate retains their availability; it does not require
reading unused components. Detailed rules belong to those entries and topics.

## PHP essentials

Use [PHP essentials](php.md#php-essentials) for language and resource contracts.

## Read by task

Use the task table for [PHP](php.md#read-by-task),
[Symfony](symfony.md#read-by-task) or [Doctrine](doctrine.md#read-by-task)
only when that component is relevant. Do not traverse all links recursively.

## Symfony essentials

When Symfony is used, follow [its essentials](symfony.md#symfony-essentials).

## Doctrine essentials

When Doctrine is used, follow [its essentials](doctrine.md#doctrine-essentials).
DBAL-only work does not require ORM guidance.

## Framework integration during file moves

Use [PHP verification](php/verification.md) for autoloading and file moves.
Check [Symfony services](symfony/structure-services.md) only with Symfony and
[Doctrine mapping](doctrine/models-mapping.md) only with Doctrine ORM.
Their owners retain the constraints on related registration and schema changes.

## Basis

Evidence remains with the [PHP](php.md#basis), [Symfony](symfony.md#basis)
and [Doctrine](doctrine.md#basis) entries; the aggregate adds no runtime evidence.
