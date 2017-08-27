BEGIN;
--
-- Create model EventModel
--
DROP TABLE IF EXISTS "data_flow_eventmodel";
CREATE TABLE data_flow_eventmodel (
    id      INTEGER  NOT NULL  PRIMARY KEY AUTOINCREMENT,
    tick    DOUBLE UNIQUE
                     COLLATE BINARY,
    title   TEXT,
    comment TEXT
);

CREATE INDEX "" ON data_flow_eventmodel (
    tick ASC
);

COMMIT;

--- Insert
INSERT INTO data_flow_eventmodel ( tick, title, comment ) VALUES ( '%s', '%s', '%s' );
--- Query last id
SELECT last_insert_rowid()