# Analyzed Threads Maintenance

This directory contains analyzed Reddit threads and an index file named `Analyzed Threads.md`.

## Rule: Additive Updates Only

When a new analyzed thread `.md` file is created in this repo, you must update `Analyzed Threads.md` to include the new thread.

**Strictly additive. Do not remove or reorder existing entries unless required to maintain alphabetical order.**

## Update Procedure

1. Identify the new analyzed thread file: any file matching `thread_*_analysis.md` under the repo.
2. Extract the thread title and URL from that file.
3. Read the current contents of `Analyzed Threads.md`.
4. Insert the new entry in the correct alphabetical position (case-insensitive) based on the heading text.
5. Follow the existing format exactly:
   - `# Thread Full Title Verbatim`
   - `URL OF THREAD`
   - A blank line between entries
6. Write the updated contents back to `Analyzed Threads.md`.

## Format Reminder

Each entry in `Analyzed Threads.md` must be formatted as:

```markdown
# Thread Full Title Verbatim
URL OF THREAD

# Another Thread Title
ANOTHER_URL

```

No other text, headers, or separators are allowed in this file.
