class DB:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DB, cls).__new__(cls)
        return cls.instance

db_1 = DB()
db_2 = DB()

print(db_1) 
print(db_2)