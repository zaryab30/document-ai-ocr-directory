# Contributing

This is a curated directory of public **Document AI & OCR tools**. Listings are
pointers to upstream projects/products (name, org, attributes, links) — no
third-party code is vendored.

## Add or update an entry

1. Edit [`data.py`](data.py) — add a `Tool(...)` with accurate org, category,
   open-source flag, the exact license, a note, and a repo or homepage.
   Cite a source; omit anything you can't verify.
2. Run `python main.py generate` to refresh `README.md`.
3. Run `pytest -q`.
4. Open a PR linking the project.

## Quality bar

- Use `proprietary` for managed APIs; record the actual OSS license otherwise
  (note copyleft like AGPL/GPL). Open-source entries must link a repository.
- `python main.py generate` must leave `README.md` unchanged in CI.
