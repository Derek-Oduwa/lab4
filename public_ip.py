
import requests
import json

url = "https://management.azure.com/subscriptions/21998d08-01bb-4dae-b637-08089cb1d4e1/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/ip4?api-version=2023-05-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAxNTE1MzQsIm5iZiI6MTcwMDE1MTUzNCwiZXhwIjoxNzAwMTU1NTY1LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBRXgxYlBqQXRNQnRnZU8wL3ozaUdKaVRXN2JjNGhXUTVmYjgwQ2M5czFwZUdlSmd1blp3MkNCZTcxeGZtVWdUQjZ0NW5aaGhNVXRDQi8wZHJrL0tLaWFNUFhOTE9GMmI5d1dZU2paU0lvQ0k9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiT2R1d2EiLCJnaXZlbl9uYW1lIjoiRGVyZWsiLCJncm91cHMiOlsiODEwOGM1MDMtZDY1Ni00MmNmLThlZTQtODk0NGFlZjBmYWRlIiwiOTdhZjgxMmQtOTZlOS00ZjAxLThhMTEtNzU4MDMzNzYyMTdhIiwiODdmNjAwM2QtOTQ3MC00MzhmLWJmZWYtODEzYjM3ZmMyYjY4IiwiODM4YTI4OWEtODRhNC00Y2E4LWFlZWMtYjMxZWMxZDcxZDRhIiwiNGRjMDNiOWYtMWI2Yy00NDE1LWFjMDUtODI0MjcxM2M3NTIwIiwiNWFkN2Q2YjQtYWRhZi00YjlkLTk1N2YtMGYzYjYxNGJlZTYwIiwiOGFjMTU0ZGQtZDQ1Zi00YzQ2LTk0ZTUtYmI3OGZlZmEzYWVmIiwiOGM4MTg2ZWEtNDJhNC00NGFmLThhNzgtYWU5MTQwMTFlNmI0IiwiZDJhNmE4ZWYtNGQyNi00ZDk1LWJkMTEtYWExZWM2MTlmODE4IiwiYWJkNDlkZmQtY2VmYi00YzM2LWFkNjctMjVmZDlmZmQzMzdmIl0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMjA3IiwibmFtZSI6IkMyMTM3MTQ0NiBEZXJlayBPZHV3YSIsIm9pZCI6ImIwMDBlNjg5LTY4YjgtNDQwNS04NWVlLWRkYzE2ZjNkZWFjYyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQ0MDQ1IiwicHVpZCI6IjEwMDMyMDAxN0RBODlGRUQiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QU53LiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IkZuUFF5akRZN2hjT3l5dGFiengtR3NwNzJhMHk2bUp3ZUQtLVRWWUFhMGMiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTM3MTQ0NkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxMzcxNDQ2QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJOUHBKVllEWlFrdWloeUlfaXRrakFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.iNsu6w4WaZyhCk8rjrrNCc-vLBzH6f4K5kIsQrWnuS9B7CFbWE7bVwLG1tZqlzOLs506GfbbH6k5wj8RK2aiOJsG3mDAFpESS1a9EUl_kVAd3jDUYgOvNKjOAxGGJNIPptZWIwUNAB8W9dOni8Mjz7nXNV4P9BsyQPBNwttirC5xH_fkiXkJD_VfU6U0caLEQboFenJFwwQKHR718uWOWFu0vzMH7CP8k6sGshbo6cFlSYNtHHiHeiQt6Z1YZQThqRkgKIvgqQrGn8rxmC9IDKulsXEhJ6z2zXYKf-cga0C3FEEEgK7R3dxOxf-HxbBsmAo2zggWyzHvm6pe9cyvPA',
    }

data = {

    'location': "westeurope"

}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())










