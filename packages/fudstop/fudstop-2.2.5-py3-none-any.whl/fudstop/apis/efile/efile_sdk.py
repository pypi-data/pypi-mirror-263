import requests
from .case_models.models import Events
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
case1 = os.environ.get('case1')
case2 = os.environ.get('case2')
divorce_key = os.environ.get('divorce_key')
prot_key = os.environ.get('protective_order_key')
headers = { 
    'Accept': 'application/pdf',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json;charset=UTF-8',
    "Cookie":"FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U2VjdXJpdHlDb250ZXh0VG9rZW4gcDE6SWQ9Il83NmFjODVjZS1kZjBiLTQ0NjYtYTZhOS03ZGZjMDBiNTc1ZDAtNjlFOTAyOTVDQTY2RTQ3MTExMThFODVFRTk3NUVGNDAiIHhtbG5zOnAxPSJodHRwOi8vZG9jcy5vYXNpcy1vcGVuLm9yZy93c3MvMjAwNC8wMS9vYXNpcy0yMDA0MDEtd3NzLXdzc2VjdXJpdHktdXRpbGl0eS0xLjAueHNkIiB4bWxucz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3Mtc3gvd3Mtc2VjdXJlY29udmVyc2F0aW9uLzIwMDUxMiI+PElkZW50aWZpZXI+dXJuOnV1aWQ6YTcyMjYwNzMtYWYzNC00MWQ2LWE0NDktODFmMTRkYWZjMmE3PC9JZGVudGlmaWVyPjxDb29raWUgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwNi8wNS9zZWN1cml0eSI+SjRqNGdVMUtVR3A2NU9MbTIwTFBVdVhXWjhlMEVsWGhxRUxPTE10bEZUb0ZTVjlXK2Y5UGM5RkhCYW5vY3NjK2VjajVjR0lVdVZ0TytYS1IxYzdDVEpKOUd1OFViUDY5MHhGd3RseW84NjhKK2FoR3owWTdZVFlaYkREU1B0dDkrOUw5TG9MWTAxSzBGRmNiSEVSM3BPWS9JRk5Gc2dsMHJ2U3R2RW15N082RW1weTFjVkl6SEFIdjc3ZXhjMXBkOHI0UW5BcU85bXdHTlJYbEN2MU9USVVaL2FyRURrVzUzeDcrWThNdUs3bjBCVFNYU0tIZ0w4aDV6QmozMFlsUWVMNUR4Zis1N0x4V0FQSFNydEhOdnFmb1B0d3YxWndBM2o4ZVM2bEpPaFIzOUZpVHZpOWN0VFV4SThkdVNYUThpMGRUNGxma0pEUitsd0JLS0REbmtRSzVHbzNvSXhmT0QxS2U1OFlLcHdlZnp1OW1YTVR6c3BxOUNQZis4U1htUGVmTVdNaGpoTWtaeWdjM0pyMWNXMzBlUFJHNVZuVzdoNnIybmpWODhYdWVIR3Z1Ymo1dXMyWjY5S0VhVTM5UEc2YUpXTGVEOU9vQ0Q2bWY5eEJLdzR4SGxqNUQyZ0thY1VUMnMycXJTWnRUalQvM3F3R1BUa0t3V0FEVjBKaHJoa3h4bnpybGtZK2ZyRCtnYzlRVkdzclduKzhaR1pQdGtPZEdnY0dPUEJMZjA3TDliMVhBcFU1aEpsbXBZT2R6QXlXU1lKQWxhYmNPY3VHditxZTdBQzN5ZmljbG1rNFhMYk14MDlES1Q5Y3VHVDY2Z1d4emhUNGNCaUt1SmVBTno0U0xkQTJtSXI1TlhVcE8xYkU0NVdHZCttc1Rud214eWIzTy9rc2d3UTE5bnJtcUtzUnZOelY2SmEvRWhYZUlVYkJ1Y1RRcTVtTDl3QW9semUrTUNPYlJkN0ZvNm5GQm1DV2xiZFhuOUxVUVV5OGM2c2krdjhpWHQ1UGtNSnJvRnVobFV1YVVvOXF3Q0NBS2txUmVjbjdENkFZdWMxRzZGb1gxT2Fpd0ZxdUM3MEg1YUx4RWI5eUlleCs1MTk5ZWkyTEN4Mk1FQktUM0xCVkE0V2MxOGlsQUpRcnVWVTJtdHFEYVBKYlVzL1c3ZE5EOExaZlBManNwSDd3dThuckFsTkJwUXFLcmFaOUl1dHB2VFpKTDVybjhtZ2h1YW12QUdscE5oUUt4T1RhRFpVUlFGRHVNTTF5WFJUQk9nVVBNdXMydFdGZ3EzblBYSGJHWHFEcG14UGtacGJmMTQwNDNSQ0MvQ1pzM3h2VkdMeVZqWWd6MnpzUjM4cDRNMVVROGdIRTNjdzIybjlBRVJ6MkNlWkI5MzluV09OTWc2bnBqdFBL; FedAuth1=eUVNbnpwa0JNOERkc1VhZ2IwMWh0aHVkR3Jsd1NZeU9KUVlqSjVEYXpVd1E3eFNVTFo5YnM2bXlBV1pjZC9ocEtCYVJWRHo3MTBLVlloZkM2bVhRdmQvTm9lcjcvaWhnOWRLTFdRaUlhWUg1WHpTa2EyaVgvdytoNFVzWmwxU0oydmh5ZGEwOThOT2dsSWhJSUZuelZjT1hlNmtDOWxEN1JjaUFIOHNGdlpQUC9rL0pOYXdOd0htK3RhMjNmb3pKM1ZSdjlnYUM5cWh4WUJYVVFBcENJWDY5ZGtVMDJscUh2VkJRUitsc3NocUZubVl4SU03OXBKTFRTTkpKMVVFR0VkU0d2b0pPMys3bVV1bW5UMExELy8yWEdFL1dBNEpvWjVsNVFBclJ0MWo3MWM3aENJREhUOHdHVEZBSVNuTUJPcnZ1akgvUGhJSFBQWTVoMC9pd0dFNmhKV0NpcElyL0JhZmk1ZDFOM1NpUmNrbkloUEJDcGc3Uy9zM1YydkMrL3VpZkJiQm85VVEyOWFmQjhJK2ZqWmpwNDIreGU5QmY3MlFZOEF6MlJWM21jdGcyT2NicElpSTZYRHpUWmtHOHkzQmdkOTdZQVFhRzBmckt1NlNMMDRZUDUvK1QrQmVIZHNMOXVHd1RWc2JZV0VkZWRzMldsNEVZbllQMEZabUU1OWdmWjNEbHhvVlNUSVpibi9penJLdFp2WER6cEtzdmRtcmtYNURmUVVGV3dNckoxUWVKS0xJRXQvQXY1WU9VcG16eDk4S1JPTmJkSlVIWnQ1aUVyZEtLaERiOENRRDJuLzdEWHcrOVZxVzRPd2l2YVkrbVh3eHcxc3FMUGRCeDhkM3k3N3c0aG83enpvN1RuNnFkUWtIM3NqZzZ5WE5QeldTS000L0pabXZZYTZTUzJlbUFiQ0Y1dzV1c3M0Q2VTUmdNbjRzcWlFU0xVSm0wWUFOT2dpYVZ5M2lFR1B1akQ2OERNMEtnV1o1SDdHNElpREVrVmtaa1I2MzNkajVaNnI5aUUrOGR1WnhrTVhuZHZ4bXF3aWgyaXZucUQ1aXo3ZC9zU2lFMktqeTArWnVrUWtiTE9GaVJ6czNUODdsYTJmYnI3WUhMVmNNRGIyNlRmRXdMdnMybW9DaGtXaXJXVjFqb05jRkJyQkVySmhFQ2tkUT09PC9Db29raWU+PC9TZWN1cml0eUNvbnRleHRUb2tlbj4=; _hjSessionUser_1494715=eyJpZCI6ImM3NjE1MDcwLTI4ZGItNWRjYy1hOWZiLWJhNjE5NmQ3OTFiMSIsImNyZWF0ZWQiOjE3MDk2MTA0MTI0MTMsImV4aXN0aW5nIjp0cnVlfQ==; __utma=211709392.1586994462.1705728131.1709440365.1709770285.22; __utmz=211709392.1709770285.22.20.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _hjSession_1494715=eyJpZCI6IjJmYjA4MGQ0LThjMmQtNDg3OS05ZTA3LTY4MThhNjkwOWZkOCIsImMiOjE3MTA5NjY1MTM2NzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowfQ==; IdSvr.WsFedTracking=Qsn_Un2pp5ZW70JcqJH8qaBBY1IPI5GnJJ6e64qGm6IT0QXpzrArHtOnyTxXarhVKpGrAyFEpS5PZv3doUBXGLwVTNXz-6UFTtMAJIoOYqeoOntDIrnc73Q8ciUFyS77QCe2OCZxWR9Vx0HvTb-L-By5m0mTf9IpH3mrTqaUMb2K7ojRzSz-3XjeHBvlfa-xGssNLGA5lYcFx0EKYLux1eowwYL-oy-hAwTgYJjyZ3B_lwyWf_DLxpWjB8Jf5sg-1ws84dUTmBiT-Elg3a0QlQ; logged_in=true; idle_timer=2024-03-20T20:30:14.463Z"

}
payload = {
    "pageSize": 20,
    "pageIndex": 0,

    "eventType": 0
}


