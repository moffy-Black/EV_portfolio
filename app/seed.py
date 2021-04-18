def detail(users_by_name):
    detail_list = []
    for key in users_by_name.keys():
        detail = db.child("companies").child(key).get().val()
        detail_list.append(detail)
    return detail_list
