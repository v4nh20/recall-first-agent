import requests
import os

# Lấy API key từ biến môi trường
API_KEY = os.getenv("RECALL_API_KEY")
BASE_URL = "https://api.competitions.recall.network/api"
TOKEN_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"  # WETH

def fetch_price():
    url = f"{BASE_URL}/price?token={TOKEN_ADDRESS}&chain=evm&specificChain=eth"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("price")
    else:
        print("❌ Lỗi khi gọi API:", response.status_code, response.text)
        return None

def run_agent():
    print("🔍 Đang lấy giá WETH từ Recall...")
    price = fetch_price()

    if price is None:
        print("⚠️ Không thể lấy giá.")
        return

    print(f"💰 Giá hiện tại: ${price:.2f}")

    if price < 1800:
        print("✅ Giá thấp → Đề xuất: BUY")
    else:
        print("⏳ Giá cao → Đề xuất: HOLD")

if __name__ == "__main__":
    run_agent()
