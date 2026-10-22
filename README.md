# Foley's Sportsmens Inn website

Live at https://foleyssportsmensinn.com, hosted on Vercel. Every change pushed to `main` publishes automatically.

- `site/` is the website itself (HTML, CSS and images). This is what gets published, and it's what the
  Website Editor edits.
- `menu_data.py` and `build.py` regenerate the pages in `site/` from the menu data. Only run
  `python3 build.py` after copying any changes made directly in `site/` into `build.py`, or it will overwrite them.
- The private-event inquiry form on `parties.html` emails the restaurant through FormSubmit.

Built by Digital Front Door (https://dfd.llc).
