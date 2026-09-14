# Architecture audit

The 2.0/2.1 rebuild had an architectural regression: it made the BetterDiscord file effectively self-contained while leaving the historical modular files disconnected. That defeated one of Chouquette Glass's original strengths: users could keep a small config file while the remotely imported core and animations were maintained separately.

2.3 fixes the chain explicitly.

The repository now has two outputs with different purposes:

1. **Public loader** — small, editable and remote-updating.
2. **Standalone preview** — bundled local test build.

No CSS module in the active import graph is empty.
