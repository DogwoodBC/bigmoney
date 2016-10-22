COPY (SELECT *
      FROM data_contributorindividual)
TO 'c:\\temp\\data_contributorindividual.csv' WITH CSV HEADER;

COPY (SELECT *
      FROM data_contributororganization)
TO 'c:\\temp\\data_contributororganization.csv' WITH CSV HEADER;