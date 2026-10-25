# Contributing

Thanks for helping make this list better!

## Adding an entry

1. Find (or create) the section that fits best.
2. Add one line at the end of the section:

   ```
   - [owner/repo](https://github.com/owner/repo) — Short description of what it does.
   ```

3. Keep descriptions short (one line), in English, and describe what the tool *does*, not how great it is.
4. Entries must be relevant to ROOT (CERN): bindings, I/O implementations, viewers, editor plugins, training material, open data, etc., with a working link.
5. Non-GitHub links (GitLab, Codeberg, docs sites…) are fine too — they just won't get star metadata.

## Guidelines

- Check that the link works before submitting.
- Don't add duplicates — search the README first.
- Sections are ordered alphabetically; keep them that way.
- A project being small is fine, but it must be installable/usable.
- If a project only works with old ROOT versions (pre-6.26), put it under **Outdated**.
- If you add a **new section**, also mirror it in `_sidebar.md` (used by the GitHub Pages site).
- Don't add `⭐/🗓` metadata yourself — a weekly GitHub Action (`.github/workflows/update-meta.yml`) appends and refreshes it automatically.

## The website

<https://cxwx.github.io/awesome-root-cern/> is rendered by [docsify](https://docsify.js.org) directly from `README.md` — there is nothing to build. Just edit the README and the site updates on the next push.
