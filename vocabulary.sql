--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.5
-- Dumped by pg_dump version 9.6.6

-- Started on 2017-12-06 11:11:14 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 11793)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 1979 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 171 (class 1259 OID 1769842)
-- Name: vocabulary; Type: TABLE; Schema: public; Owner: databaser
--

CREATE TABLE vocabulary (
    word text,
    "I" bigint,
    "E" bigint,
    "N" bigint,
    "S" bigint,
    "T" bigint,
    "F" bigint,
    "J" bigint,
    "P" bigint
);


ALTER TABLE vocabulary OWNER TO databaser;

--
-- TOC entry 1971 (class 0 OID 1769842)
-- Dependencies: 171
-- Data for Name: vocabulary; Type: TABLE DATA; Schema: public; Owner: databaser
--

COPY vocabulary (word, "I", "E", "N", "S", "T", "F", "J", "P") FROM stdin;
somewhat	890	217	942	165	515	592	441	666
rank	85	30	93	22	60	55	48	67
relationship	3252	1024	3716	560	1827	2449	1801	2475
item	175	52	189	38	104	123	99	128
cherish	48	13	51	10	22	39	25	36
leg	234	67	257	44	139	162	118	183
share	1530	446	1751	225	819	1157	851	1125
hey	1539	589	1825	303	868	1260	789	1339
welcome	1554	554	1798	310	906	1202	925	1183
think	6398	1937	7210	1125	3805	4530	3285	5050
latest	166	43	172	37	100	109	89	120
\.


--
-- TOC entry 1978 (class 0 OID 0)
-- Dependencies: 6
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2017-12-06 11:11:14 CET

--
-- PostgreSQL database dump complete
--

