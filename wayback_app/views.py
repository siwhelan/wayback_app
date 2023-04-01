from django.http import (
    JsonResponse,
    HttpResponseBadRequest,
    HttpResponseServerError,
    HttpResponse,
)
from django.shortcuts import render
import requests


def check_wayback_availability(url, timestamp=None):
    api_url = "https://archive.org/wayback/available"
    payload = {"url": url}

    if timestamp:
        payload["timestamp"] = timestamp

    try:
        # Send GET request to Wayback Machine API with URL and (optional) timestamp
        response = requests.get(api_url, params=payload)
        response.raise_for_status()  # raise exception for 4xx or 5xx HTTP status codes
        data = response.json()  # parse JSON response
    except requests.exceptions.RequestException as e:
        # handle any exceptions that occurred during the request
        print(f"Error: {e}")
        return None

    return data

def index(request):
    if request.method == "POST":
        url = request.POST.get("url", "")
        timestamp = request.POST.get("timestamp", "")

        if not url:
            # Return HTTP 400 Bad Request if user did not provide a URL
            return HttpResponseBadRequest("Please provide a URL.")

        wayback_data = check_wayback_availability(url, timestamp)

        if not wayback_data:
            # Return HTTP 500 Internal Server Error if an error occurred while checking the URL
            return HttpResponseServerError(
                "An error occurred while checking the URL."
            )

        if wayback_data.get("archived_snapshots"):
            # Construct URL for closest snapshot
            snapshot_url = wayback_data["archived_snapshots"]["closest"]["url"]
            # Render template with URL
            return render(request, "snapshot.html", {"snapshot_url": snapshot_url})
        else:
            # Return regular HTTP response indicating that the URL 
            # is not available in the Wayback Machine, with a button to refresh/start over
            return render(request, "not_found.html")
    else:
        # Render index.html template for GET requests
        return render(request, "index.html")