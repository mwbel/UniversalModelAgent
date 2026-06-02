# AGENTS.md

This file guides Codex when working in this repository.

## Language

- Use Chinese when communicating with the user.
- Keep commands, paths, API names, environment variables, and schema keys in English.

## Project Direction

This project is a local-first Universe Model Agent. It combines:

- local RAG strategies
- DeepSeek-compatible answer generation
- astronomy-focused interactive visualizations

Interactive visualization work should follow the A2UI-oriented approach used by `edu-viz-core-main`: the agent chooses a declared capability, emits a structured render instruction, and the frontend renders it through a consistent surface.

## A2UI Visualization Rules

Do not add new visualizations as one-off hardcoded buttons or ad hoc if/else branches.

Every visualization capability must be registered in:

- `backend/visualization_catalog.py`

Each capability should declare:

- `id`
- `title`
- `description`
- `concepts`
- `keywords`
- `tags`
- `a2ui_hint`
- `expresses`
- `educational_use`
- `cannot_express`
- `implementation_kind`
- `source_entry`
- `trigger_patterns`
- `plugin_id`
- `component_id`
- `intent_type`
- `props_schema`
- `default_props`
- `interaction_events`
- `feedback_contract`

The planner in `backend/services/visualization_planner.py` is the only place that should decide which visualization capability to return for a question.

Planner output must include:

- `matchScore`
- `matchReasons`
- `matchedConcepts`
- `renderMode`
- `generatorType`
- `a2uiInstruction`
- `embedUrl`
- `galleryUrl`

The current frontend may still use iframe fallback rendering, but all new capabilities must provide an `a2uiInstruction` with:

- `protocol`
- `surface`
- `pluginId`
- `componentId`
- `intentType`
- `initialProps`
- `propsSchema`
- `events`
- `feedbackContract`
- `fallback`

## Interaction Feedback

When adding real A2UI components later, user interactions should be designed to flow back into the teaching conversation. At minimum, define the intended feedback payload in `feedback_contract` before implementing the UI.

Examples:

- selected body in a solar-system scene
- current date in an ephemeris comparison
- observer frame in a retrograde-motion demo
- selected moon phase in an eclipse demo

## Frontend

The current renderer lives in:

- `frontend/app.js`

It should display the chosen visualization, preserve the fallback embed path, and expose enough A2UI metadata for debugging. When replacing iframe rendering with a real A2UI renderer, keep the same planner response shape so backend orchestration remains stable.

## Verification

For visualization changes, run:

```bash
python3 -m py_compile backend/*.py backend/services/*.py
node -e "const fs=require('fs'); new Function(fs.readFileSync('frontend/app.js','utf8')); console.log('frontend ok')"
```

If the local server is running, also verify:

```bash
curl -s "http://127.0.0.1:8787/api/visualizations/plan?question=为什么会发生月食"
```
