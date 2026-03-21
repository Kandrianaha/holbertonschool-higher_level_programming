#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Error: Invalid input types.")
        return
    
    if template == "":
        print("Tenplate is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        content = template
        content = content.replace("{name}", str(attendee.get("name", "N/A") or "N/A"))
        content = content.replace("{event_title}", str(attendee.get("event_title", "N/A") or "N/A"))
        content = content.replace("{event_date}", str(attendee.get("event_date", "N/A") or "N/A"))
        content = content.replace("{event_location}", str(attendee.get("event_location", "N/A") or "N/A"))

    with open(f"output_{i}.txt", "w") as f:
        f.write(content)
