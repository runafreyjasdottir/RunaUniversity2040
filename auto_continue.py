#!/usr/bin/env python3
"""
Progress tracking for University 2040 content generation.
"""

# Course list for Computer Systems Administration (Bachelor)
# Based on the curriculum.md
COURSES = [
    "SA101", "SA102", "SA103", "SA104", "SA105", "SA106", "SA107", "SA108",  # Year 1
    "SA201", "SA202", "SA203", "SA204", "SA205", "SA206", "SA207", "SA208",  # Year 2
    "SA301", "SA302", "SA303", "SA304", "SA305", "SA306", "SA307", "SA308",  # Year 3
    "SA401", "SA402", "SA403", "SA404", "SA405", "SA406", "SA407"             # Year 4
]

# Master's level courses
MASTER_COURSES = [
    "SA501", "SA503", "SA505", 
    "SA601", "SA603"
]

def get_completed_courses():
    """Check which courses have lectures.md files."""
    completed = []
    base_path = "/home/pi/RunaUniversity2040"
    
    # Check bachelor's courses
    for course in COURSES:
        lectures_path = f"{base_path}/bachelors/computer-systems-administration/{course}/lectures.md"
        try:
            with open(lectures_path, 'r') as f:
                content = f.read()
                # Check if it's a valid lecture file (not just a placeholder)
                if len(content) > 100 and "Overview" in content:
                    completed.append(course)
        except FileNotFoundError:
            pass
    
    # Check master's courses
    for course in MASTER_COURSES:
        lectures_path = f"{base_path}/masters/computer-system-administration/{course}/lectures.md"
        try:
            with open(lectures_path, 'r') as f:
                content = f.read()
                if len(content) > 100 and "Overview" in content:
                    completed.append(course)
        except FileNotFoundError:
            pass
            
    return completed

def main():
    completed = get_completed_courses()
    total = len(COURSES) + len(MASTER_COURSES)
    print(f"Progress: {len(completed)}/{total}")
    print(f"Completed courses: {', '.join(sorted(completed))}")
    
    # Find next incomplete course
    all_courses = COURSES + MASTER_COURSES
    for course in all_courses:
        if course not in completed:
            print(f"Next item: {course}")
            return course
    
    print("All courses completed!")
    return None

if __name__ == "__main__":
    main()