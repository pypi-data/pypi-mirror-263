# tk-core

Centralized core functionality for Terakeet SD, DS, DE, etc.

# APIs

## Current

- [common](src/tk_core/common/README.md)
  - anything you find yourself using frequently could be added here
- [serp_api](src/tk_core/serp_api/README.md)
  - anything related to <a href=https://serpapi.com>SERPAPI</a>
  - there is a base class for all Google endpoints: `serp_api.base.py:SERPAPI`
- [snowflake](src/tk_core/snowkeet/README.md)
  - anything related to snowflake
- [core](src/tk_core/core/README.md)
  - functionality that is core to the other sub-modules in the package

## Future

- google
- open_ai
- semrush

## Examples

Each sub-packages should have their own directory inside the `examples` directory. These will be built out over time to help (along with the documentation) understand functionality and common use cases for the tk-core package.

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

# Questions, Concerns, Bugs

Clone the repo, create a PR and give it a shot your self. Make sure to write some tests--or update the existing ones--with any changing functionality. Feel free to reach out to the engineering team for help.
