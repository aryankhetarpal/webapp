from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://k0r42n1ui68mru88e9yv:pscale_pw_vJFV7hrxSYdDlANkVPD39WnE4kusABheaEAaFgpSvPC@aws.connect.psdb.cloud/webapp?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def add_to_db(data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO shiftenter (full_name, shift_start, shift_end, picture) VALUES (:full_name, :shift_start, :shift_end, :picture)"
        ).bindparams(
            full_name=data["full_name"],
            shift_start=data["shift_start"],
            shift_end=data["shift_end"],
            picture=data["picture"]
        )
        conn.execute(query)


