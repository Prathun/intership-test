import requests
from fake_useragent import UserAgent

api_url = "https://www.carwale.com/api/v4/autocomplete/?source=1%2C2%2C3%2C5%2C11%2C15%2C13%2C14%2C10%2C16%2C17%2C4%2C8%2C9%2C6%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29&value=mahindra&size=20&applicationId=1&showNoResult=true&cityId=-1"

ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

cookies = {
    "BHC": "BDiHonu0UAvKz1DWIgqfpO9Zy",
    "CWC": "KbYlKbGOLkNCulwBCdHpu8gMG",
    "CurrentLanguage": "en",
    "_pageviews_modelid": "-1",
    "_abtest": "46",
    "languageSelected": "en",
    "_gcl_au": "1.1.1680467201.1746250973",
    "_ga": "GA1.1.16872966.1746250973",
    "_carSearchType": "1",
    "_fbp": "fb.1.1746250981158.616250130102534793",
    "_gcl_gs": "2.1.k1$i1746261958$u52149691",
    "_gcl_aw": "GCL.1746261970.Cj0KCQjw_dbABhC5ARIsAAh2Z-SkXap2YOOurds_PZqmNhaLB8eo9wrapbwn1_bnHaF_uLFpRHEsT7YaAtQ5EALw_wcB",
    "_cwutmz": "utmcsr%3Dgoogle%7Cutmgclid%3D%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic%7Cutmtrm%3D%7Cutmcnt%3D",
    "vernacularPopupClose": "1",
    "cebs": "1",
    "_ce.clock_data": "414%2C103.147.208.148%2C1%2C06b4a7e6274c16710a1f6ac7ae09eff9%2CChrome%2CIN",
    "__gads": "ID=606d1db7dc2631f2:T=1746250981:RT=1746862795:S=ALNI_MbGDMxfvmHcJD-wnJnIrPXlxRHn_g",
    "__gpi": "UID=000010b6b540bc59:T=1746250981:RT=1746862795:S=ALNI_MbM7I1JKiZE7tnPseozoEydze9xog",
    "__eoi": "ID=15d245a2f3212333:T=1746250981:RT=1746862795:S=AA-AfjYW0w-X2G-kF1ZraXf-43U-",
    "cebsp_": "2",
    "_uetsid": "f948e4302d7111f0bd459930065ab7f3",
    "_uetvid": "e889409027df11f088bce1051db58b3e",
    "FCNEC": "%5B%5B%22AKsRol_6mKt_iKFbanWKE8PwbGUtAjagT1d8KZ58hMbMvdzN5OSlA-yWKCPOrZqepZe0Z_VhIb-1jkWBmc3ysrK2o5x0xccMuKa-lOdtR-YiwkzT4ARmls_ZmSIL_q5HnF6PFnU_FbdqQ7ute8NziXmhDy0RE0MGeg%3D%3D%22%5D%5D",
    "_ce.s": "v~aacea0ea00903feef445bf0f8646e6ce68e12870~lcw~1746863142557~vir~returning~lva~1746862815802~vpv~1~as~false~v11.fhb~1746862793479~v11.lhb~1746863117966~v11.cs~44156~v11.s~f650a500-2d71-11f0-8fbd-e524a18c0811~v11.sla~1746863142567~v11.send~1746863142556~lcw~1746863142568",
    ".AspNetCore.Antiforgery.9TtSrW0hzOs": "CfDJ8JUh_GoNOjhBqUJ2d7OuCzQw8Hm8simNQqt7NDd6AGigctCGJsaFAWXOuRoxGgrKcJD62F-d-oQ3n7h5QYSWAparlt2VtgXaLvjsdS_8hOELePbRmChn3yVkDoOUzOGzMvA3v2px-N_qrQPcy5GxmcQ",
    "bhs_cw": "BDiHonu0UAvKz1DWIgqfpO9Zy.M4GG3uH9wV.1746862785.1746862807.1746863744.3",
    "_cwv": "KbYlKbGOLkNCulwBCdHpu8gMG.KbYlKbGOLkNCulwBCdHpu8gMG.1746862780.1746863740.1746863745.3",
    "_cwutmzsrc": "G%7CG%7CG%7CG%7CG%7CG%7CG%7CG%7CG%7CG",
    "_cwutmzmed": "O%7CO%7CO%7CP%7CP%7CO%7CO%7CO%7CO%7CO",
    "_ga_Z81QVQY510": "GS2.1.s1746862783$o3$g1$t1746863747$j55$l0$h0"
}

response = requests.get(api_url, headers=headers, cookies=cookies, timeout=10)
response.raise_for_status()

data = response.json()
filter_data = []
for item in data:
    items = {
        "modelName": item["payload"].get("modelName"),
        "makeName": item["payload"].get("makeName")
    }
    filter_data.append(items)

for modelname in filter_data:
    print(modelname)

print("\nData fetched successfully")