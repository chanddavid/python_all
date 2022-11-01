# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from hashlib import new
import pandas as pd
import regex as re


data = [
    {
        'key_as_string': '2022-08-01',
        'key': 1659291300000,
        'doc_count': 69,
        'referrer': {
            'doc_count_error_upper_bound': 0,
            'sum_other_doc_count': 2,
            'buckets': [
                {
                    'key': 'https://ekbana.com/',
                    'doc_count': 39

                },
                {
                    'key': 'https://www.google.com/',
                    'doc_count': 11

                },
                {
                    'key': 'https://careers.ekbana.com/thankyou',
                    'doc_count': 4

                },
            ]
        }

    },
    {
        'key_as_string': '2022-08-02',
        'key': 1659291300000,
        'doc_count': 69,
        'referrer': {
            'doc_count_error_upper_bound': 0,
            'sum_other_doc_count': 2,
            'buckets': [
                {
                    'key': 'https://ekbana.com/',
                    'doc_count': 30

                },
                {
                    'key': 'https://www.google.com/',
                    'doc_count': 10

                },
                {
                    'key': 'https://careers.ekbana.com/thankyou',
                    'doc_count': 5

                },
            ]
        }

    }]



pattern = "(\w|-)+(?=(\.(com|net|org|info|coop|int|co|ac|ie|co|ai|eu|ca|icu|top|xyz|tk|cn|ga|cf|nl|us|eu" \
                       "|de|hk|am|tv|bingo|blackfriday|gov|edu|mil|arpa|au|it|ru)(\.|\/|$)))"

def myfunc(str):
    if str == "":
        return ""
    txt = re.search(pattern=pattern, string=str)
    if txt is None:
        return float("NaN")
    else:
        return 'twitter' if txt[0] == 't' else txt[0]

lst = []
newlst = []

for i in data:
    for j in i['referrer']['buckets']:
        lst.append(
            {

                "referrer": myfunc(j["key"]),
                "count": j["doc_count"]
            })

for i in data:
    newlst.append(
        {
            "date": i['key_as_string'],
            "referrer": [k for k in lst]

        })

conlist=[]
for dict in lst:
    for i in dict:
        if i in conlist:
            conlist[i]+=(lst[i])
        else:
            conlist[i]=lst[i]
        print(i)
print(lst)
