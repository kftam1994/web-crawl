import os
import requests
import json

def fetch_tradingview_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['ideas']['items']
    else:
        print(f"Error: Unable to fetch data. Status code {response.status_code}")
        return []

def save_chart_image(image_url, save_path):
    image_response = requests.get(image_url, stream=True)
    if image_response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in image_response.iter_content(1024):
                file.write(chunk)
    else:
        print(f"Error: Unable to download image from {image_url}. Status code {image_response.status_code}")

def extract_and_save_data(items, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for item in items:
        # Extract useful data
        data = {
            "id": item.get("id"),
            "name": item.get("name"),
            "description": item.get("description"),
            "created_at": item.get("created_at"),
            "chart_url": item.get("chart_url"),
            "symbol": item.get("symbol", {}).get("name"),
            "user": {
                "id": item.get("user", {}).get("id"),
                "username": item.get("user", {}).get("username"),
                "pro_plan": item.get("user", {}).get("pro_plan"),
            },
            "likes_count": item.get("likes_count"),
        }

        # Save the data as JSON
        json_path = os.path.join(output_dir, f"{data['id']}.json")
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        # Save the chart image
        image_url = item.get("image", {}).get("big")
        if image_url:
            image_path = os.path.join(output_dir, f"{data['id']}.png")
            save_chart_image(image_url, image_path)

if __name__ == "__main__":
    # URL for TradingView ideas data
    url = "https://www.tradingview.com/ideas/page-1"
    output_directory = "tradingview_data"

    # Fetch and process data
    items = fetch_tradingview_data(url)
    extract_and_save_data(items, output_directory)
    print(f"Data extraction and image download complete. Saved in '{output_directory}' folder.")