def get_envelopes():
    r = requests.get("https://efiletx.tylertech.cloud/OfsEfsp/api/filinghistory/filing/widget/envelopes", headers=headers).json()
    print(r)


def get_record(case_key):
    try:
        response = requests.post(f"https://research.txcourts.gov/CourtRecordsSearch/case/{case_key}/filings", headers=headers, json=payload)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        # If response.raise_for_status() is successful, we can try to decode the response.
        try:
            json_response = response.json()
            


            totalEvents = json_response['totalEvents']
            events = json_response['events']
            events = Events(events)



            events_df = events.as_dataframe
            print(events_df)
            return events_df
    











        except ValueError:
            # In case json decoding fails
            print("Response content is not valid JSON")
    except requests.exceptions.HTTPError as http_err:
        # In the case of HTTP errors, we can check what the server returned
        print(f"HTTP error occurred: {http_err}")
        print("Response content:", response.content)
    except requests.exceptions.RequestException as err:
        # For other request-related errors
        print(f"Error occurred: {err}")





def get_case(case_number):

    r = requests.get(f"https://research.txcourts.gov/CourtRecordsSearch/TranslateExternalToKeys/Tarrant%20County%20-%20District/{case_number}", headers=headers, json=payload).json()


    cmsKey = r['cmsKey'] if 'cmsKey' in r else None
    courtKey = r['courtKey'] if 'courtKey' in r else None
    caseKey = r['caseKey'] if 'caseKey' in r else None
    externalSource = r['externalSource'] if 'externalSource' in r else None
    jurisdictionKey = r['jurisdictionKey'] if 'jurisdictionKey' in r else None
    caseDataGUID = r['caseDataGUID'] if 'caseDataGUID' in r else None

    data_dict = { 
        'cmsKey': cmsKey,
        'courtKey': courtKey,
        'caseKey': caseKey,
        'externalSource': externalSource,
        'jurisdictionKey': jurisdictionKey,
        'caseDataGUID': caseDataGUID
    }
 


    df = pd.DataFrame(data_dict, index=[0])
    print(df)
    return df



get_case(case1)