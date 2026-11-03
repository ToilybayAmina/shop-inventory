import requests
import datetime

# GitHub API параметрлері
REPO = "ToilybayAmina/shop-inventory"
TOKEN = "YOUR_GITHUB_TOKEN"  # Жергілікті іске қосқанда өз токеніңізді қоясыз
headers = {"Authorization": f"token {TOKEN}"}

def get_dora_metrics():
    url = f"https://api.github.com/repos/{REPO}/pulls?state=all&per_page=100"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Қате: {response.status_code}")
        return

    prs = response.json()
    merged_prs = [pr for pr in prs if pr.get('merged_at') is not None]

    print(f"Жалпы біріктірілген PR саны: {len(merged_prs)}")

    lead_times = []
    for pr in merged_prs:
        created = datetime.datetime.strptime(pr['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        merged = datetime.datetime.strptime(pr['merged_at'], "%Y-%m-%dT%H:%M:%SZ")
        lead_time_hours = (merged - created).total_seconds() / 3600
        lead_times.append(lead_time_hours)

    if lead_times:
        avg_lead_time = sum(lead_times) / len(lead_times)
        print(f"Орташа Lead Time: {avg_lead_time:.1f} сағат")
    else:
        print("Деректер жоқ.")

if __name__ == "__main__":
    get_dora_metrics()
