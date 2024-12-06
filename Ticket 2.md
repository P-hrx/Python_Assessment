# Ticket MIDP-313

The sales system seems to have been bugging out, and starting on the 16th will send some bad data. We need to add some validation to the system to create a csv report daily for any bad records that come in, so we can investigate and get the
source system to resend those records.

---

## Acceptance Criteria

The ingestion pipeline creates a daily csv file for each file processed in an `error_reports` folder.

An error is defined as any field that does not match the schema provided in `./src/configs/schemas.py`. If a string is in a field where the type is `int`, that is an error. If an enum is passed that does not match the `valid_values`, that
is an error.

The files should always be generated even if there are no errors. They will have the full rows of data that have any errors on any field. The files will be named `errors_$sourceName_YYYYMMDD.csv`.

We will want to rerun all files after this is implemented.

> The "broken" data exists in the `./data_for_ticket_2/` folder. Copy it into the `./landing_zone/` folder when ready.
