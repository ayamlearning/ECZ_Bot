import centres_db as db
import datetime


def search_centre_by_district(dist):
    records=db.search_by_district(dist)

    if len(records)<1:
        return "no records found"

    else:
        result=""
        for i in records:
            temp_result=""
            temp_result+="Constituency: "+str(i[3])+"\n"
            temp_result+="Ward: "+str(i[4])+"\n"
            temp_result+="Polling Station Name: "+str(i[6])+"\n"

            result+=temp_result+"\n"

    return result

def search_by_constituency(conts_name):

    phase=0
    now = datetime.datetime.now().date()

    if (now > datetime.datetime(2020, 11, 9).date() and now < datetime.datetime(2020, 11, 16).date()):
        phase= 1
    elif (now >= datetime.datetime(2020, 11, 17).date() and now <= datetime.datetime(2020, 11, 23).date()):
        phase= 2
    elif (now >= datetime.datetime(2020, 11, 24).date() and now <= datetime.datetime(2020, 11, 2).date()):
        phase= 3
    else:
        phase= 4

    records=db.search_constituency(conts_name,phase)

    if len(records)<1:
        return "no records found"

    else:
        result=""
        for i in records:
            temp_result=""
            temp_result+="Constituency: "+str(i[3])+"\n"
            temp_result+="Ward: "+str(i[4])+"\n"
            temp_result+="Polling Station Name: "+str(i[6])+"\n"

            result+=temp_result+"\n"

    return result

def search_centre_by_ward(ward):
    records=db.search_by_ward(ward)

    if len(records)<1:
        return "no records found"

    else:
        result=""
        for i in records:
            temp_result=""
            temp_result+="Constituency: "+str(i[3])+"\n"
            temp_result+="Ward: "+str(i[4])+"\n"
            temp_result+="Polling Station Name: "+str(i[6])+"\n"

            result+=temp_result+"\n"

    return result

def search_centre_by_constituency_and_ward(conts_name,ward_name):
    records=db.search_by_constituency_and_ward(conts_name,ward_name)

    if len(records)<1:
        return "no records found"

    else:
        result=""
        for i in records:
            temp_result=""
            temp_result+="Constituency: "+str(i[3])+"\n"
            temp_result+="Ward: "+str(i[4])+"\n"
            temp_result+="Polling Station Name: "+str(i[5])+"\n"

            result+=temp_result+"\n"

    return result


def list_constituencies():
    cons= db.get_all_constituencies()
    lst_cons=[]
    for c in cons:
        lst_cons.append(c[0].lower())

    return lst_cons

if __name__ == '__main__':
    print(list_constituencies())
