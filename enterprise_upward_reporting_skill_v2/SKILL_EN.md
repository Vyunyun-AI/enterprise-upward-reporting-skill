---
name: enterprise_upward_reporting_cn_soe_en
version: 2.0.0
language: en
summary: Rewrites draft materials into formal upward-reporting documents aligned with governance, supervision, and compliance expectations of mainland Chinese SOEs.
owner: OpenAI-generated from user-provided source
entrypoint: SKILL_EN.md
---

# Skill: Upward Reporting Optimization for Mainland Chinese SOEs

## Purpose
Transform user-provided drafts into formal upward-reporting documents aligned with the governance logic, supervisory expectations, and compliance standards commonly used in mainland Chinese state-owned enterprises.

## Use this skill when
- The user asks to turn a draft into a formal memo, report, reply, rectification note, or internal submission.
- The source material is a business update, issue explanation, rectification response, inspection response, or compliance-oriented status report.
- The user wants stronger political positioning, business metrics support, and closed-loop compliance language.

## Do not use this skill when
- The task is advertising, marketing copy, or social-media writing.
- The task is academic, journalistic, or literary writing.
- The request depends on fabricating facts, metrics, policy references, or accountable persons.

## Core method
1. Classify the draft into a reporting pattern.
2. Restructure it using the standard model.
3. Upgrade the text along three dimensions: political positioning, business metrics, and compliance closure.
4. Normalize the language into disciplined formal-institutional prose.
5. Run a truthfulness check before final output.

## Three mandatory dimensions
### Political positioning
Open with alignment to central policy direction, supervisory logic, or higher-level deployment, and explain why the matter matters.

### Business metrics
Use KPI logic, operational evidence, and trend explanations. Never invent numbers.

### Compliance closure
Express a full chain of fact, basis, corrective actions, observed effects, and next-step arrangements.

## Required output
Return:
1. The optimized full report text.
2. A short optimization note explaining improvements across political positioning, business metrics, and compliance closure.

## Guardrails
- Do not fabricate facts, policies, IDs, or names.
- Do not conceal problems with inflated rhetoric.
- Do not over-question the user when information is incomplete; produce the best grounded version from available material.
