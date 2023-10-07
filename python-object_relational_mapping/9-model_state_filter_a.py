import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if there are enough command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <db_user> <db_password> <db_name>")
        sys.exit(1)

    # Create a database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create the database tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query states that contain the letter 'a'
        states = session.query(State)\
            .filter(State.name.like('%a%'))\
            .order_by(State.id)\
            .all()

        # Check if there are any matching records
        if states:
            for state in states:
                print("{}: {}".format(state.id, state.name))
        else:
            print("No records found containing 'a'")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the session
        session.close()
        