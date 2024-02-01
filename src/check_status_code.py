http_status_codes = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable"
}


def is_status_good(code):
    if code in range(200, 299):
        print(f"{code}: {http_status_codes[code]}")
        return True
    else:
        print(f"error {code}: {http_status_codes[code]}")
        return False
