import aiohttp
import asyncio
import json
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# URL dan header
url = "https://clownfish-app-f7unk.ondigitalocean.app/v2/click/clickEvent"
headers = {
    "Sec-CH-UA": '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    "Content-Type": "application/json",
    "Sec-CH-UA-Mobile": "?1",
    "Launch-Params": "query_id="
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 EdgA/126.0.0.0",
    "Sec-CH-UA-Platform": '"Android"',
    "Accept": "*/*",
    "Origin": "https://miniapp.yesco.in",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://miniapp.yesco.in/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=1, i",
}


payload_template = {
    "count": 1500,
    "sessionId": "31dee19e-b678-4325-9636-c042a9dd883f",
    "startSessionMs": 1721756711483,
    "lastSessionActivityMs": 1721756721201,
    "totalSessionClicks": 1,
}


async def send_request():
    async with aiohttp.ClientSession() as session:
        payload = payload_template.copy()
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                response_data = await response.json()
                if response_data.get("status") == "ok":
                    count = payload["count"]  # Ambil nilai count dari payload
                    print(
                        f"{Fore.GREEN}Status: ok, add click +{count}{Style.RESET_ALL}"
                    )
                else:
                    print(
                        f"{Fore.RED}Gagal | Respons: {response_data}{Style.RESET_ALL}"
                    )
        except json.JSONDecodeError:
            print(
                f"{Fore.RED}Gagal | Respons JSON tidak valid: {await response.text()}{Style.RESET_ALL}"
            )
        except Exception as e:
            print(f"{Fore.RED}Gagal | Error: {str(e)}{Style.RESET_ALL}")


async def main():
    while True:  # Loop tak berujung
        await send_request()
        await asyncio.sleep(5)  # Tunggu selama 2 detik


# Run the asynchronous main function
asyncio.run(main())
yesputih
