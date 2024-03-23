################
influxio backlog
################


************
Iteration +1
************
- [x] Add project boilerplate
- [x] Make it work
- [x] Export to SQLite, PostgreSQL, and CrateDB
- [x] Fix documentation about crate:// target
- [x] Check if using a CrateDB schema works well
- [x] Release 0.1.0


************
Iteration +2
************
- [o] Fix ``.from_lineprotocol``
- [o] Tests using ``assert_dataframe_equal``? Maybe in ``cratedb-toolkit``?
- [o] Support InfluxDB 1.x
- [o] Verify connecting to InfluxDB Cloud works well
- [o] Fix ``cratedb_toolkit.sqlalchemy.patch_inspector()`` re. reflection of ``?schema=`` URL parameter
- [o] Fix ``crate.client.sqlalchemy.dialect.DateTime`` re. ``TimezoneUnawareException``
- [o] Add Docker Compose file for auxiliary services
- [o] Refinements
- [o] Verify documentation. ``influxio.cli.help_copy``
- [o] Refactor general purpose code to ``pueblo`` package
- [o] Verify import and export of ILP and CSV files works well


************
Iteration +3
************
- [o] Unlock more parameters in InfluxDbAdapter.write_df
- [o] Format: Compressed line protocol
- [o] Format: Annotated CSV
  - https://docs.influxdata.com/influxdb/v2.6/reference/syntax/annotated-csv/
  - https://docs.influxdata.com/influxdb/v2.6/reference/syntax/annotated-csv/extended/
- [o] Backends: python, cmdline, flux
- [o] InfluxDB 1.x subscriptions?
- [o] Line protocol builder
  https://github.com/functionoffunction/influx-line
- [o] cloud-to-cloud copy
- [o] influxio list testdata://
- [o] "SQLAlchemy » Dialects built-in" is broken
- [o] ``DBURI = "crate+psycopg://localhost:4200"``
- [o] Use Podman instead of Docker

References
==========
- https://docs.influxdata.com/influxdb/v2.6/migrate-data/
- https://docs.influxdata.com/influxdb/v2.6/reference/cli/influx/write/
- https://docs.influxdata.com/influxdb/v2.6/reference/cli/influx/backup/
- https://docs.influxdata.com/influxdb/v2.6/reference/cli/influx/export/
- https://github.com/influxdata/flux/blob/e513f1483/stdlib/sql/sql_test.flux#L119-L173
- https://github.com/influxdata/flux/blob/e513f1483/stdlib/universe/universe.flux#L1159-L1176
- https://github.com/influxdata/flux/blob/e513f1483/stdlib/sql/to.go#L525
