# tk-core

Centralized core functionality for Terakeet SD, DS, DE, etc.

# APIs

## Current

- common
  - anything you find yourself using frequently could be added here
- serp_api
  - anything related to <a href=https://serpapi.com>SERPAPI</a>
  - there is a base class for all Google endpoints: `serp_api.base.py:SERPAPI`
- snowflake

  - anything related to snowflake

- core
  - functionality that is core to the other sub-modules in the package

## Future

- google
- open_ai
- semrush

# Project Structure

```
tk-core
|
├── src
│   └── tk_core
│       ├── common
│       │   ├── de_service.py
│       │   ├── dictionary.py
│       │   ├── files.py
│       │   ├── hasher.py
│       │   └── s3.py
|       |
│       ├── core
│       │   └── models.py
|       |
│       ├── google (future)
│       │   ├── gsc.py
│       │   ├── ga.py
│       │   ├── sheets.py
│       │   ├── calendar.py
│       │   └── gmail.py
|       |
│       ├── open_ai (future)
|       |
│       ├── semrush (future)
|       |
│       ├── serp_api
│       │   ├── README.md
│       │   ├── base.py
│       │   ├── batch_serp.py
│       │   ├── format_for_snowflake.py
│       │   ├── models.py
│       │   ├── serp.py
│       │   ├── trend.py
│       │   └── util.py
|       |
│       └── snowflake
│       │   ├── error_wrapper.py
│       │   ├── snowkeet_new.py
│           └── snowkeet.py
└── test
    ├── common
    ├── core
    └── serpapi
|
├── README.md
├── .coveragerc
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
```
