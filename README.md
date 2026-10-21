# Agent_Engineering_Kit

A reusable library of engineering rules, project instructions, and workflow
templates for AI coding agents in Codex, Claude Code, and Cursor. Adopt the
resources that match your stack in a new or existing project, covering architecture,
coding practices, verification, and agent collaboration.

## Technologies

- **Python:** FastAPI, Pydantic, SQLAlchemy, Psycopg.
- **PHP:** Symfony, Doctrine.
- **Go:** Gin.
- **JavaScript / TypeScript:** Node.js, NestJS, React, Next.js, Angular, NgRx, TypeORM.
- **Database and containers:** PostgreSQL, Docker.
- **Game development:** Unreal Engine, including C++ and Blueprints; [Godot](standards/godot.md),
  with GDScript and conditional C#/GDExtension guidance.

Select only the technologies your project uses; available profiles are listed in
[the catalog](standards/catalog.toml).

## Adopt in your project

1. Clone or download this library to a location your agent can read.
2. Open the target project in Codex, Claude Code, or Cursor. Replace the placeholders
   below with the library path, project path, and selected client, then send the request:

> Read `templates/skills/aek-integrate-project/SKILL.md` from the Agent_Engineering_Kit
> source at `<framework-path>`. For the project at `<project-path>` using
> `<client>`, prepare an import of the applicable rules. Show the proposed file
> changes and conflict resolutions. Leave the target project untouched.

3. Review the proposal, then ask the agent to apply it:

> Apply the prepared Agent_Engineering_Kit import to `<project-path>` for `<client>`
> within the reviewed scope. Preserve unrelated changes and existing model choices,
> and follow the agreed checkpoints.

The agent selects the relevant rules, adapts project instructions, checks the
adopted references, and records the import. No package or global skill installation
is required. Integration and model-setup skills run from the library source by
default; they are not installed in the target's `.agents/skills`. That directory
is created only for explicitly selected persistent skills, such as the optional
design/review entries. Keep the library source accessible for future updates.

See [MIGRATION.md](MIGRATION.md) for the full procedure, updates, and recovery.
