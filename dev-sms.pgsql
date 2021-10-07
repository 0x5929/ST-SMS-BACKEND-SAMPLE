--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8
-- Dumped by pg_dump version 12.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_emailaddress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailaddress (
    id bigint NOT NULL,
    email character varying(254) NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.account_emailaddress OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailaddress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailaddress_id_seq OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailaddress_id_seq OWNED BY public.account_emailaddress.id;


--
-- Name: account_emailconfirmation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailconfirmation (
    id bigint NOT NULL,
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) NOT NULL,
    email_address_id bigint NOT NULL
);


ALTER TABLE public.account_emailconfirmation OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailconfirmation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailconfirmation_id_seq OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailconfirmation_id_seq OWNED BY public.account_emailconfirmation.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authentication_account; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authentication_account (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    email character varying(254) NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    phone_number character varying(15) NOT NULL,
    is_office boolean NOT NULL,
    is_recruit boolean NOT NULL,
    is_instructor boolean NOT NULL,
    programs character varying(5)[],
    school_name character varying(10) NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_admin boolean NOT NULL,
    is_superuser boolean NOT NULL
);


ALTER TABLE public.authentication_account OWNER TO postgres;

--
-- Name: authentication_account_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authentication_account_groups (
    id bigint NOT NULL,
    account_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.authentication_account_groups OWNER TO postgres;

--
-- Name: authentication_account_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authentication_account_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_account_groups_id_seq OWNER TO postgres;

--
-- Name: authentication_account_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authentication_account_groups_id_seq OWNED BY public.authentication_account_groups.id;


--
-- Name: authentication_account_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authentication_account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_account_id_seq OWNER TO postgres;

--
-- Name: authentication_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authentication_account_id_seq OWNED BY public.authentication_account.id;


--
-- Name: authentication_account_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authentication_account_user_permissions (
    id bigint NOT NULL,
    account_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.authentication_account_user_permissions OWNER TO postgres;

--
-- Name: authentication_account_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authentication_account_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_account_user_permissions_id_seq OWNER TO postgres;

--
-- Name: authentication_account_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authentication_account_user_permissions_id_seq OWNED BY public.authentication_account_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO postgres;

--
-- Name: cms_client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cms_client (
    client_uuid uuid NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone_number character varying(15) NOT NULL,
    initial_contact date NOT NULL,
    email character varying(254) NOT NULL,
    city character varying(200) NOT NULL,
    success boolean NOT NULL,
    recruit_emails character varying(254)[] NOT NULL,
    school_name character varying(10) NOT NULL
);


ALTER TABLE public.cms_client OWNER TO postgres;

--
-- Name: cms_note; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cms_note (
    note_uuid uuid NOT NULL,
    date date NOT NULL,
    product character varying(4) NOT NULL,
    price_currency character varying(3) NOT NULL,
    price numeric(10,2) NOT NULL,
    content text NOT NULL,
    client_id uuid NOT NULL
);


ALTER TABLE public.cms_note OWNER TO postgres;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: gms_baserecord; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_baserecord (
    id bigint NOT NULL,
    date date NOT NULL,
    completed boolean NOT NULL
);


ALTER TABLE public.gms_baserecord OWNER TO postgres;

--
-- Name: gms_baserecord_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.gms_baserecord_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gms_baserecord_id_seq OWNER TO postgres;

--
-- Name: gms_baserecord_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.gms_baserecord_id_seq OWNED BY public.gms_baserecord.id;


--
-- Name: gms_baserotation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_baserotation (
    rotation_uuid uuid NOT NULL,
    school_name character varying(10) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    instructor_email character varying(254) NOT NULL
);


ALTER TABLE public.gms_baserotation OWNER TO postgres;

--
-- Name: gms_basestudent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_basestudent (
    student_uuid uuid NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    makeup_student boolean NOT NULL
);


ALTER TABLE public.gms_basestudent OWNER TO postgres;

--
-- Name: gms_cnaclinicalrecord; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_cnaclinicalrecord (
    baserecord_ptr_id bigint NOT NULL,
    cna_clinical_record_uuid uuid NOT NULL,
    comments character varying(200) NOT NULL,
    performance_satisfied boolean NOT NULL,
    topic character varying(200) NOT NULL,
    student_id uuid NOT NULL
);


ALTER TABLE public.gms_cnaclinicalrecord OWNER TO postgres;

--
-- Name: gms_cnarotation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_cnarotation (
    baserotation_ptr_id uuid NOT NULL,
    rotation_num integer NOT NULL,
    instructor_title character varying(50) NOT NULL,
    clinical_site character varying(50) NOT NULL,
    CONSTRAINT gms_cnarotation_rotation_num_check CHECK ((rotation_num >= 0))
);


ALTER TABLE public.gms_cnarotation OWNER TO postgres;

--
-- Name: gms_cnastudent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_cnastudent (
    basestudent_ptr_id uuid NOT NULL,
    rotation_id uuid NOT NULL
);


ALTER TABLE public.gms_cnastudent OWNER TO postgres;

--
-- Name: gms_cnatheoryrecord; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_cnatheoryrecord (
    baserecord_ptr_id bigint NOT NULL,
    cna_theory_record_uuid uuid NOT NULL,
    hours_spent integer NOT NULL,
    test_score integer,
    topic character varying(200) NOT NULL,
    student_id uuid NOT NULL,
    CONSTRAINT gms_cnatheoryrecord_hours_spent_check CHECK ((hours_spent >= 0))
);


ALTER TABLE public.gms_cnatheoryrecord OWNER TO postgres;

--
-- Name: gms_hhaclinicalrecord; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_hhaclinicalrecord (
    baserecord_ptr_id bigint NOT NULL,
    hha_clinical_record_uuid uuid NOT NULL,
    hours_spent integer NOT NULL,
    comments character varying(200) NOT NULL,
    performance_satisfied boolean NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    topic character varying(200) NOT NULL,
    student_id uuid NOT NULL,
    CONSTRAINT gms_hhaclinicalrecord_hours_spent_check CHECK ((hours_spent >= 0))
);


ALTER TABLE public.gms_hhaclinicalrecord OWNER TO postgres;

--
-- Name: gms_hharotation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_hharotation (
    baserotation_ptr_id uuid NOT NULL,
    rotation_num integer NOT NULL,
    instructor_title character varying(50) NOT NULL,
    clinical_site character varying(50) NOT NULL,
    CONSTRAINT gms_hharotation_rotation_num_check CHECK ((rotation_num >= 0))
);


ALTER TABLE public.gms_hharotation OWNER TO postgres;

--
-- Name: gms_hhastudent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_hhastudent (
    basestudent_ptr_id uuid NOT NULL,
    rotation_id uuid NOT NULL
);


ALTER TABLE public.gms_hhastudent OWNER TO postgres;

--
-- Name: gms_hhatheoryrecord; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gms_hhatheoryrecord (
    baserecord_ptr_id bigint NOT NULL,
    hha_theory_record_uuid uuid NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    hours_spent integer NOT NULL,
    test_score integer,
    topic character varying(200) NOT NULL,
    student_id uuid NOT NULL,
    CONSTRAINT gms_hhatheoryrecord_hours_spent_check CHECK ((hours_spent >= 0))
);


ALTER TABLE public.gms_hhatheoryrecord OWNER TO postgres;

--
-- Name: sms_program; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sms_program (
    program_uuid uuid NOT NULL,
    program_name character varying(4) NOT NULL,
    approval_entities character varying(10)[] NOT NULL,
    school_id uuid
);


ALTER TABLE public.sms_program OWNER TO postgres;

--
-- Name: sms_rotation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sms_rotation (
    rotation_uuid uuid NOT NULL,
    rotation_number integer NOT NULL,
    program_id uuid
);


ALTER TABLE public.sms_rotation OWNER TO postgres;

--
-- Name: sms_school; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sms_school (
    school_uuid uuid NOT NULL,
    school_name character varying(10) NOT NULL,
    school_code character varying(50) NOT NULL,
    school_address character varying(150) NOT NULL,
    year_founded date NOT NULL
);


ALTER TABLE public.sms_school OWNER TO postgres;

--
-- Name: sms_student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sms_student (
    student_uuid uuid NOT NULL,
    student_id character varying(11) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone_number character varying(15) NOT NULL,
    email character varying(254) NOT NULL,
    mailing_address character varying(200) NOT NULL,
    course character varying(4) NOT NULL,
    start_date date NOT NULL,
    completion_date date NOT NULL,
    date_enrollment_agreement_signed date NOT NULL,
    third_party_payer_info character varying(10) NOT NULL,
    course_cost_currency character varying(3) NOT NULL,
    course_cost numeric(10,2) NOT NULL,
    total_charges_charged_currency character varying(3) NOT NULL,
    total_charges_charged numeric(10,2) NOT NULL,
    total_charges_paid_currency character varying(3) NOT NULL,
    total_charges_paid numeric(10,2) NOT NULL,
    paid boolean NOT NULL,
    graduated boolean NOT NULL,
    passed_first_exam boolean NOT NULL,
    passed_second_or_third_exam boolean NOT NULL,
    employed boolean NOT NULL,
    place_of_employment character varying(100) NOT NULL,
    employment_address character varying(150) NOT NULL,
    "position" character varying(50) NOT NULL,
    starting_wage_currency character varying(3) NOT NULL,
    starting_wage numeric(4,2),
    hours_worked_weekly character varying(1) NOT NULL,
    description_of_attempts_to_contact_student text NOT NULL,
    google_sheet_migrated boolean NOT NULL,
    google_sheet_migration_issue character varying(4) NOT NULL,
    rotation_id uuid
);


ALTER TABLE public.sms_student OWNER TO postgres;

--
-- Name: socialaccount_socialaccount; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialaccount (
    id bigint NOT NULL,
    provider character varying(30) NOT NULL,
    uid character varying(191) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    extra_data text NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.socialaccount_socialaccount OWNER TO postgres;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialaccount_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialaccount_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialaccount_id_seq OWNED BY public.socialaccount_socialaccount.id;


--
-- Name: socialaccount_socialapp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialapp (
    id bigint NOT NULL,
    provider character varying(30) NOT NULL,
    name character varying(40) NOT NULL,
    client_id character varying(191) NOT NULL,
    secret character varying(191) NOT NULL,
    key character varying(191) NOT NULL
);


ALTER TABLE public.socialaccount_socialapp OWNER TO postgres;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialapp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialapp_id_seq OWNED BY public.socialaccount_socialapp.id;


--
-- Name: socialaccount_socialapp_sites; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialapp_sites (
    id bigint NOT NULL,
    socialapp_id bigint NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialapp_sites OWNER TO postgres;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialapp_sites_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_sites_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialapp_sites_id_seq OWNED BY public.socialaccount_socialapp_sites.id;


--
-- Name: socialaccount_socialtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialtoken (
    id bigint NOT NULL,
    token text NOT NULL,
    token_secret text NOT NULL,
    expires_at timestamp with time zone,
    account_id bigint NOT NULL,
    app_id bigint NOT NULL
);


ALTER TABLE public.socialaccount_socialtoken OWNER TO postgres;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialtoken_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialtoken_id_seq OWNED BY public.socialaccount_socialtoken.id;


--
-- Name: account_emailaddress id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress ALTER COLUMN id SET DEFAULT nextval('public.account_emailaddress_id_seq'::regclass);


--
-- Name: account_emailconfirmation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation ALTER COLUMN id SET DEFAULT nextval('public.account_emailconfirmation_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: authentication_account id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account ALTER COLUMN id SET DEFAULT nextval('public.authentication_account_id_seq'::regclass);


--
-- Name: authentication_account_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_groups ALTER COLUMN id SET DEFAULT nextval('public.authentication_account_groups_id_seq'::regclass);


--
-- Name: authentication_account_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.authentication_account_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: gms_baserecord id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_baserecord ALTER COLUMN id SET DEFAULT nextval('public.gms_baserecord_id_seq'::regclass);


--
-- Name: socialaccount_socialaccount id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialaccount_id_seq'::regclass);


--
-- Name: socialaccount_socialapp id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_id_seq'::regclass);


--
-- Name: socialaccount_socialapp_sites id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_sites_id_seq'::regclass);


--
-- Name: socialaccount_socialtoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialtoken_id_seq'::regclass);


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
1	root@localhost	t	t	1
2	recruit@st-inst.com	t	t	2
3	selecttherapyinstitute@gmail.com	t	t	3
4	admin@st-inst.com	t	t	4
5	christianm.lara@gmail.com	t	t	5
6	ancamndza@gmail.com	t	t	6
7	support@st-inst.com	t	t	7
\.


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add Token	1	add_token
2	Can change Token	1	change_token
3	Can delete Token	1	delete_token
4	Can view Token	1	view_token
5	Can add token	2	add_tokenproxy
6	Can change token	2	change_tokenproxy
7	Can delete token	2	delete_tokenproxy
8	Can view token	2	view_tokenproxy
9	Can add log entry	3	add_logentry
10	Can change log entry	3	change_logentry
11	Can delete log entry	3	delete_logentry
12	Can view log entry	3	view_logentry
13	Can add permission	4	add_permission
14	Can change permission	4	change_permission
15	Can delete permission	4	delete_permission
16	Can view permission	4	view_permission
17	Can add group	5	add_group
18	Can change group	5	change_group
19	Can delete group	5	delete_group
20	Can view group	5	view_group
21	Can add content type	6	add_contenttype
22	Can change content type	6	change_contenttype
23	Can delete content type	6	delete_contenttype
24	Can view content type	6	view_contenttype
25	Can add session	7	add_session
26	Can change session	7	change_session
27	Can delete session	7	delete_session
28	Can view session	7	view_session
29	Can add site	8	add_site
30	Can change site	8	change_site
31	Can delete site	8	delete_site
32	Can view site	8	view_site
33	Can add email address	9	add_emailaddress
34	Can change email address	9	change_emailaddress
35	Can delete email address	9	delete_emailaddress
36	Can view email address	9	view_emailaddress
37	Can add email confirmation	10	add_emailconfirmation
38	Can change email confirmation	10	change_emailconfirmation
39	Can delete email confirmation	10	delete_emailconfirmation
40	Can view email confirmation	10	view_emailconfirmation
41	Can add social account	11	add_socialaccount
42	Can change social account	11	change_socialaccount
43	Can delete social account	11	delete_socialaccount
44	Can view social account	11	view_socialaccount
45	Can add social application	12	add_socialapp
46	Can change social application	12	change_socialapp
47	Can delete social application	12	delete_socialapp
48	Can view social application	12	view_socialapp
49	Can add social application token	13	add_socialtoken
50	Can change social application token	13	change_socialtoken
51	Can delete social application token	13	delete_socialtoken
52	Can view social application token	13	view_socialtoken
53	Can add account	14	add_account
54	Can change account	14	change_account
55	Can delete account	14	delete_account
56	Can view account	14	view_account
57	Can add program	15	add_program
58	Can change program	15	change_program
59	Can delete program	15	delete_program
60	Can view program	15	view_program
61	Can add rotation	16	add_rotation
62	Can change rotation	16	change_rotation
63	Can delete rotation	16	delete_rotation
64	Can view rotation	16	view_rotation
65	Can add school	17	add_school
66	Can change school	17	change_school
67	Can delete school	17	delete_school
68	Can view school	17	view_school
69	Can add student	18	add_student
70	Can change student	18	change_student
71	Can delete student	18	delete_student
72	Can view student	18	view_student
73	Can add client	19	add_client
74	Can change client	19	change_client
75	Can delete client	19	delete_client
76	Can view client	19	view_client
77	Can add note	20	add_note
78	Can change note	20	change_note
79	Can delete note	20	delete_note
80	Can view note	20	view_note
81	Can add base record	21	add_baserecord
82	Can change base record	21	change_baserecord
83	Can delete base record	21	delete_baserecord
84	Can view base record	21	view_baserecord
85	Can add base rotation	22	add_baserotation
86	Can change base rotation	22	change_baserotation
87	Can delete base rotation	22	delete_baserotation
88	Can view base rotation	22	view_baserotation
89	Can add base student	23	add_basestudent
90	Can change base student	23	change_basestudent
91	Can delete base student	23	delete_basestudent
92	Can view base student	23	view_basestudent
93	Can add CNA Rotation	24	add_cnarotation
94	Can change CNA Rotation	24	change_cnarotation
95	Can delete CNA Rotation	24	delete_cnarotation
96	Can view CNA Rotation	24	view_cnarotation
97	Can add CNA Student	25	add_cnastudent
98	Can change CNA Student	25	change_cnastudent
99	Can delete CNA Student	25	delete_cnastudent
100	Can view CNA Student	25	view_cnastudent
101	Can add HHA Rotation	26	add_hharotation
102	Can change HHA Rotation	26	change_hharotation
103	Can delete HHA Rotation	26	delete_hharotation
104	Can view HHA Rotation	26	view_hharotation
105	Can add HHA Student	27	add_hhastudent
106	Can change HHA Student	27	change_hhastudent
107	Can delete HHA Student	27	delete_hhastudent
108	Can view HHA Student	27	view_hhastudent
109	Can add HHA Theory Record	28	add_hhatheoryrecord
110	Can change HHA Theory Record	28	change_hhatheoryrecord
111	Can delete HHA Theory Record	28	delete_hhatheoryrecord
112	Can view HHA Theory Record	28	view_hhatheoryrecord
113	Can add HHA Clinical Record	29	add_hhaclinicalrecord
114	Can change HHA Clinical Record	29	change_hhaclinicalrecord
115	Can delete HHA Clinical Record	29	delete_hhaclinicalrecord
116	Can view HHA Clinical Record	29	view_hhaclinicalrecord
117	Can add CNA Theory Record	30	add_cnatheoryrecord
118	Can change CNA Theory Record	30	change_cnatheoryrecord
119	Can delete CNA Theory Record	30	delete_cnatheoryrecord
120	Can view CNA Theory Record	30	view_cnatheoryrecord
121	Can add CNA Clinical Record	31	add_cnaclinicalrecord
122	Can change CNA Clinical Record	31	change_cnaclinicalrecord
123	Can delete CNA Clinical Record	31	delete_cnaclinicalrecord
124	Can view CNA Clinical Record	31	view_cnaclinicalrecord
\.


--
-- Data for Name: authentication_account; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authentication_account (id, password, last_login, email, username, first_name, last_name, date_joined, phone_number, is_office, is_recruit, is_instructor, programs, school_name, is_active, is_staff, is_admin, is_superuser) FROM stdin;
3	pbkdf2_sha256$260000$xqaQhoMPP9QS0iGcrNo1Bc$+Hu9JqWxn2yEKvzHiNYTLPSHM8lYYLqAudpHOOv1Pz0=	\N	selecttherapyinstitute@gmail.com	k.di	Kai	Di	2021-10-06 12:21:12.705225-07		t	t	f	{}		t	t	f	f
4	pbkdf2_sha256$260000$8oo4l1CCrJdFhSXVSOu9p6$SiM5Rcnbs7VaB9kSdga8ZxSdB/WOOqddODEwSKYQzsQ=	\N	admin@st-inst.com	k.ren	Kevin	Ren	2021-10-06 12:25:03.557498-07		t	t	t	{CNA,HHA}		t	t	t	f
5	pbkdf2_sha256$260000$79rbqP4EJHnVxrcoptsh1G$JkAiOU1R6gdeYMd6DMEqRqPCm+oXvaWeuLciNsfC07k=	\N	christianm.lara@gmail.com	c.lara	Christian	Lara	2021-10-06 12:27:01.875504-07		f	f	t	{CNA,HHA}		t	f	f	f
6	pbkdf2_sha256$260000$YVVFSlvvZ6gAhi0C8lEn4t$b8b8VkMq9OeO63w9nwQjWHY60Fi2Q6cNzb0rkp287gQ=	\N	ancamndza@gmail.com	p.curby	Patricia	Curby	2021-10-06 12:27:45.03637-07		f	f	t	{CNA}		t	f	f	f
2	pbkdf2_sha256$260000$nqcTn09JGkKsdvuD3dlGYL$ysxA9z2H6bJIiTezjRBl0uDzTqtL3LLjisxdj5b4Nxo=	2021-10-06 15:39:15.954303-07	recruit@st-inst.com	n.liang	Nan	Liang	2021-10-06 12:19:23.888886-07		t	t	f	{}		t	t	f	f
1	pbkdf2_sha256$260000$e8ZPfgrXgn8uXs1XB8jphK$WaeXyUtMK78SwaN/Pd8BEiTEfuulzf4v8icDvxyd1Aw=	2021-10-06 15:39:47.105807-07	root@localhost	root	root	root	2021-10-06 12:17:36.413239-07		t	t	t	{CNA,HHA}		t	t	t	t
7	pbkdf2_sha256$260000$Yj9BMCsccJre9WDmyo9NWh$G581lZg2T1fQ3S4/4c8GNTpt4uX2IBc6GsOq70LhlCg=	\N	support@st-inst.com	p.hu	Peiyi	Hu	2021-10-07 08:43:52.158473-07		t	f	f	{}		t	f	f	f
\.


--
-- Data for Name: authentication_account_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authentication_account_groups (id, account_id, group_id) FROM stdin;
\.


--
-- Data for Name: authentication_account_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authentication_account_user_permissions (id, account_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
\.


--
-- Data for Name: cms_client; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cms_client (client_uuid, first_name, last_name, phone_number, initial_contact, email, city, success, recruit_emails, school_name) FROM stdin;
1b6f00a6-dec7-4766-be71-2ce630eb2df5	Testclient	A	626-555-5455	2021-10-06	testclienta@email.com	Rosemead	f	{recruit@st-inst.com,selecttherapyinstitute@gmail.com}	
\.


--
-- Data for Name: cms_note; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cms_note (note_uuid, date, product, price_currency, price, content, client_id) FROM stdin;
d598af07-bbab-44f0-9ba2-94cd58f4ecdf	2021-10-06	CNA	USD	2350.00	Tried contacting.	1b6f00a6-dec7-4766-be71-2ce630eb2df5
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-10-06 12:18:04.420674-07	1	root	2	[{"changed": {"fields": ["Programs", "Is office", "Is recruit", "Is instructor"]}}]	14	1
2	2021-10-06 12:18:17.117075-07	1	root@localhost	1	[{"added": {}}]	9	1
3	2021-10-06 12:19:23.890642-07	2	n.liang	1	[{"added": {}}]	14	1
4	2021-10-06 12:19:37.294881-07	2	n.liang	2	[{"changed": {"fields": ["Is recruit"]}}]	14	1
5	2021-10-06 12:19:57.758216-07	2	recruit@st-inst.com	1	[{"added": {}}]	9	1
6	2021-10-06 12:21:12.706995-07	3	k.di	1	[{"added": {}}]	14	1
7	2021-10-06 12:24:07.657915-07	2	n.liang	2	[{"changed": {"fields": ["password"]}}]	14	1
8	2021-10-06 12:24:25.349997-07	3	selecttherapyinstitute@gmail.com	1	[{"added": {}}]	9	1
9	2021-10-06 12:25:03.559219-07	4	k.ren	1	[{"added": {}}]	14	1
10	2021-10-06 12:25:15.460231-07	4	admin@st-inst.com	1	[{"added": {}}]	9	1
11	2021-10-06 12:27:01.877388-07	5	c.lara	1	[{"added": {}}]	14	1
12	2021-10-06 12:27:09.156202-07	5	c.lara	2	[]	14	1
13	2021-10-06 12:27:45.038198-07	6	p.curby	1	[{"added": {}}]	14	1
14	2021-10-06 12:28:18.389375-07	5	christianm.lara@gmail.com	1	[{"added": {}}]	9	1
15	2021-10-06 12:28:35.211801-07	6	ancamndza@gmail.com	1	[{"added": {}}]	9	1
16	2021-10-06 12:31:22.381005-07	0c805318-7706-405e-a66c-5936062617a5	STI	1	[{"added": {}}]	17	1
17	2021-10-06 12:31:43.516884-07	67301e14-cd3d-493a-a2cf-84d8c490c0ef	CNA	1	[{"added": {}}]	15	1
18	2021-10-06 12:31:58.376585-07	0af7e2ff-1370-43fb-8bd8-6f4623ecc496	HHA	1	[{"added": {}}]	15	1
19	2021-10-06 12:49:52.666893-07	fcd1f629-6449-4672-8dc8-4a2183cc70e9	CNA Rotation# 1	1	[{"added": {}}]	16	1
20	2021-10-06 12:50:16.744047-07	4481466a-7bb3-4ccc-8a51-52f4a534dd4a	HHA Rotation# 1	1	[{"added": {}}]	16	1
21	2021-10-06 14:45:44.279575-07	90f120c5-1894-4afc-b204-a912172570a5	test_a	1	[{"added": {}}]	18	1
22	2021-10-06 14:55:24.947002-07	db7d3163-7856-4b61-b242-65ef034c4bfe	test_b	1	[{"added": {}}]	18	1
23	2021-10-06 14:56:27.045575-07	90f120c5-1894-4afc-b204-a912172570a5	test_a	2	[]	18	1
24	2021-10-06 14:56:45.096684-07	db7d3163-7856-4b61-b242-65ef034c4bfe	test_b	2	[]	18	1
25	2021-10-06 14:59:15.944449-07	1b6f00a6-dec7-4766-be71-2ce630eb2df5	Testclient A	1	[{"added": {}}]	19	1
26	2021-10-06 15:01:06.277371-07	d598af07-bbab-44f0-9ba2-94cd58f4ecdf	d598af07-bbab-44f0-9ba2-94cd58f4ecdf	1	[{"added": {}}]	20	1
27	2021-10-06 15:29:54.414168-07	fdc7898d-80f0-4a48-9617-d205b1486066	CNA Rotation #1	1	[{"added": {}}]	24	1
28	2021-10-06 15:30:30.47669-07	f1bd7d07-2633-4650-b85f-448f54fd3789	HHA Rotation #1	1	[{"added": {}}]	26	1
29	2021-10-06 15:31:49.477298-07	ccc37087-32fa-4c26-8af8-e84619dc2e47	Test a	1	[{"added": {}}]	25	1
30	2021-10-06 15:32:51.33112-07	d4125d1a-56af-4522-846d-dd09cff85162	Test b	1	[{"added": {}}]	27	1
31	2021-10-06 15:35:29.758458-07	075a3e5d-6ad7-44db-a47e-294ae38895dd	075a3e5d-6ad7-44db-a47e-294ae38895dd	1	[{"added": {}}]	30	1
32	2021-10-06 15:36:01.425808-07	5f6eec84-6e5d-46ba-93c6-c34e98c2530a	5f6eec84-6e5d-46ba-93c6-c34e98c2530a	1	[{"added": {}}]	31	1
33	2021-10-06 15:37:50.192383-07	b7b559e8-035c-4329-91c7-8800115fc2e6	b7b559e8-035c-4329-91c7-8800115fc2e6	1	[{"added": {}}]	28	1
34	2021-10-06 15:38:28.263788-07	08d594c5-2a3e-49ce-93d5-1551d4f86ebd	08d594c5-2a3e-49ce-93d5-1551d4f86ebd	1	[{"added": {}}]	29	1
35	2021-10-07 08:43:52.161317-07	7	p.hu	1	[{"added": {}}]	14	1
36	2021-10-07 08:44:09.499235-07	7	support@st-inst.com	1	[{"added": {}}]	9	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	authtoken	token
2	authtoken	tokenproxy
3	admin	logentry
4	auth	permission
5	auth	group
6	contenttypes	contenttype
7	sessions	session
8	sites	site
9	account	emailaddress
10	account	emailconfirmation
11	socialaccount	socialaccount
12	socialaccount	socialapp
13	socialaccount	socialtoken
14	authentication	account
15	sms	program
16	sms	rotation
17	sms	school
18	sms	student
19	cms	client
20	cms	note
21	gms	baserecord
22	gms	baserotation
23	gms	basestudent
24	gms	cnarotation
25	gms	cnastudent
26	gms	hharotation
27	gms	hhastudent
28	gms	hhatheoryrecord
29	gms	hhaclinicalrecord
30	gms	cnatheoryrecord
31	gms	cnaclinicalrecord
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-10-06 12:17:19.735876-07
2	contenttypes	0002_remove_content_type_name	2021-10-06 12:17:19.773973-07
3	auth	0001_initial	2021-10-06 12:17:19.821403-07
4	auth	0002_alter_permission_name_max_length	2021-10-06 12:17:19.827542-07
5	auth	0003_alter_user_email_max_length	2021-10-06 12:17:19.834169-07
6	auth	0004_alter_user_username_opts	2021-10-06 12:17:19.842139-07
7	auth	0005_alter_user_last_login_null	2021-10-06 12:17:19.849921-07
8	auth	0006_require_contenttypes_0002	2021-10-06 12:17:19.853232-07
9	auth	0007_alter_validators_add_error_messages	2021-10-06 12:17:19.861538-07
10	auth	0008_alter_user_username_max_length	2021-10-06 12:17:19.870092-07
11	auth	0009_alter_user_last_name_max_length	2021-10-06 12:17:19.878555-07
12	auth	0010_alter_group_name_max_length	2021-10-06 12:17:19.890306-07
13	auth	0011_update_proxy_permissions	2021-10-06 12:17:19.898936-07
14	auth	0012_alter_user_first_name_max_length	2021-10-06 12:17:19.909216-07
15	authentication	0001_initial	2021-10-06 12:17:19.992872-07
16	account	0001_initial	2021-10-06 12:17:20.062311-07
17	account	0002_email_max_length	2021-10-06 12:17:20.083569-07
18	account	0003_auto_20210921_1732	2021-10-06 12:17:20.18178-07
19	admin	0001_initial	2021-10-06 12:17:20.234759-07
20	admin	0002_logentry_remove_auto_add	2021-10-06 12:17:20.254862-07
21	admin	0003_logentry_add_action_flag_choices	2021-10-06 12:17:20.273772-07
22	authtoken	0001_initial	2021-10-06 12:17:20.306178-07
23	authtoken	0002_auto_20160226_1747	2021-10-06 12:17:20.360085-07
24	authtoken	0003_tokenproxy	2021-10-06 12:17:20.366153-07
25	cms	0001_initial	2021-10-06 12:17:20.402738-07
26	gms	0001_initial	2021-10-06 12:17:20.5992-07
27	sessions	0001_initial	2021-10-06 12:17:20.622127-07
28	sites	0001_initial	2021-10-06 12:17:20.633278-07
29	sites	0002_alter_domain_unique	2021-10-06 12:17:20.65026-07
30	sms	0001_initial	2021-10-06 12:17:20.736526-07
31	socialaccount	0001_initial	2021-10-06 12:17:20.856068-07
32	socialaccount	0002_token_max_lengths	2021-10-06 12:17:20.892722-07
33	socialaccount	0003_extra_data_default_dict	2021-10-06 12:17:20.910752-07
34	socialaccount	0004_auto_20210928_0619	2021-10-06 12:17:21.085339-07
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
xuan8f5mi2sztvlqe7a7abj526j06btd	.eJxVjMEOgyAQRP-Fc2Ok4OL2Vn_ELMsSSA0mBU9N_73aeGiP82bmvdRMW0vzVuU556BuSqvLL_PEDylHQcty4I6Y16207rs569rd9ySlZaaW1zKdrz9Vopp2D8bg_RBh1FdvBBhMBAEMLOSCkQBEiDbYgWH0vQMepNdotXboGEHU-wPixDzK:1mYFZj:j5xpNvYgr00zG41z85ae_6H0brEm3vLAUEIIYf2zkmo	2021-10-20 15:39:47.108439-07
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: gms_baserecord; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_baserecord (id, date, completed) FROM stdin;
1	2021-10-06	t
2	2021-10-06	t
3	2021-10-06	t
4	2021-10-06	t
\.


--
-- Data for Name: gms_baserotation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_baserotation (rotation_uuid, school_name, start_date, end_date, instructor_email) FROM stdin;
fdc7898d-80f0-4a48-9617-d205b1486066	STI	2021-10-06	2021-12-30	ancamndza@gmail.com
f1bd7d07-2633-4650-b85f-448f54fd3789	STI	2021-10-06	2021-12-30	christianm.lara@gmail.com
\.


--
-- Data for Name: gms_basestudent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_basestudent (student_uuid, first_name, last_name, makeup_student) FROM stdin;
ccc37087-32fa-4c26-8af8-e84619dc2e47	Test	A	f
d4125d1a-56af-4522-846d-dd09cff85162	Test	B	f
\.


--
-- Data for Name: gms_cnaclinicalrecord; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_cnaclinicalrecord (baserecord_ptr_id, cna_clinical_record_uuid, comments, performance_satisfied, topic, student_id) FROM stdin;
2	5f6eec84-6e5d-46ba-93c6-c34e98c2530a		t	Mouth care of the unconscious resident	ccc37087-32fa-4c26-8af8-e84619dc2e47
\.


--
-- Data for Name: gms_cnarotation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_cnarotation (baserotation_ptr_id, rotation_num, instructor_title, clinical_site) FROM stdin;
fdc7898d-80f0-4a48-9617-d205b1486066	1	LVN	Rowland
\.


--
-- Data for Name: gms_cnastudent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_cnastudent (basestudent_ptr_id, rotation_id) FROM stdin;
ccc37087-32fa-4c26-8af8-e84619dc2e47	fdc7898d-80f0-4a48-9617-d205b1486066
\.


--
-- Data for Name: gms_cnatheoryrecord; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_cnatheoryrecord (baserecord_ptr_id, cna_theory_record_uuid, hours_spent, test_score, topic, student_id) FROM stdin;
1	075a3e5d-6ad7-44db-a47e-294ae38895dd	1	75	Module 2 Quiz	ccc37087-32fa-4c26-8af8-e84619dc2e47
\.


--
-- Data for Name: gms_hhaclinicalrecord; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_hhaclinicalrecord (baserecord_ptr_id, hha_clinical_record_uuid, hours_spent, comments, performance_satisfied, start_time, end_time, start_date, end_date, topic, student_id) FROM stdin;
4	08d594c5-2a3e-49ce-93d5-1551d4f86ebd	2		t	22:38:07	00:00:00	2021-10-05	2021-10-06	Nutrition	d4125d1a-56af-4522-846d-dd09cff85162
\.


--
-- Data for Name: gms_hharotation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_hharotation (baserotation_ptr_id, rotation_num, instructor_title, clinical_site) FROM stdin;
f1bd7d07-2633-4650-b85f-448f54fd3789	1	LVN	Rowland
\.


--
-- Data for Name: gms_hhastudent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_hhastudent (basestudent_ptr_id, rotation_id) FROM stdin;
d4125d1a-56af-4522-846d-dd09cff85162	f1bd7d07-2633-4650-b85f-448f54fd3789
\.


--
-- Data for Name: gms_hhatheoryrecord; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gms_hhatheoryrecord (baserecord_ptr_id, hha_theory_record_uuid, start_time, end_time, hours_spent, test_score, topic, student_id) FROM stdin;
3	b7b559e8-035c-4329-91c7-8800115fc2e6	22:36:21	00:00:00	2	40	Personal Care Services	d4125d1a-56af-4522-846d-dd09cff85162
\.


--
-- Data for Name: sms_program; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sms_program (program_uuid, program_name, approval_entities, school_id) FROM stdin;
67301e14-cd3d-493a-a2cf-84d8c490c0ef	CNA	{CDPH,BPPE}	0c805318-7706-405e-a66c-5936062617a5
0af7e2ff-1370-43fb-8bd8-6f4623ecc496	HHA	{CDPH,BPPE}	0c805318-7706-405e-a66c-5936062617a5
\.


--
-- Data for Name: sms_rotation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sms_rotation (rotation_uuid, rotation_number, program_id) FROM stdin;
fcd1f629-6449-4672-8dc8-4a2183cc70e9	1	67301e14-cd3d-493a-a2cf-84d8c490c0ef
4481466a-7bb3-4ccc-8a51-52f4a534dd4a	1	0af7e2ff-1370-43fb-8bd8-6f4623ecc496
\.


--
-- Data for Name: sms_school; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sms_school (school_uuid, school_name, school_code, school_address, year_founded) FROM stdin;
0c805318-7706-405e-a66c-5936062617a5	STI	27091740	2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770	2009-03-05
\.


--
-- Data for Name: sms_student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sms_student (student_uuid, student_id, first_name, last_name, phone_number, email, mailing_address, course, start_date, completion_date, date_enrollment_agreement_signed, third_party_payer_info, course_cost_currency, course_cost, total_charges_charged_currency, total_charges_charged, total_charges_paid_currency, total_charges_paid, paid, graduated, passed_first_exam, passed_second_or_third_exam, employed, place_of_employment, employment_address, "position", starting_wage_currency, starting_wage, hours_worked_weekly, description_of_attempts_to_contact_student, google_sheet_migrated, google_sheet_migration_issue, rotation_id) FROM stdin;
90f120c5-1894-4afc-b204-a912172570a5	01-1006-TA	Test	A	626-323-1414	testa@email.com	1020 S. Fake Ave, TestA, CA 91770	CNA	2021-10-06	2021-12-30	2021-10-06		USD	2350.00	USD	2350.00	USD	2350.00	t	f	f	f	f				USD	\N			f		fcd1f629-6449-4672-8dc8-4a2183cc70e9
db7d3163-7856-4b61-b242-65ef034c4bfe	01-1006-TB	Test	B	626-333-5544	testb@email.com	1300 N. Fake Ave, TestB, CA 91888	HHA	2021-10-06	2021-12-10	2021-10-06		USD	680.00	USD	680.00	USD	600.00	f	f	f	f	f				USD	\N			f		4481466a-7bb3-4ccc-8a51-52f4a534dd4a
\.


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialaccount (id, provider, uid, last_login, date_joined, extra_data, user_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialapp (id, provider, name, client_id, secret, key) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialapp_sites (id, socialapp_id, site_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialtoken (id, token, token_secret, expires_at, account_id, app_id) FROM stdin;
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 7, true);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 124, true);


--
-- Name: authentication_account_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authentication_account_groups_id_seq', 1, false);


--
-- Name: authentication_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authentication_account_id_seq', 7, true);


--
-- Name: authentication_account_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authentication_account_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 36, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 31, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 34, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: gms_baserecord_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.gms_baserecord_id_seq', 4, true);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- Name: account_emailaddress account_emailaddress_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_email_key UNIQUE (email);


--
-- Name: account_emailaddress account_emailaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id);


--
-- Name: account_emailconfirmation account_emailconfirmation_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_key_key UNIQUE (key);


--
-- Name: account_emailconfirmation account_emailconfirmation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authentication_account authentication_account_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account
    ADD CONSTRAINT authentication_account_email_key UNIQUE (email);


--
-- Name: authentication_account_groups authentication_account_groups_account_id_group_id_7b343099_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_groups
    ADD CONSTRAINT authentication_account_groups_account_id_group_id_7b343099_uniq UNIQUE (account_id, group_id);


--
-- Name: authentication_account_groups authentication_account_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_groups
    ADD CONSTRAINT authentication_account_groups_pkey PRIMARY KEY (id);


--
-- Name: authentication_account authentication_account_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account
    ADD CONSTRAINT authentication_account_pkey PRIMARY KEY (id);


--
-- Name: authentication_account_user_permissions authentication_account_u_account_id_permission_id_cc8410e2_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_user_permissions
    ADD CONSTRAINT authentication_account_u_account_id_permission_id_cc8410e2_uniq UNIQUE (account_id, permission_id);


--
-- Name: authentication_account_user_permissions authentication_account_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_user_permissions
    ADD CONSTRAINT authentication_account_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: authentication_account authentication_account_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account
    ADD CONSTRAINT authentication_account_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: cms_client cms_client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cms_client
    ADD CONSTRAINT cms_client_pkey PRIMARY KEY (client_uuid);


--
-- Name: cms_note cms_note_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cms_note
    ADD CONSTRAINT cms_note_pkey PRIMARY KEY (note_uuid);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: gms_baserecord gms_baserecord_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_baserecord
    ADD CONSTRAINT gms_baserecord_pkey PRIMARY KEY (id);


--
-- Name: gms_baserotation gms_baserotation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_baserotation
    ADD CONSTRAINT gms_baserotation_pkey PRIMARY KEY (rotation_uuid);


--
-- Name: gms_basestudent gms_basestudent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_basestudent
    ADD CONSTRAINT gms_basestudent_pkey PRIMARY KEY (student_uuid);


--
-- Name: gms_cnaclinicalrecord gms_cnaclinicalrecord_baserecord_ptr_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnaclinicalrecord
    ADD CONSTRAINT gms_cnaclinicalrecord_baserecord_ptr_id_key UNIQUE (baserecord_ptr_id);


--
-- Name: gms_cnaclinicalrecord gms_cnaclinicalrecord_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnaclinicalrecord
    ADD CONSTRAINT gms_cnaclinicalrecord_pkey PRIMARY KEY (cna_clinical_record_uuid);


--
-- Name: gms_cnarotation gms_cnarotation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnarotation
    ADD CONSTRAINT gms_cnarotation_pkey PRIMARY KEY (baserotation_ptr_id);


--
-- Name: gms_cnarotation gms_cnarotation_rotation_num_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnarotation
    ADD CONSTRAINT gms_cnarotation_rotation_num_key UNIQUE (rotation_num);


--
-- Name: gms_cnastudent gms_cnastudent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnastudent
    ADD CONSTRAINT gms_cnastudent_pkey PRIMARY KEY (basestudent_ptr_id);


--
-- Name: gms_cnatheoryrecord gms_cnatheoryrecord_baserecord_ptr_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnatheoryrecord
    ADD CONSTRAINT gms_cnatheoryrecord_baserecord_ptr_id_key UNIQUE (baserecord_ptr_id);


--
-- Name: gms_cnatheoryrecord gms_cnatheoryrecord_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnatheoryrecord
    ADD CONSTRAINT gms_cnatheoryrecord_pkey PRIMARY KEY (cna_theory_record_uuid);


--
-- Name: gms_hhaclinicalrecord gms_hhaclinicalrecord_baserecord_ptr_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhaclinicalrecord
    ADD CONSTRAINT gms_hhaclinicalrecord_baserecord_ptr_id_key UNIQUE (baserecord_ptr_id);


--
-- Name: gms_hhaclinicalrecord gms_hhaclinicalrecord_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhaclinicalrecord
    ADD CONSTRAINT gms_hhaclinicalrecord_pkey PRIMARY KEY (hha_clinical_record_uuid);


--
-- Name: gms_hharotation gms_hharotation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hharotation
    ADD CONSTRAINT gms_hharotation_pkey PRIMARY KEY (baserotation_ptr_id);


--
-- Name: gms_hharotation gms_hharotation_rotation_num_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hharotation
    ADD CONSTRAINT gms_hharotation_rotation_num_key UNIQUE (rotation_num);


--
-- Name: gms_hhastudent gms_hhastudent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhastudent
    ADD CONSTRAINT gms_hhastudent_pkey PRIMARY KEY (basestudent_ptr_id);


--
-- Name: gms_hhatheoryrecord gms_hhatheoryrecord_baserecord_ptr_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhatheoryrecord
    ADD CONSTRAINT gms_hhatheoryrecord_baserecord_ptr_id_key UNIQUE (baserecord_ptr_id);


--
-- Name: gms_hhatheoryrecord gms_hhatheoryrecord_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhatheoryrecord
    ADD CONSTRAINT gms_hhatheoryrecord_pkey PRIMARY KEY (hha_theory_record_uuid);


--
-- Name: sms_program sms_program_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_program
    ADD CONSTRAINT sms_program_pkey PRIMARY KEY (program_uuid);


--
-- Name: sms_rotation sms_rotation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_rotation
    ADD CONSTRAINT sms_rotation_pkey PRIMARY KEY (rotation_uuid);


--
-- Name: sms_school sms_school_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_school
    ADD CONSTRAINT sms_school_pkey PRIMARY KEY (school_uuid);


--
-- Name: sms_student sms_student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_student
    ADD CONSTRAINT sms_student_pkey PRIMARY KEY (student_uuid);


--
-- Name: sms_student sms_student_student_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_student
    ADD CONSTRAINT sms_student_student_id_key UNIQUE (student_id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_provider_uid_fc810c6e_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_provider_uid_fc810c6e_uniq UNIQUE (provider, uid);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq UNIQUE (socialapp_id, site_id);


--
-- Name: socialaccount_socialapp socialaccount_socialapp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp
    ADD CONSTRAINT socialaccount_socialapp_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp_sites_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq UNIQUE (app_id, account_id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_pkey PRIMARY KEY (id);


--
-- Name: account_emailaddress_email_03be32b2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_email_03be32b2_like ON public.account_emailaddress USING btree (email varchar_pattern_ops);


--
-- Name: account_emailaddress_user_id_2c513194; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_user_id_2c513194 ON public.account_emailaddress USING btree (user_id);


--
-- Name: account_emailconfirmation_email_address_id_5b7f8c58; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_email_address_id_5b7f8c58 ON public.account_emailconfirmation USING btree (email_address_id);


--
-- Name: account_emailconfirmation_key_f43612bd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_key_f43612bd_like ON public.account_emailconfirmation USING btree (key varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authentication_account_email_04383543_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_account_email_04383543_like ON public.authentication_account USING btree (email varchar_pattern_ops);


--
-- Name: authentication_account_groups_account_id_caf1df9b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_account_groups_account_id_caf1df9b ON public.authentication_account_groups USING btree (account_id);


--
-- Name: authentication_account_groups_group_id_b50264dd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_account_groups_group_id_b50264dd ON public.authentication_account_groups USING btree (group_id);


--
-- Name: authentication_account_user_permissions_account_id_f54c8acd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_account_user_permissions_account_id_f54c8acd ON public.authentication_account_user_permissions USING btree (account_id);


--
-- Name: authentication_account_user_permissions_permission_id_0cd35b44; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_account_user_permissions_permission_id_0cd35b44 ON public.authentication_account_user_permissions USING btree (permission_id);


--
-- Name: authentication_account_username_a7bddf07_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_account_username_a7bddf07_like ON public.authentication_account USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: cms_note_client_id_0d48fdc7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX cms_note_client_id_0d48fdc7 ON public.cms_note USING btree (client_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: gms_cnaclinicalrecord_student_id_2362bc24; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX gms_cnaclinicalrecord_student_id_2362bc24 ON public.gms_cnaclinicalrecord USING btree (student_id);


--
-- Name: gms_cnastudent_rotation_id_acb48d03; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX gms_cnastudent_rotation_id_acb48d03 ON public.gms_cnastudent USING btree (rotation_id);


--
-- Name: gms_cnatheoryrecord_student_id_97d37348; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX gms_cnatheoryrecord_student_id_97d37348 ON public.gms_cnatheoryrecord USING btree (student_id);


--
-- Name: gms_hhaclinicalrecord_student_id_0d71d051; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX gms_hhaclinicalrecord_student_id_0d71d051 ON public.gms_hhaclinicalrecord USING btree (student_id);


--
-- Name: gms_hhastudent_rotation_id_81f0cc2e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX gms_hhastudent_rotation_id_81f0cc2e ON public.gms_hhastudent USING btree (rotation_id);


--
-- Name: gms_hhatheoryrecord_student_id_f7834b67; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX gms_hhatheoryrecord_student_id_f7834b67 ON public.gms_hhatheoryrecord USING btree (student_id);


--
-- Name: sms_program_school_id_092aa9bd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sms_program_school_id_092aa9bd ON public.sms_program USING btree (school_id);


--
-- Name: sms_rotation_program_id_980ca011; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sms_rotation_program_id_980ca011 ON public.sms_rotation USING btree (program_id);


--
-- Name: sms_student_rotation_id_e8fd2073; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sms_student_rotation_id_e8fd2073 ON public.sms_student USING btree (rotation_id);


--
-- Name: sms_student_student_id_11373a2a_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sms_student_student_id_11373a2a_like ON public.sms_student USING btree (student_id varchar_pattern_ops);


--
-- Name: socialaccount_socialaccount_user_id_8146e70c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialaccount_user_id_8146e70c ON public.socialaccount_socialaccount USING btree (user_id);


--
-- Name: socialaccount_socialapp_sites_site_id_2579dee5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialapp_sites_site_id_2579dee5 ON public.socialaccount_socialapp_sites USING btree (site_id);


--
-- Name: socialaccount_socialapp_sites_socialapp_id_97fb6e7d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialapp_sites_socialapp_id_97fb6e7d ON public.socialaccount_socialapp_sites USING btree (socialapp_id);


--
-- Name: socialaccount_socialtoken_account_id_951f210e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialtoken_account_id_951f210e ON public.socialaccount_socialtoken USING btree (account_id);


--
-- Name: socialaccount_socialtoken_app_id_636a42d7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialtoken_app_id_636a42d7 ON public.socialaccount_socialtoken USING btree (app_id);


--
-- Name: account_emailaddress account_emailaddress_user_id_2c513194_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_2c513194_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emailconfirmation account_emailconfirmation_email_address_id_5b7f8c58_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_email_address_id_5b7f8c58_fk FOREIGN KEY (email_address_id) REFERENCES public.account_emailaddress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_account_groups authentication_accou_account_id_caf1df9b_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_groups
    ADD CONSTRAINT authentication_accou_account_id_caf1df9b_fk_authentic FOREIGN KEY (account_id) REFERENCES public.authentication_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_account_user_permissions authentication_accou_account_id_f54c8acd_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_user_permissions
    ADD CONSTRAINT authentication_accou_account_id_f54c8acd_fk_authentic FOREIGN KEY (account_id) REFERENCES public.authentication_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_account_groups authentication_accou_group_id_b50264dd_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_groups
    ADD CONSTRAINT authentication_accou_group_id_b50264dd_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_account_user_permissions authentication_accou_permission_id_0cd35b44_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_account_user_permissions
    ADD CONSTRAINT authentication_accou_permission_id_0cd35b44_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_authentication_account_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_authentication_account_id FOREIGN KEY (user_id) REFERENCES public.authentication_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cms_note cms_note_client_id_0d48fdc7_fk_cms_client_client_uuid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cms_note
    ADD CONSTRAINT cms_note_client_id_0d48fdc7_fk_cms_client_client_uuid FOREIGN KEY (client_id) REFERENCES public.cms_client(client_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_authentication_account_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_authentication_account_id FOREIGN KEY (user_id) REFERENCES public.authentication_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnaclinicalrecord gms_cnaclinicalrecor_baserecord_ptr_id_b58740bf_fk_gms_baser; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnaclinicalrecord
    ADD CONSTRAINT gms_cnaclinicalrecor_baserecord_ptr_id_b58740bf_fk_gms_baser FOREIGN KEY (baserecord_ptr_id) REFERENCES public.gms_baserecord(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnaclinicalrecord gms_cnaclinicalrecor_student_id_2362bc24_fk_gms_cnast; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnaclinicalrecord
    ADD CONSTRAINT gms_cnaclinicalrecor_student_id_2362bc24_fk_gms_cnast FOREIGN KEY (student_id) REFERENCES public.gms_cnastudent(basestudent_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnarotation gms_cnarotation_baserotation_ptr_id_4eb5f2be_fk_gms_baser; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnarotation
    ADD CONSTRAINT gms_cnarotation_baserotation_ptr_id_4eb5f2be_fk_gms_baser FOREIGN KEY (baserotation_ptr_id) REFERENCES public.gms_baserotation(rotation_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnastudent gms_cnastudent_basestudent_ptr_id_6cd44926_fk_gms_bases; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnastudent
    ADD CONSTRAINT gms_cnastudent_basestudent_ptr_id_6cd44926_fk_gms_bases FOREIGN KEY (basestudent_ptr_id) REFERENCES public.gms_basestudent(student_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnastudent gms_cnastudent_rotation_id_acb48d03_fk_gms_cnaro; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnastudent
    ADD CONSTRAINT gms_cnastudent_rotation_id_acb48d03_fk_gms_cnaro FOREIGN KEY (rotation_id) REFERENCES public.gms_cnarotation(baserotation_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnatheoryrecord gms_cnatheoryrecord_baserecord_ptr_id_dfc4e66f_fk_gms_baser; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnatheoryrecord
    ADD CONSTRAINT gms_cnatheoryrecord_baserecord_ptr_id_dfc4e66f_fk_gms_baser FOREIGN KEY (baserecord_ptr_id) REFERENCES public.gms_baserecord(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_cnatheoryrecord gms_cnatheoryrecord_student_id_97d37348_fk_gms_cnast; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_cnatheoryrecord
    ADD CONSTRAINT gms_cnatheoryrecord_student_id_97d37348_fk_gms_cnast FOREIGN KEY (student_id) REFERENCES public.gms_cnastudent(basestudent_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hhaclinicalrecord gms_hhaclinicalrecor_baserecord_ptr_id_184dda28_fk_gms_baser; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhaclinicalrecord
    ADD CONSTRAINT gms_hhaclinicalrecor_baserecord_ptr_id_184dda28_fk_gms_baser FOREIGN KEY (baserecord_ptr_id) REFERENCES public.gms_baserecord(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hhaclinicalrecord gms_hhaclinicalrecor_student_id_0d71d051_fk_gms_hhast; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhaclinicalrecord
    ADD CONSTRAINT gms_hhaclinicalrecor_student_id_0d71d051_fk_gms_hhast FOREIGN KEY (student_id) REFERENCES public.gms_hhastudent(basestudent_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hharotation gms_hharotation_baserotation_ptr_id_43b42e66_fk_gms_baser; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hharotation
    ADD CONSTRAINT gms_hharotation_baserotation_ptr_id_43b42e66_fk_gms_baser FOREIGN KEY (baserotation_ptr_id) REFERENCES public.gms_baserotation(rotation_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hhastudent gms_hhastudent_basestudent_ptr_id_ec5de18c_fk_gms_bases; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhastudent
    ADD CONSTRAINT gms_hhastudent_basestudent_ptr_id_ec5de18c_fk_gms_bases FOREIGN KEY (basestudent_ptr_id) REFERENCES public.gms_basestudent(student_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hhastudent gms_hhastudent_rotation_id_81f0cc2e_fk_gms_hharo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhastudent
    ADD CONSTRAINT gms_hhastudent_rotation_id_81f0cc2e_fk_gms_hharo FOREIGN KEY (rotation_id) REFERENCES public.gms_hharotation(baserotation_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hhatheoryrecord gms_hhatheoryrecord_baserecord_ptr_id_629e6131_fk_gms_baser; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhatheoryrecord
    ADD CONSTRAINT gms_hhatheoryrecord_baserecord_ptr_id_629e6131_fk_gms_baser FOREIGN KEY (baserecord_ptr_id) REFERENCES public.gms_baserecord(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gms_hhatheoryrecord gms_hhatheoryrecord_student_id_f7834b67_fk_gms_hhast; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gms_hhatheoryrecord
    ADD CONSTRAINT gms_hhatheoryrecord_student_id_f7834b67_fk_gms_hhast FOREIGN KEY (student_id) REFERENCES public.gms_hhastudent(basestudent_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sms_program sms_program_school_id_092aa9bd_fk_sms_school_school_uuid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_program
    ADD CONSTRAINT sms_program_school_id_092aa9bd_fk_sms_school_school_uuid FOREIGN KEY (school_id) REFERENCES public.sms_school(school_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sms_rotation sms_rotation_program_id_980ca011_fk_sms_program_program_uuid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_rotation
    ADD CONSTRAINT sms_rotation_program_id_980ca011_fk_sms_program_program_uuid FOREIGN KEY (program_id) REFERENCES public.sms_program(program_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sms_student sms_student_rotation_id_e8fd2073_fk_sms_rotation_rotation_uuid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sms_student
    ADD CONSTRAINT sms_student_rotation_id_e8fd2073_fk_sms_rotation_rotation_uuid FOREIGN KEY (rotation_id) REFERENCES public.sms_rotation(rotation_uuid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialapp_sites socialaccount_social_site_id_2579dee5_fk_django_si; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_site_id_2579dee5_fk_django_si FOREIGN KEY (site_id) REFERENCES public.django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialaccount socialaccount_social_user_id_8146e70c_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_social_user_id_8146e70c_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_account_id_951f210e_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_account_id_951f210e_fk FOREIGN KEY (account_id) REFERENCES public.socialaccount_socialaccount(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_app_id_636a42d7_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_636a42d7_fk FOREIGN KEY (app_id) REFERENCES public.socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

