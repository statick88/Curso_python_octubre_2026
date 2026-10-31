# Course examples review
Objective: verify and complete course examples, organized as miniprojects in one repository.
Branch: revision-curso (base origin/main 7c9a115); delivery: work-unit commits and branch push, no PR; checks: unittest, pytest and structural/runtime probes.

## Specs
S1. "verifica que todo este correcto, agrega las rutas necesarias en .gitignore, separa los proyectos"
S2. "verifica la docuemntacion, str doc en cada funcion, completa el codigo que falte, realiza pruebas y sube los cambios"
S3. "actualiza los Readme con los avances y verifica que esten a la par con lo que hemos desarrollado en el ebook"
S4. "Carpetas independientes en este repositorio"; "Repositorio statick88/course_of_python"; "Completar también los ejercicios en la entrega"
S5. "no, todo en un solo repositorio, son miniproyectos de ejemplos del curso"

## Tasks
T1 | S1,S4,S5 | inline: repository boundaries and ignored runtime files | done | commit: pending; check-ignore passed, nested Git HEAD preserved
T2 | S2,S4 | delegated (context backstop): complete practices M0–M10 and feria with their checks and guides | in_progress | commit: pending
T3 | S1,S2,S3,S5 | delegated (context backstop): complete/document/test modular Tetris proyecto2 | in_progress | commit: pending
T4 | S1,S2,S3,S5 | delegated (context backstop): document/test legacy Tetris and weekly examples without erasing didactic bases | in_progress | commit: pending
T5 | S2,S3 | inline: reconcile README with ebook, run seam checks, independent verification for file writes, review if due, commit and push | pending | commit: pending

## Log
L1. Original request: "verifica que todo este correcto, agrega las rutas necesarias en .gitignore, separa los proyectos, verifica la docuemntacion, str doc en cada funcion, completa el codigo que falte, realiza pruebas y sube los cambios, actualiza los Readme con los avances y verifica que esten a la par con lo que hemos desarrollado en el ebook"
L2. User clarification: "Carpetas independientes en este repositorio"; "Repositorio statick88/course_of_python"; "Completar también los ejercicios en la entrega".
L3. Final organization clarification: "no, todo en un solo repositorio, son miniproyectos de ejemplos del curso".
L4. Read-only exploration found legacy Tetris in proyecto/, modular Tetris in proyecto2/ (nested Git without remote), week 3 OOP examples and incomplete practices. Main was 15 commits behind; created revision-curso from fetched origin/main without resetting main or discarding untracked work. The incoming 15 commits supply all M0–M10 practices. Preserve nested Git in an ignored local backup, never delete it. Keep current project paths to avoid breaking commands.
L5. Ebook reference inspected over HTTPS: https://raw.githubusercontent.com/statick88/course_of_python/HEAD/_quarto.yml and labs/practicas-abp-modulos.qmd plus labs/practica-abp-feria-snacks.qmd. Modules M0–M10 and exact practice paths agree with origin/main. Ebook remains read-only; report coverage, not invented curriculum completion.
L6. Forecast: existing untracked Tetris implementations contribute substantial imported code; expected authored corrections/docs/tests exceed 400 lines. Keep reviewable behavioral commits; user requests branch publication, not PR creation. No repository branch-prefix or Sonar configuration detected; native review mode is on. GUI/audio real-device proof may need explicit availability reporting.
L7. T1: moved proyecto2/.git to ignored .local/git-history/proyecto2.git; preserved HEAD 3e0f64df68ed52a8f6b9fdfef114f1b317c3af50 and status (only .atl untracked). Restore if needed by moving the metadata back; no deletion. git check-ignore confirmed venv, pytest cache, agent state and backup exclusions. This is passive configuration: structural verification, no meaningful RED.
L8. T2/T3/T4 dispatched concurrently with disjoint edit surfaces (practice tree, modular Tetris, legacy/weekly examples). Parent is updating root README correspondence and historical-vs-current distinction. Runtime profile check: system Python 3.15.2 lacks pytest, pygame and customtkinter; workers must report the exact available interpreter and GUI proof, not install globally or invent results.
