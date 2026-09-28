# Profile evidence record

Research snapshot: **26 September 2026 UTC / 27 September 2026 Asia/Kolkata**. This record separates repository implementation evidence, the supplied résumé, and owner-provided context. A source being present does not establish production reliability or independently verify an award.

## Identity and editorial decisions

- **HARSHIT KUMAR**, pre-final-year B.Tech student specializing in Artificial Intelligence & Machine Learning, VIT-AP University: supplied directly by the owner. The résumé lists B.Tech Computer Science Engineering at Vellore Institute of Technology, A.P.; specialization and current year follow the owner's explicit profile instructions. Grades and CGPA are omitted.
- The exact supplied [GitHub](https://github.com/Harshitcodes154), [LinkedIn](https://www.linkedin.com/in/harshit-kumar-59783b311/) and [email](mailto:harshitkumar7212@gmail.com) identify the profile. No substitute social account was searched for or used.
- **Null Chapter CTF** is the canonical name, following the owner's clarification. The résumé and older portfolio use “Null Matrix CTF”; that older wording was not propagated into the new profile.
- **AXH AI is omitted**, following the owner's later instruction. No technical description or placeholder is invented.
- The résumé's “Wafer AI Map Detection” is represented by the primary **WAFER-GPT** entry, without creating a duplicate wafer project. Current repository code takes precedence over older résumé implementation wording.

## Résumé preservation

The [downloadable résumé](../assets/resume/Harshit-Kumar-Resume.pdf) is a byte-for-byte copy of supplied `latest_mine.pdf`. Its original wording, including “Null Matrix CTF,” remains untouched; correcting the profile did not alter the résumé.

Both files have SHA-256:

```text
1D24B96FD7042BD8B658B4D77C8832B35DE29AE5F3571B09219FEEE9B5F5C314
```

## Project implementation evidence

### WAFER-GPT — primary wafer-defect project

Inspected commit: `3409d7e38f0ceaeb7c53d19e3ad291c958da607b`.

- **Implemented:** image preprocessing, nine-class TensorFlow/Keras CNN inference, class probabilities, Grad-CAM, Gemini-assisted interpretation and contextual chat. Actual preprocessing quantizes grayscale wafer maps to three intensity levels, resizes to 224 × 224, converts to RGB and normalizes. [Inference and Grad-CAM source](https://github.com/Harshitcodes154/WAFER-GPT/blob/3409d7e38f0ceaeb7c53d19e3ad291c958da607b/backend/main.py#L124), [Gemini layer](https://github.com/Harshitcodes154/WAFER-GPT/blob/3409d7e38f0ceaeb7c53d19e3ad291c958da607b/backend/llm.py).
- **Stack:** Python, FastAPI, Uvicorn, TensorFlow/Keras, OpenCV, NumPy, Pillow and Google Gen AI SDK; HTML/CSS/JavaScript frontend. [Dependencies](https://github.com/Harshitcodes154/WAFER-GPT/blob/3409d7e38f0ceaeb7c53d19e3ad291c958da607b/backend/requirements.txt), [frontend](https://github.com/Harshitcodes154/WAFER-GPT/tree/3409d7e38f0ceaeb7c53d19e3ad291c958da607b/frontend), [Dockerfile](https://github.com/Harshitcodes154/WAFER-GPT/blob/3409d7e38f0ceaeb7c53d19e3ad291c958da607b/backend/Dockerfile).
- **Flow:** web upload → FastAPI → preprocessing → CNN / Grad-CAM → Gemini interpretation → JSON results; contextual chat uses a separate endpoint. API responses and model/configuration presence were inspected; repository code was not executed.
- **Availability:** the [Vercel interface](https://wafer-gpt.vercel.app) returned HTTP 200. The configured Railway `/health` returned HTTP 404. The interface link is valid evidence of a published frontend, not a claim that inference was operational during this review.
- **Excluded claims:** accuracy, latency, training dataset size, manufacturing-grade diagnosis, exact Gemini version availability and production readiness. Older résumé references to PyTorch, Gradio and PDF reporting are not used as descriptions of this repository's current implementation.

### ThermoWatch-AI

Inspected commit: `f976b5b3707ff06902893c13f377083fa4beee08`.

- **Implemented:** NASA FIRMS VIIRS retrieval, DBSCAN spatial clustering, nearest-facility attribution using OSM data and BallTree, engineered features, scikit-learn inference, heuristic risk prioritization, Folium visualization and CSV/PDF exports. The Streamlit app contains both application logic and UI. [Application](https://github.com/Harshitcodes154/ThermoWatch-AI/blob/f976b5b3707ff06902893c13f377083fa4beee08/app.py), [dependencies](https://github.com/Harshitcodes154/ThermoWatch-AI/blob/f976b5b3707ff06902893c13f377083fa4beee08/requirements.txt).
- **Model evidence:** training compares ExtraTrees and RandomForest variants using preprocessing pipelines. The exported winner is loaded from Hugging Face by the app; the serialized model was not deserialized in this review, so no specific deployed estimator or accuracy is asserted. [Training](https://github.com/Harshitcodes154/ThermoWatch-AI/blob/f976b5b3707ff06902893c13f377083fa4beee08/scripts/train_source_classifier_v5.py#L485).
- **Scope limits:** training labels derive from source attribution; risk scores are heuristic, not calibrated fire probabilities. Historical temporal processing exists separately; current live features do not establish longitudinal persistence tracking. Open-Meteo supplies weather, not validated fire-spread simulation. [Label construction](https://github.com/Harshitcodes154/ThermoWatch-AI/blob/f976b5b3707ff06902893c13f377083fa4beee08/scripts/build_training_dataset.py#L237), [historical processing](https://github.com/Harshitcodes154/ThermoWatch-AI/blob/f976b5b3707ff06902893c13f377083fa4beee08/temporal_cluster.py).
- **Availability:** [declared Streamlit demo](https://thermowatch-aigit-sih.streamlit.app/) returned HTTP 200; this verifies its web shell, not successful end-to-end inference. Dashboard risk indicators are implemented; email/SMS/emergency alert delivery was not found.

### RazorRecover

- **Implemented prototype:** payment-risk analysis, Gemini-assisted action selection with deterministic fallback, policy checks, simulated retries, audit flow, customer assistant and Streamlit dashboard. [Recovery API](https://github.com/Harshitcodes154/RazorRecover/blob/master/backend/api/recovery.py), [AI agent](https://github.com/Harshitcodes154/RazorRecover/blob/master/backend/services/ai_agent.py), [dashboard](https://github.com/Harshitcodes154/RazorRecover/blob/master/dashboard.py).
- **Stack:** Python, FastAPI, Pydantic, Uvicorn, Gemini, Streamlit and pandas. [Dependency manifest](https://github.com/Harshitcodes154/RazorRecover/blob/master/requirements.txt).
- **Limit:** transactions and recovery execution are simulated using in-memory state. No real funds recovered, live payment-provider integration or durable scheduler is asserted. [Payment engine](https://github.com/Harshitcodes154/RazorRecover/blob/master/backend/services/payment_engine.py), [action executor](https://github.com/Harshitcodes154/RazorRecover/blob/master/backend/services/action_executer.py).
- The repository-declared [Streamlit demo](https://razorrecover-buildathon.streamlit.app/) responded HTTP 200; backend operation was not verified.

### Ashoka Cooling Point

- **Implemented web application:** appliance-service booking flow, Supabase authentication, customer dashboard and admin technician-assignment interface. [Booking flow](https://github.com/Harshitcodes154/Ashoka-Cooling-Point/blob/main/src/pages/Booking.tsx), [dashboard](https://github.com/Harshitcodes154/Ashoka-Cooling-Point/blob/main/src/pages/Dashboard.tsx), [authentication](https://github.com/Harshitcodes154/Ashoka-Cooling-Point/blob/main/src/context/AuthContext.tsx).
- **Stack:** TypeScript, React, Vite, React Router, Tailwind CSS, Framer Motion, Supabase and SQL/PostgreSQL schema. [Dependencies](https://github.com/Harshitcodes154/Ashoka-Cooling-Point/blob/main/package.json), [schema](https://github.com/Harshitcodes154/Ashoka-Cooling-Point/blob/main/supabase/migrations/20231025_init_schema.sql).
- Netlify configuration exists; no public demo was verified. This is an appliance-service app, not an AI temperature-monitoring system. The checked-in schema does not establish audited production security or a complete admin authorization workflow.

### Operation Sindoor

The fictional aerial-combat / air-defense game concept, including aircraft, radar, threat warnings, target locking, missions, HUD and weather atmosphere, comes **directly from the owner**. It is presented as a game, with no claim of a real defense system.

No Operation Sindoor README, source tree or implementation file was fetched. Account-level metadata identifies [OperationSindoor](https://github.com/Harshitcodes154/OperationSindoor) as a C# repository; metadata alone does not establish Unity, Cesium, feature completion or architecture. The profile therefore makes no implementation stack claim for this module. A second similarly named repository exists, so the selected link remains a metadata-based mapping.

## Achievements and participation

The [owner's published portfolio](https://github.com/Harshitcodes154/LATEST_PORTFOLIO/blob/main/index.html) is self-authored evidence. The supplied résumé and conversation are owner attestations. None is treated as independently issued award documentation.

| Profile item | Evidence and wording boundary |
|---|---|
| WAFER-GPT hackathon win | Owner statement plus portfolio heading “Winner — Android Club Hackathon, VIT-AP,” associated with WAFER-GPT. No exact rank, date or prize amount added. |
| Null Chapter CTF — winner | Owner-confirmed corrected name; résumé/portfolio record a win under the older “Null Matrix CTF” wording. No professional cybersecurity role inferred. |
| Google Gen AI Academy, APAC 2026 | Owner supplies 2026; résumé and portfolio support Tracks 1 & 2 and hands-on GenAI/cloud activity. Participation wording, not an invented certification or rank. |
| PixelHack / DAG Club, VIT-AP | Owner supplies DAG Club context; portfolio supports PixelHack participation. No win or rank asserted. |
| Technical Expo / WAFER-GPT presentation | Owner supplies project association; portfolio supports Technical Expo presentation. No award or exact date added. |
| SanDisk Hackathon, if included | Portfolio states participation only; no win, ranking or date asserted. |

## Skill provenance shortlist

| Skill group | Basis |
|---|---|
| Python, TensorFlow/Keras, CNNs, OpenCV, Grad-CAM, FastAPI, Gemini | WAFER-GPT implementation and dependencies. |
| scikit-learn, pandas, geospatial processing, Streamlit, Folium | ThermoWatch implementation; Streamlit also used by RazorRecover. |
| Agentic application patterns | RazorRecover's AI/action/policy pipeline; additional agentic learning context in the résumé. Prototype scope is retained. |
| JavaScript, TypeScript, React, HTML/CSS, SQL | WAFER frontend and Ashoka Cooling Point source/schema. |
| Java and C | Supplied résumé; not attributed to these inspected AI repositories. C++ proficiency is not inferred from C. |
| Docker | WAFER Dockerfile; résumé also describes containerization work. |
| Google Cloud, Vertex AI, Cloud Run, AWS services | Résumé/owner-provided experience; not misrepresented as deployment targets of WAFER or ThermoWatch. |
| Linux, systems exploration, game development | Owner-provided interests/focus. C# repository metadata alone is not a proficiency endorsement. |

## Contribution and statistics provenance

The bundled [activity source record](../assets/contribution/activity-source.json) stores GitHub API metadata and the actual daily contribution calendar, with fetch time and definitions. The initial fetch was `2026-09-26T19:07:39Z`. Calendar values are not illustrative data. Streaks are calculated within the captured calendar window; language shares use GitHub Linguist bytes across public non-fork repositories and do not measure proficiency. Repository push timestamps are activity indicators, not build/deployment health.

Project “ONLINE”/command-center status ornamentation expresses the profile's visual theme; it must not be read as continuous monitoring or a verified service-level claim. Future updates should preserve this distinction and refresh data through the bundled update workflow.
