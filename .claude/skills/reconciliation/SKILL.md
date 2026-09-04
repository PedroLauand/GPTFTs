---
name: reconciliation
description: Check the syntheses, pipeline and draft against the filed sources and against each other, and write a report without fixing anything. Use periodically, before a beat is approved, or when the user says reconcile, audit, check consistency.
---

Read `conventions/meta/workflows/reconciliation.md` and follow it exactly.

If you have not already read `conventions/` in this session, read it first.
`conventions/domain/` has the standing assumptions, notation and glossary;
`conventions/meta/` describes how this repository works.

The workflow file is the definition. This skill only makes it invokable by
name, and an agent without skills reads the same file directly.
