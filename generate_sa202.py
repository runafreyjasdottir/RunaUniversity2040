#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/pi/RunaUniversity2040')
from generate_content import parse_curriculum, get_degree_info, generate_course_file
from pathlib import Path

BASE = Path("/home/pi/RunaUniversity2040")
degree_path = BASE / "bachelors" / "computer-systems-administration"
curriculum_file = degree_path / "curriculum.md"

degree_info = get_degree_info(curriculum_file)
courses = parse_curriculum(curriculum_file)

# Find SA202
target_course = None
for course in courses:
    if course["code"] == "SA202":
        target_course = course
        break

if target_course is None:
    print("Course SA202 not found")
    sys.exit(1)

print(f"Generating content for {target_course['code']}: {target_course['name']}")
filepath = generate_course_file(target_course, degree_info, degree_path)
print(f"Generated: {filepath}")