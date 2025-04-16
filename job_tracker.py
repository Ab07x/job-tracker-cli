
import csv
import os

FILENAME = "jobs.csv"
FIELDS = ["Company", "Title", "Date Applied", "Status"]

def load_jobs():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_jobs(jobs):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(jobs)

def add_job():
    company = input("Company: ")
    title = input("Job Title: ")
    date = input("Date Applied (YYYY-MM-DD): ")
    status = input("Status (e.g., Applied, Interviewing, Rejected, Offer): ")
    return {"Company": company, "Title": title, "Date Applied": date, "Status": status}

def display_jobs(jobs):
    if not jobs:
        print("No job applications found.")
        return
    print("\n--- Job Applications ---")
    for i, job in enumerate(jobs, start=1):
        print(f"{i}. {job['Company']} - {job['Title']} ({job['Date Applied']}) - Status: {job['Status']}")

def update_job(jobs):
    display_jobs(jobs)
    index = int(input("Enter job number to update status: ")) - 1
    if 0 <= index < len(jobs):
        new_status = input("New Status: ")
        jobs[index]['Status'] = new_status
        print("Job updated successfully.")
    else:
        print("Invalid job number.")

def delete_job(jobs):
    display_jobs(jobs)
    index = int(input("Enter job number to delete: ")) - 1
    if 0 <= index < len(jobs):
        del jobs[index]
        print("Job deleted successfully.")
    else:
        print("Invalid job number.")

def main():
    jobs = load_jobs()
    while True:
        print("\n1. View Jobs\n2. Add Job\n3. Update Status\n4. Delete Job\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            display_jobs(jobs)
        elif choice == '2':
            jobs.append(add_job())
            save_jobs(jobs)
        elif choice == '3':
            update_job(jobs)
            save_jobs(jobs)
        elif choice == '4':
            delete_job(jobs)
            save_jobs(jobs)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
