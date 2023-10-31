from app.db import connection as connect

query = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE photo(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY, 
    source VARCHAR(255),
    date DATE DEFAULT now(),
    intruder INTEGER
);

CREATE TABLE attribute(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    type VARCHAR(55) NOT NULL CHECK ( type IN ('suit', 'helmet', 'person')),
    photo_id UUID REFERENCES photo(id) NOT NULL,
    person_id UUID REFERENCES attribute(id) ON DELETE CASCADE,
    first_point POINT NOT NULL,
    second_point POINT NOT NULL, 
    confidence FLOAT CHECK ( confidence > 0 AND confidence < 100 ) NOT NULL
);
"""


async def startup():
    conn = await connect.connection()
    await conn.execute(query)
    await conn.execute("""
        CREATE OR REPLACE FUNCTION check_person_id() RETURNS TRIGGER AS $$
        BEGIN
            IF NEW.person_id IS NOT NULL AND NOT EXISTS (
                SELECT 1 FROM attribute WHERE id = NEW.person_id AND type = 'person'
            ) THEN
                RAISE EXCEPTION 'Invalid person_id';
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER check_person_id_trigger
        BEFORE INSERT OR UPDATE ON attribute
        FOR EACH ROW
        EXECUTE FUNCTION check_person_id();
    """)
