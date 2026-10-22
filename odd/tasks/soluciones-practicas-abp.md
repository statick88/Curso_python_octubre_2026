# Reference solutions for ABP practices
Publish completed examples only on `solucion`; keep student templates on `main`.
Preserve the existing remote history, teacher checks and eighteen weekly examples.

## Specs

- S1. User: «en el repo de codigo de las practicas en la rama solucion publica las soluciones de las tareas».

Acceptance follows the existing per-module `guia.md` and unchanged teacher tests: M0 planning document; M1 exact prompts/output; M2 conversions and formatting; M3 inclusive ranges and a while counter; M4 default/explicit rates; M5 ordered new collections without mutation; M6 vote counts and unique winner; M7 validated UTF-8 CSV to new JSON; M8 greeting catalog reuse; M9 at least four real student test methods detecting the teacher mutants; M10 independent validated JSON pipeline. The three already-published snacks solutions must remain intact. Preserve numeric paths, activity titles and public commands. M0 is one hypothetical reference plan, not a unique correct answer or proof of real-world feasibility.

## Tasks

- T0 | S1 | route: inline parent | reconcile remote main/solucion with new module materials, record initial public RED | commit: 296d6be47359452de5155b12775633951d45b1da | done
- T1 | S1 | route: inline parent | complete M0–M6 and observe focused teacher GREEN | commit: 2890e0e39f5a964d24cb87e73bebe1490a660cfd | done
- T2 | S1 | route: inline parent | complete M7–M10, retain three existing snacks solutions, observe public 58-method GREEN | commit: e3a3353b9f8e7fae0532575f1972e7c75a5b3183 | done
- T3 | S1 | route: inline parent | document branch roles, verify public acceptance, unchanged teacher checks and weekly examples, lint/format | commit: this work unit | done
- T4 | S1 | route: inline parent | publish fast-forward updates without force and confirm remote solution files and tests | commit: pending | in_progress

## Log

- L1. User: «en el repo de codigo de las practicas en la rama solucion publica las soluciones de las tareas».
- L2. Remote main advanced to `c42a4e975e85f0855655104e01da2ce3ccb82684`: README/curriculum updates, variables clarification and four new weekly examples. Existing `solucion` is `d5fb271934ebb854c40099ad86a7ebe1cd1fafb6`, with three completed snacks functions. Preserve both histories and all eighteen weekly examples. Student materials are locally at `9ddebdaa26f9d92cbd7e57142797136271aa0302`.
- L3. Created isolated worktrees `integracion` (`feat/abp-publicacion-integrada`, from remote main) and `soluciones` (`feat/abp-soluciones`, from remote solucion). The original dirty ebook main remains untouched. No push has occurred. Publication retry job-40 stopped at the ancestry preflight; it never started the newly authorized 40-minute render.
- L4. Existing maintenance checks already accept assertion-RED templates and GREEN solutions with unchanged method counts. Do not weaken them. Teacher tests and instructional guides are the public contract; reference code must not import private verification helpers or unfinished exercises.
- L5. Public initial RED observed: exit 1, 58 teacher methods, assertion failures only; twelve existing snacks checks remain GREEN. No private references were injected. README merge preserves the remote eighteen-example index and all curriculum checkboxes; weekly Python files and three existing snacks solutions remain byte-identical.
- L6. T1: existing public tests for M0–M6 all GREEN (32 methods, exit 0, no output/errors/skips); seven artifacts pass Ruff check and format. M3 uses the required while loop; M0 contains explicitly hypothetical data and still requires instructor judgment. Risk: none; weekly examples, teacher tests and existing snacks solutions are unchanged.
- L7. T2: all 58 original public teacher methods and three maintenance methods pass using the real solution files. Ruff check and all 38-file format checks pass, without suppressions. CSV rows and JSON schema are validated before new-file creation; exclusive mode prevents overwrites. M8 reuses SALUDOS; M9 supplies four assertion methods detected by the existing mutant grader. A pure M10 schema predicate preserves contractual ValueError while resolving TRY004; no exception contract was weakened. Existing snacks answers remain unchanged. Risk: none (validated new records, no stored-data rewrites or unrelated contracts).
- L8. T3: branch-role banners distinguish solved references from main templates in both catalogs and all eleven guides. New solution-only acceptance test rejects an isolated copy of unfinished main material (RED) and accepts actual solved files (GREEN); it reads no Git history. Four organization/acceptance methods pass, including a real 58-method teacher run. All teacher/discovery files remain byte-identical to student integration; all eighteen weekly scripts and three previous snacks answers are preserved. All Python files compile; Ruff check and format pass (41 checked formatting surfaces). Local catalog paths resolve. Risk: none; no existing tests weakened, no secrets/crypto/certificate material introduced, JSON is schema-validated and new files use exclusive creation. Publication waits for the separately authorized ebook render.
