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
    "Cookie":"FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U2VjdXJpdHlDb250ZXh0VG9rZW4gcDE6SWQ9Il83YTA3Yzk0Zi1kMjhjLTQ2NDEtYThlNS1hZGRhNDBmNmM0OWQtNzkzMzI5REE3RjhDREYyMDI2QzUxNDZCQzU4N0RBMUIiIHhtbG5zOnAxPSJodHRwOi8vZG9jcy5vYXNpcy1vcGVuLm9yZy93c3MvMjAwNC8wMS9vYXNpcy0yMDA0MDEtd3NzLXdzc2VjdXJpdHktdXRpbGl0eS0xLjAueHNkIiB4bWxucz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3Mtc3gvd3Mtc2VjdXJlY29udmVyc2F0aW9uLzIwMDUxMiI+PElkZW50aWZpZXI+dXJuOnV1aWQ6YTE0MWM5OTYtODczZS00OGE4LWIzYjYtNmJjOGQ5ODFlZjE1PC9JZGVudGlmaWVyPjxDb29raWUgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwNi8wNS9zZWN1cml0eSI+blFDd0Z0MkhKMVpqUG83VWxyR2ptNGZKaGhxRE1CL29hWmwzWlpENnhRTXcwSWpXeDZnbU9tV1hkemtXb2F6MnVlVytOUHp2eEFFUHJjNXZIOVJWQzNjWlhpbmhWYVdZZ2pmckhFR0VGSUo3a1ZGREQ0NUhZWWdtdlBQRlNBQndGNytzeU4wNDNjTDZPVkNERFYwZXRLRWVJTEdoejRRamNXRU1aWWVZeC80UVlQV3R0V2dHcERvNVQyZHloTUFKUHcrVmptTFlrWDJRRmdSMlJUZjhVZ2tncHVlcnJRL280NHpBMDJoNVNaSXNRSksrWHBNcElKZWdqeTNGWDdJdWt3QnJHWGtGR0J5VzFyUmpRaU9XazN3SitVUmhIbUdUbE1ibUoxalNNQUFHUDQyTVJxU1ZieXhWQjRGWU9mSENxenFEUTZncFJsYUkvSHhyUVVIdnpYc2FJWUk2bTRib0J2Q0JWdTRxK0NTTFRNZm1QSEtaQUhIN2c3YWsxTUxnekZaTFFpZnUzNmN0T0xoQkZoYWJqVitsMWtoMXY5ZEEyNnQ3Y0pPZStEM2UyWG0rd2ZselJoSyttU3h0TTBJb2NzMmhjQU95T3FlQTkvMDRxUDdPOGwzK2xHR00zUXhJVk5ocDlVTFBxcVdTbmRRN0V1d1BYVjNBL2xwRjk5RmsyTUt1S1NJeHp2SjBYcTdYcjBrZzdKYys4OEJDRUdQZ1hOSm9KZUQxV1AxZC9CRWpNQktNTG9ESXBNenU2aVRFM2RIaWRkTnByNmFXbk5xUFkwNmoxdi93SUlGODZhekZITlZ6aVBxRi9lb2ZNRy8yWkxrUDFhMmhNS3BrZnNwTFd4SHdWU0N4eVkwcGZFbzdXT0dtOGRMRlREa1FTYzJ5OGFGdmJsdmV5cHh6YmFLTDlJTE9kWHd6clY4NmEvT2o3eXlNR0F0WXBhdlpkQUZQcHpEUis4cERXM3pVRmhML0lzQ1JVMDUydjBNR2swem9hWHRUNnBoVlZ0QUpTWGRXQXFNZ0s0amlmNWphRmM0dlkxSW4zWjMrenBiNExsa21BeGZ3UVZGN09zYVVPNTVjek13cjdTbHo3UEVjMFFmS0FoK2F0VEpMNmcrTTRndC9NeHlwMlJRckpTTWZ2dWp6dHR6TnBMeVV2a25nTFJPK1hoeWZRd3lRV1lrUTk1WjZqS3BrMGVEckdhNzJqcCtyZyt5TWl2aHdNYmFxWUJGN2FxRlBOdDBUVkRGVDRrLzUvQkNFV1pPaDBJUDdlSmFFYkN4OUJrYzJyem9mbVJIUjNZb2EzdTViTzR0ak5taWpwY3c4ZlZ0OHpzM28rVldxL3E4TnNLRFA1Wmo3aXA3ZWozV0hIZFJCdXVmK0MwT1JvYVRadWxKU2JNTFlRMlRjUURF; FedAuth1=aGVHdHA4WmlOMzR4Q0RHMnoycW02T2pXeE1LL3J4RjdLbngyamlPUzRnd0hoenhtbU9QRCtHWjE2enduaEw0ZmFkZGVnNVdTaWVSYzRzM01OOERnYm1QVzFQY3dPQnZiQkdxVHNpbllEQVg0UE1nQlZyaG1xYWRWUlpNSWhYZmtpY0JxSXN3aVJHb2hCcFl4WVh4Z0x5SHFlcGQ1Wm41NTNlcmZCUTlPdU9HOThQU2o3dDdMdmNqUlNGd3RiaDcyVytwTVNkaHR1ZkNVVmxIbWpEeUZKUDNMR1pmd1FpeFEwY1l6ZzNMZEd1Y1JWT3MrZE53UTR6cDV0VUZlZHp3VUxuRERQc0U3U3NQekZHeGdhaGFQLy9ZY0ZITWxacnNFNC8zWkhYNWViNWNCQ0NnenVpcVlLNXFGbTVIdkVndmwvYkxiajErSXQ0WjhQalJxdGRLUTEyWmx6RldnUWE5eWpRR0praHlTRVBpQWJiL1ZZcUR6N1VWNlFsTTZPbjJIUWtka3RRd2F1VmRoU2R5cVZPV3drSGxlSXA0b3A2OHlacExoYS9vNkZ4QjJTakhSOGV3Tmx5cDhPL2Z3YWdNNkJwR3Z1UFBaeEZpVmVSdVJmZ2QzMlZ0Y0ZJdVhRSFBJODJ1UlpMMWNpQ29KSzhxWlB5azVXTFRPR2lYb3hjTFlIQ1lOaGtoZUZsNVF0YmExRWJtSTRvd0FQb001Z0VNc0FUell6VHRkTVVCU01MbUw1d2VJY2sxSERmTGxUd3lQMjZLQjREbWErN1lJM01FcGlBSE9mNHNWYkxGaEFnazR5Um44ZEMrK3hQZ0xORi9yWFA0TElUNWtiNnViVGxsU1RIaURxVmFUMFJKclk3bGZNQ0lVVjQ5ZFRGdFhYdEdNaHc3NDVJUG1IaW16TlA2NmhJNkt3TE91QXRzZ1ZnQVNrNlJzcVMvaHdBQWVGS3U4b0g4YUxkYnplM0llVFNkNGJHR0JjNFRDR20xRnVnak9DRHhwVGlWL2E4NXpoVktNQ2QyS1o2NndQZ0ZzQlp4OWFlNDVuT01hQ3QxNXMwNjdXcWIwdmN4bXVzdDUrUy90WXVHVlhDMytqN2NwbnVVNnVvb3drOGwrYlJVYkJZVnAyY0JScWdUbWdkYnpRYXJIeC9xbnlBdGZmd2JoVnR6eEJqZjdidEdxV0NvRWNPWEdaMzMvM3grVXJrR3QwVjYyS2xBa0JSLzk0SDc5Qkc4YjBYOG81MHZMT3ZiclhGeFhRZWQ4UUQvV0xxNVFQYTg0aFNkMlVpLy93MHNldUV6dEd1UlhwRXJFOXRsdXI8L0Nvb2tpZT48L1NlY3VyaXR5Q29udGV4dFRva2VuPg==; _hjSessionUser_1494715=eyJpZCI6ImM3NjE1MDcwLTI4ZGItNWRjYy1hOWZiLWJhNjE5NmQ3OTFiMSIsImNyZWF0ZWQiOjE3MDk2MTA0MTI0MTMsImV4aXN0aW5nIjp0cnVlfQ==; __utma=211709392.1586994462.1705728131.1709440365.1709770285.22; __utmz=211709392.1709770285.22.20.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); IdSvr.WsFedTracking=Pw5Y16wuz40xfX8lUsOOT3alQYHnYLCj3oLWrgO_kH3Q96rRQKDzdLxWFBAgPjmDER6flBMPiBAZkjb-L7A_fEZTyzUdHB6FhUYpdU7tUywUrwslmhhU1P8P_17WXRVbODEdtwLbjI--qPwa7harHlopEVlqr8sFp0rAwJQQlVqp5KutzikiCI4LP4Q7vyefjRVFKU7xXbi_Pbr7qnc6CZgwpWSnvPMdgqKFpCNMu_wDc4HflSsHpXAcPivZ7HlFBJnRagJ16HNxqhoIh1Fv6lvoiTT5Ax5PipGddyGlkrY; _hjSession_1494715=eyJpZCI6ImVlYzEwMjYzLTMxNTctNDEwYy1iYTMxLWJlYTgwNjdiNTZhMyIsImMiOjE3MTA4MjEwMTExNTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowfQ==; logged_in=true; idle_timer=2024-03-19T04:32:11.464Z"

}
payload = {
    "pageSize": 20,
    "pageIndex": 0,

    "eventType": 0
}


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