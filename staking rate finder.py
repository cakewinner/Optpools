import requests

# Function to fetch the highest staking rates from various platforms
def fetch_highest_staking_rate():
    # Example API endpoints for different platforms
    platforms = {
        "PlatformA": "https://api.platforma.com/staking_rates",
        "PlatformB": "https://api.platformb.com/staking_rates",
        "PlatformC": "https://api.platformc.com/staking_rates"
    }
    
    highest_rate = 0
    best_platform = ""

    for platform, url in platforms.items():
        response = requests.get(url)
        data = response.json()
        
        # Assuming the API returns a list of rates
        for rate in data['rates']:
            if rate['duration'] == 90 and rate['currency'] == 'USDT' or 'USDC' or 'DAI':
                if rate['percentage'] > highest_rate:
                    highest_rate = rate['percentage']
                    best_platform = platform

    return highest_rate, best_platform

# Main execution
if __name__ == "__main__":
    rate, platform = fetch_highest_staking_rate()
    #Stake USDT