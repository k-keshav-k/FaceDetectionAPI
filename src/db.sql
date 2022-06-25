create table faces (
   id SERIAL,
   name character varying (200),
   vector double precision [],
   person_name character varying (200),
   version int,
   date character varying(200)
 )
 
--  CREATE OR REPLACE FUNCTION public.euclidian (
--   arr1 double precision [],
--   arr2 double precision [])
--   RETURNS double precision AS
-- $BODY$
--   select sqrt (SUM (tab.v)) as euclidian from (SELECT
--      UNNEST (vec_sub (arr1, arr2)) as v) as tab;
-- $BODY$
-- LANGUAGE sql IMMUTABLE STRICT

-- CREATE OR REPLACE FUNCTION public.vec_sub (
--   arr1 double precision [],
--   arr2 double precision [])
-- RETURNS double precision [] AS
-- $BODY$
--   SELECT array_agg (result)
--     FROM (SELECT (tuple.val1 - tuple.val2) * (tuple.val1 - tuple.val2)
--         AS result
--         FROM (SELECT UNNEST ($1) AS val1
--                , UNNEST ($2) AS val2
--                , generate_subscripts ($1, 1) AS ix) tuple
--     ORDER BY ix) inn;
-- $BODY$
-- LANGUAGE sql IMMUTABLE STRICT

-- select tab.id as tabid, tab.name as tabname,
--         euclidian ('{0.1,0.2,...,0.128}', tab.vector) as eucl from tab
-- order by eulc ASC