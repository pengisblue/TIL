CREATE TABLE examples (
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples');

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHR(100) NOT NULL
DEFAULT
  '한국';

ALTER TABLE 
  examples
ADD COLUMN 
  Age INTEGER NOT NULL;

ALTER TABLE 
  examples
ADD COLUMN 
  Address VARCHAR(100) NOT NULL;

ALTER TABLE 
  examples
RENAME COLUMN 
  Address TO PostCode;

ALTER TABLE 
  examples
DROP COLUMN 
  PostCode;

ALTER TABLE
  new_examples
RENAME TO
  examples;

DROP TABLE examples;

DROP TABLE new_examples;