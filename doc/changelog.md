# Changelog

V0.0.9
- Restored time-of-day to the BIDS session label to prevent same-day session collisions
    - `make_session_label` previously truncated to the `YYYY-MM-DD` date only (since V0.0.8), so two sessions scanned on the same calendar day were written under the identical `ses-` label, causing their raw/derivative files to land in the same local BIDS directory and silently overwrite/conflate
    - Now captures the full date+time (e.g. `2026-07-28 09:09:58` or `2026-07-28_09_09_58`) and sanitizes it to alphanumeric-only (e.g. `20260728090958`), keeping dcm2bids' alphanumeric-only session-name constraint satisfied while preserving uniqueness
    - Falls back to date-only if a label has no time component
    - Added unit tests for `make_session_label` (`tests/test_parser.py`)

V0.0.8
- Fixed crash when Flywheel session label uses an underscore instead of a space between date and time (e.g. `2026-06-24_09_09_58`)
    - `make_session_label` now extracts the `YYYY-MM-DD` date via regex and strips non-alphanumeric characters, instead of splitting on whitespace
    - Previously this caused dcm2bids to raise `NameError: Session '...' should contains only alphanumeric characters`, resulting in 0 scans found and no output

V0.0.7
- Added a trigger for acquisition container type (SYSTEM trigger when running gear rules)

V0.0.6
- Updated Docker image to 0.0.6
- Improved output file organization
    - if session level output as normal
    - catch for fiducial file being missing if run on cpu, not gpu

## 0.0.0
```
NJB: 4/11/2024

- Added function to grab all acquisitions from session  

```


## 0.0.0
```
NJB: 25/10/2024

- Initial build of Docker image for Flywheel 

```