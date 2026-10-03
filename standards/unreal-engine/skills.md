# Optional skills for Unreal, Blender and MCP

Read only when choosing an execution aid or extending the workflow. This is a
reference shortlist, not an installation manifest or a list to preload. Checked
**2026-09-29**. External skills do not replace project rules, actual tool schemas
or the [verification cadence](verification.md#complete-a-coherent-block-then-verify).

## Recommended starting points

| Skill / source | Use when | Compatibility and selection |
| --- | --- | --- |
| [`unreal-mcp` — EpicGames](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/main/skills/unreal-mcp/SKILL.md) | Querying or changing a live Unreal editor through native MCP | Preferred vendor reference for compatible native providers. The distribution targets Claude Code; adapt client setup and tool names to the actual client. Do not assume the skill establishes a live connection. |
| [`create-toolset` — EpicGames](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/main/skills/create-toolset/SKILL.md) | Adding a genuinely missing C++/Python tool to `ToolsetRegistry` | Use only for tool authoring; existing tools should be discovered first. New tools need meaningful failure and mutation coverage, not repeated whole-project tests. |
| [`unreal-skill` — EpicGames](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/main/skills/unreal-skill/SKILL.md) | Capturing a recurring project-specific editor procedure | Unreal Agent Skills and client-side `SKILL.md` packages have different discovery/registration contracts; follow the actual target format. |
| `unreal-engine-mcp` — installed local skill, if available | Existing Codex workflow for native UE MCP setup and operation | Optional local alternative; resolve it from the client's skill inventory. Do not encode a user's absolute skill path in the portable bundle or load both setup guides without need. |
| [`blender-modeling` — RobLe3/cc-blender-skill](https://github.com/RobLe3/cc-blender-skill/blob/main/plugin/skills/blender-modeling/SKILL.md) | Mesh, modifier and procedural prop work through Blender Python/MCP | Community candidate, not Blender-maintained. Match Blender version and MCP execution semantics; preserve project naming instead of imposing its `GEO-` convention. |
| [`blender-export` — RobLe3/cc-blender-skill](https://github.com/RobLe3/cc-blender-skill/blob/main/plugin/skills/blender-export/SKILL.md) | Preparing an asset for the selected Unreal import pipeline | Conditional reference only: review recipes before execution. Do not inherit fixed file/texture/polycount budgets, whole-scene export, transform baking or universal axis settings. Validate a representative import when the pipeline is unfamiliar. |

The Epic repository is vendor-owned (311 GitHub stars observed); a verified
skills.sh install count was not established. For RobLe3, the directory reported
about 1.2K installs for modeling and 714 for export; the repository had 77 stars.
These are dated adoption signals, not proof of correctness. Its export recipes
contain opinionated defaults and require adaptation before production use.

Directory links: [modeling](https://skills.sh/roble3/cc-blender-skill/blender-modeling),
[export](https://skills.sh/roble3/cc-blender-skill/blender-export).
If installation is requested, select individual skills, for example
`npx skills add RobLe3/cc-blender-skill@blender-modeling`; check the destination
and client support before changing configuration. This catalog installs nothing.

## Providers and workflow references are separate

- [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender), formerly
  `blender-mcp`, supplies a community Blender MCP integration, not a standalone
  modeling skill. Match the connected provider's real tools; its presence is not
  implied by loading a skill. It is not an official Blender integration.
- [`blender` — ptrthomas/blender-agent](https://github.com/ptrthomas/blender-agent/blob/main/.claude/skills/blender/SKILL.md)
  is a useful reference for batching adjustments before previewing. Its HTTP
  bridge is a different execution setup, not a drop-in Blender MCP skill.
  Do not adopt its process-killing recovery examples or delegate verification to
  the user when available tools can supply the necessary evidence.
- Use [Superpowers](../superpowers.md) selectively: brainstorming for unresolved
  design, systematic debugging after an actual failure, and verification before
  claiming completion. The framework's block-level checks and evidence reuse
  replace blanket per-edit TDD, fresh reruns and automatic extra reviewers.

## Resolve conflicts before using a recipe

Read the relevant procedure once and apply project scope, recovery and cost
constraints. No automatic tool installation, global configuration edits, asset
renaming, save-all, process restart or whole-scene export follows from this list.
Keep unrelated dirty assets intact.

Epic's current skill permits some independent overlapping calls, while the UE 5.8
[engine documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor)
states that clients should avoid overlapping tool invocations. Retain this
profile's serial-call policy; batching means a bounded sequence, not concurrent
mutations. Resolve version-specific differences only when the task needs them.
