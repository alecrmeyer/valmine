#!/bin/sh
    curl 'https://api.tracker.gg/api/v2/valorant/standard/profile/riot/chy%2300000?' \
  -H 'authority: api.tracker.gg' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en' \
  -H 'cookie: _ga=GA1.2.819530566.1648750995; X-Mapping-Server=s14; __gads=ID=5ce613606603ca69:T=1648750998:S=ALNI_MYwbR9aOQ2BRffEUYgS_VKVxIQHPA; panoramaId_expiry=1649355799493; _cc_id=4ecf426da37d1c816c0700a34a9cf4d0; panoramaId=4f2afb83e3ddca2018cbc0108d8c4945a702829f0be48eadbce9b6a56ec098d4; __gpi=UID=0000040ba49e58b7:T=1648752829:RT=1648752829:S=ALNI_Mbv7T5GdxskDfIMvi_oE0Ac6UXW3w; _gid=GA1.2.6398677.1649312637; __cflb=02DiuFQAkRrzD1P1mdjW28WYn2UPf2uFAhUxT7GFJ5PHW; __cf_bm=4ckORc8hrscjFdmnJOnnwIYfnkS_np0vDH.cGslNqmg-1649314170-0-Aag+EigR1E4GZsxR6+2BCqQKal/tzxBv7sxrwmtHgxgW70sm2QOKnwBbAwVjGsWen40VBZDddcqI+8PWSK1TvJo=; _gat_UA422801044=1; _gat_UA4228010427=1; _gat_UA4228010411=1' \
  -H 'if-modified-since: Thu, 07 Apr 2022 06:34:10 GMT' \
  -H 'origin: https://tracker.gg' \
  -H 'referer: https://tracker.gg/' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36' \
    --compressed > valdata.json

    python3 valmine2.py

for NEXT in {1..15}
do
    echo "next is $NEXT"
        curl "https://api.tracker.gg/api/v2/valorant/standard/matches/riot/chy%2300000?type=competitive&next=$NEXT" \
  -H 'authority: api.tracker.gg' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en' \
  -H 'cookie: _ga=GA1.2.819530566.1648750995; X-Mapping-Server=s14; __gads=ID=5ce613606603ca69:T=1648750998:S=ALNI_MYwbR9aOQ2BRffEUYgS_VKVxIQHPA; panoramaId_expiry=1649355799493; _cc_id=4ecf426da37d1c816c0700a34a9cf4d0; panoramaId=4f2afb83e3ddca2018cbc0108d8c4945a702829f0be48eadbce9b6a56ec098d4; __gpi=UID=0000040ba49e58b7:T=1648752829:RT=1648752829:S=ALNI_Mbv7T5GdxskDfIMvi_oE0Ac6UXW3w; _gid=GA1.2.6398677.1649312637; __cflb=02DiuFQAkRrzD1P1mdjW28WYn2UPf2uFAhUxT7GFJ5PHW; __cf_bm=4ckORc8hrscjFdmnJOnnwIYfnkS_np0vDH.cGslNqmg-1649314170-0-Aag+EigR1E4GZsxR6+2BCqQKal/tzxBv7sxrwmtHgxgW70sm2QOKnwBbAwVjGsWen40VBZDddcqI+8PWSK1TvJo=; _gat_UA422801044=1; _gat_UA4228010427=1; _gat_UA4228010411=1' \
  -H 'origin: https://tracker.gg' \
  -H 'referer: https://tracker.gg/' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36' \
    --compressed > valdata.json

    python3 valmine2.py

done
Rscript -e 'library(rmarkdown); rmarkdown::render("valanalysis.Rmd", "html_document")'
open valanalysis.html
