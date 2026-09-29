import random
import csv
from datetime import datetime, timedelta

# 1. GENERATE MOCK PROCUREMENT DATA
random.seed(42)
n_rows = 200

hubs = ['Mekelle Hub', 'Hawassa Hub', 'Dire Dawa Hub', 'Bahir Dar Hub', 'Adama Hub']
items = ['Emergency Medical Kits', 'Water Purification Units', 'Ready-to-Use Therapeutic Food (RUTF)', 'Educational Supplies', 'High-Energy Biscuits']
vendors = ['Ethio Logistics Corp', 'Global Relief Supplies Ltd', 'Horn of Africa Freight', 'Red Sea Trading']
statuses = ['Delivered', 'In Transit', 'Delayed', 'Under Review']

start_date = datetime(2026, 1, 1)
data = []

for i in range(n_rows):
    order_date = start_date + timedelta(days=random.randint(0, 250))
    status_choice = random.choices(statuses, weights=[0.6, 0.2, 0.1, 0.1], k=1)[0]
    qty = random.randint(50, 2000)
    unit_cost = round(random.uniform(5.0, 150.0), 2)
    total_val = round(qty * unit_cost, 2)
    lead_time = random.randint(5, 25) if status_choice == 'Delivered' else "N/A"
    
    data.append({
        'PO_Number': f'PO-2026-{1000+i}',
        'Order_Date': order_date.strftime('%Y-%m-%d'),
        'Item_Category': random.choice(items),
        'Destination_Hub': random.choice(hubs),
        'Vendor': random.choice(vendors),
        'Quantity_Ordered': qty,
        'Unit_Cost_USD': unit_cost,
        'Status': status_choice,
        'Total_Value_USD': total_val,
        'Lead_Time_Days': lead_time
    })

# 2. RUN PROCUREMENT METRICS & ANALYTICS
print("="*60)
print("     ADDIS ABABA LOGISTICS: PROCUREMENT ANALYTICS REPORT  ")
print("="*60)

total_spend = sum(row['Total_Value_USD'] for row in data)
print(f"\n[+] Total Procurement Spend Analyzed: ${total_spend:,.2f} USD")

# Metric B: Sourcing
category_spend = {}
for row in data:
    cat = row['Item_Category']
    category_spend[cat] = category_spend.get(cat, 0) + row['Total_Value_USD']

print("\n[+] Total Spend by Item Category:")
for cat, spend in sorted(category_spend.items(), key=lambda x: x[1], reverse=True):
    print(f" - {cat}: ${spend:,.2f} USD")

# Metric C: Risk Management
status_counts = {}
for row in data:
    stat = row['Status']
    status_counts[stat] = status_counts.get(stat, 0) + 1

print("\n[+] Order Status Breakdown (Risk Assessment):")
for stat, count in status_counts.items():
    pct = (count / n_rows) * 100
    print(f" - {stat}: {count} orders ({pct:.1f}%)")

# Save to CSV
with open('procurement_clean_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    if data:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

print("\n[✔] Clean pipeline database saved as 'procurement_clean_dataset.csv'.")
print("="*60)
