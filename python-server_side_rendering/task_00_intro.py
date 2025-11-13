import os
import sys

TEMPLATE_FILE = 'template.txt'
PLACEHOLDERS = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
NA_VALUE = "N/A"
ERROR_PREFIX = "Error:"


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of
    attendees.

    Args:
        template (str): The template string with placeholders (e.g., {name}).
        attendees (list): A list of dictionaries, where each dict contains
                          data for an attendee.
    """
    if not isinstance(template, str):
        print(f"{ERROR_PREFIX} Template is not a string, "
              "no output files generated.", file=sys.stderr)
        return

    is_list_of_dicts = (isinstance(attendees, list) and
                        all(isinstance(a, dict) for a in attendees))
    if not is_list_of_dicts:
        print(f"{ERROR_PREFIX} Attendees is not a list of dictionaries, "
              "no output files generated.", file=sys.stderr)
        return

    if not template.strip():
        print("Template is empty, no output files generated.", file=sys.stderr)
        return

    if not attendees:
        print("No data provided, no output files generated.", file=sys.stderr)
        return

    for index, attendee in enumerate(attendees, 1):
        personalized_invitation = template

        for placeholder in PLACEHOLDERS:
            key = placeholder.strip('{}')

            value = attendee.get(key)
            if value is None:
                replacement_value = NA_VALUE
            else:
                replacement_value = str(value)

            personalized_invitation = personalized_invitation.replace(
                placeholder, replacement_value)

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w') as f:
                f.write(personalized_invitation)
        except IOError as e:
            print(f"{ERROR_PREFIX} writing to file {output_filename}: {e}",
                  file=sys.stderr)


if __name__ == '__main__':
    if not os.path.exists(TEMPLATE_FILE):
        print(f"{ERROR_PREFIX} Template file '{TEMPLATE_FILE}' not found. "
              "Please run the bash command first.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(TEMPLATE_FILE, 'r') as file:
            template_content = file.read()
    except IOError as e:
        print(f"{ERROR_PREFIX} reading template file: {e}", file=sys.stderr)
        sys.exit(1)

    attendees_data = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"},
        {"name": "Diana", "event_date": "2024-01-01",
         "event_location": "Online"}
    ]

    print("--- Running Test Case 1:"
          "Valid Inputs ---")
    generate_invitations(template_content, attendees_data)

    print("\n--- Running Test Case 2: "
          "Empty Template ---")
    generate_invitations("", attendees_data)

    print("\n--- Running Test Case 3:"
          "Empty Attendees List ---")
    generate_invitations(template_content, [])

    print("\n--- Running Test Case 4:"
          "Invalid Template Type (Expected Error) ---")
    generate_invitations(123, attendees_data)

    print("\n--- Running Test Case 5:"
          "Invalid Attendees Type (Expected Error) ---")
    generate_invitations(template_content, "not a list")
