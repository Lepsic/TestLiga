from app.db import connection as connect

query = """
CREATE TABLE photo(
    id UUID PRIMARY KEY, 
    source VARCHAR(255),
    date DATE DEFAULT now(),
    intruder INTEGER
);

CREATE TABLE attribute(
    id UUID PRIMARY KEY,
    type VARCHAR(55) NOT NULL CHECK ( type IN ('suit', 'helmet', 'person')),
    photo_id UUID REFERENCES photo(id) NOT NULL,
    person_id UUID REFERENCES attribute(id) ON DELETE CASCADE,
    positionX INTEGER NOT NULL,
    positionY INTEGER NOT NULL, 
    confidence FLOAT CHECK ( 0<confidence<100 ) NOT NULL
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
