# Unreal, Blender и MCP: skills и проверки после блока изменений

Дата исследования: **2026-09-29**. Запрос: сохранить полезные названия/ссылки и
сократить расход контекста на повторные проверки при работе с движком и редактором.
Использованы Superpowers и find-skills. Это исследование инструкций и открытых
источников; запусков Unreal/Blender и измерений экономии токенов не было.

## Что подтверждают источники

1. [Epic: автоматизация редактора](https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor)
   описывает программное выполнение повторяемых действий, размещение акторов и
   пайплайны импорта. Это основание объединять известные операции в скрипт.
2. [Epic: native MCP](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor)
   предусматривает Tool Search: три метаинструмента вместо загрузки всех схем.
   Та же документация предписывает не перекрывать вызовы к редактору.
3. [Epic: официальный plugin skills](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin)
   содержит `unreal-mcp`, `create-toolset` и `unreal-skill`; README описывает
   выполнение нескольких операций через Python. Наличие этой возможности в
   репозитории не доказывает её наличие в конкретной сборке пользователя.
4. [Anthropic: code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
   рекомендует загружать инструменты по потребности, фильтровать данные до передачи
   модели и выполнять связанную логику внутри среды исполнения. Опубликованные
   показатели экономии относятся к их примеру, не к нашему Unreal-проекту.
5. [ptrthomas: Blender skill](https://github.com/ptrthomas/blender-agent/blob/main/.claude/skills/blender/SKILL.md)
   прямо рекомендует объединять изменения перед рендером и повышать качество
   предпросмотра по необходимости. Это community-рекомендация; HTTP bridge и
   примеры аварийного завершения процессов не перенесены в наши правила.

**Наш вывод:** использовать цикл «контекст и восстановимое состояние → связанный
блок изменений → достаточная проверка результата». Ни Epic, ни Anthropic не задают
универсального числа действий или обязательного процента экономии. Ограничение
контекста обеспечивают выборочная загрузка, краткие результаты и отсутствие
повторных циклов без причины, а не пропуск обязательных проверок.

## Отбор навыков

Проверены leaderboard skills.sh, результаты `npx skills find blender` и
`npx skills find unreal`, затем исходные SKILL.md и страницы репозиториев.
Выдача Unreal содержит много нерелевантных популярных навыков; популярность
сама по себе не использовалась как основание рекомендации.

Основной выбор для native Unreal MCP — три навыка Epic. Для Blender сохранены
`blender-modeling` и условно `blender-export` из RobLe3/cc-blender-skill.
Названия, ссылки, сигналы популярности и ограничения находятся в переносимом
[каталоге](../../standards/unreal-engine/skills.md). Рецепты экспорта содержат
общие бюджеты и настройки, которые нельзя считать требованиями Unreal-проекта.
MCP provider Blender выделен отдельно от skills; установка не выполнялась.

Обнаружено расхождение источников Epic: текущий `unreal-mcp` допускает отдельные
независимые параллельные вызовы, страница UE 5.8 требует последовательных.
Сохранено последовательное выполнение; для данной задачи параллельность не нужна.

## Практические границы блока

| Работа | Выполнить вместе | Проверить на границе |
| --- | --- | --- |
| Расстановка группы props | Создание, transform и материалы связанных объектов | Затронутые свойства и нужный вид сцены |
| Blueprint-взаимодействие | Узлы, связи, параметры законченного поведения | Compile изменённых Blueprint и целевой PIE-сценарий |
| Blender → Unreal | Подготовка объекта, нужные материалы, экспорт и импорт | Нужные свойства импортированного ассета в Unreal |
| C++ gameplay | Согласованное изменение кода и необходимого покрытия | Соответствующая сборка и проверка поведения |

Сбой инструмента, неопределённый исход мутации или зависимость от новой сборки
останавливают зависимую работу сразу. Для незнакомого импорта сначала проверяется
репрезентативный ассет, затем обрабатывается оставшаяся группа. Один скриншот
не доказывает поведение, один render не доказывает timing, наличие FBX не доказывает
правильность импорта. После исправления повторяется затронутая проверка.

Реализация политики: [Unreal verification](../../standards/unreal-engine/verification.md)
и [MCP/editor](../../standards/unreal-engine/mcp-editor.md). Каталог включён в
переносимый комплект, но читается только при выборе навыков.

## 2026-10-23 addendum: relocated adoption signals

Moved from `standards/unreal-engine/skills.md` on 2026-10-23; observed 2026-09-29
and not rechecked:

> The Epic repository is vendor-owned (311 GitHub stars observed); a verified
> skills.sh install count was not established. For RobLe3, the directory reported
> about 1.2K installs for modeling and 714 for export; the repository had 77 stars.

Directory links: [modeling](https://skills.sh/roble3/cc-blender-skill/blender-modeling),
[export](https://skills.sh/roble3/cc-blender-skill/blender-export). Example
individual installation recorded then:
`npx skills add RobLe3/cc-blender-skill@blender-modeling`. These are dated adoption
signals, not proof of correctness or a current installation instruction.

2026-10-23 wording check: the UE 5.8
[Unreal MCP page](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor?application_version=5.8)
states that the server executes tool invocations serially on the game thread,
"meaning clients should not issue overlapping Tool calls". The earlier text above
described this as a requirement; the standards now label non-overlap as local policy.

2026-10-23 telemetry check: the same UE 5.8 page's console-variable table lists
`ModelContextProtocol.EnableAnalytics`, type `bool`, default `true`, described as
"Gate telemetry emission". The standards now apply the shared local policy of
disabling optional telemetry where supported; enabling it is a project decision.
