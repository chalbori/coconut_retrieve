class Database:
    host = "1.233.215.92"
    port = "27017"
    database = "COCONUTlatest"
    user_id = "swlee"
    user_password = "camd5882"
    connection_info = "mongodb://{}:{}@{}:{}/{}".format(
        user_id, user_password, host, port, database
    )