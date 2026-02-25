def solution(id_pw, db):
    check_id = 0
        
    for db_id, db_pw in db:
        if db_id == id_pw[0]:
            check_id = 1
            if db_pw == id_pw[1]:
                return "login"
        
    return "wrong pw" if check_id else "fail"