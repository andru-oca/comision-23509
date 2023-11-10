def delete_user(dni:str,db:list[dict]=None)->None:
    if db is None:
        print("che, noru, no me pasaste una db")
        return None


    # db = [
    #     user
    #     for user in db
    #     if user["dni"] != dni
    # ]


    for index,user in enumerate(db):
        if user["dni"] == dni:
            db.pop(index)

    print(id(db))
    print(len(db))
