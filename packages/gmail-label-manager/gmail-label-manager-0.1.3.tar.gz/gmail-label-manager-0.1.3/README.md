# Gmail Label Manager

The `gmail_label_manager` module is a crucial component of the Gmail Label Email Processor toolkit, designed to interact with Gmail labels. It allows for fetching the ID of specific Gmail labels, enabling precise control and filtering of emails for processing based on label criteria.

## Features

- Retrieve the ID of a specific Gmail label.
- Supports integration with Gmail API to manage and utilize labels for email processing tasks.

## Installation

This module is part of the Gmail Label Email Processor toolkit. To use it, ensure you have Python 3.6 or higher installed.

```bash
git clone https://github.com/yourusername/gmail-label-email-processor.git
cd gmail-label-email-processor


## Prerequisites

Before using the gmail_label_manager, you must have completed the authentication setup provided by gmail_api_auth.py, including obtaining a credentials.json file from the Google Developer Console and ensuring it is placed in the project root.

## Usage

The gmail_label_manager module can be used to fetch label IDs as part of email processing workflows. Here's a simple example:

```bash
from gmail_label_manager import get_label_id_by_name

# Fetch the ID of a specific label
label_id = get_label_id_by_name("YOUR_LABEL_NAME_HERE")

if label_id:
    print(f"Label ID for 'YOUR_LABEL_NAME_HERE': {label_id}")
else:
    print("Label not found.")

Replace "YOUR_LABEL_NAME_HERE" with the actual name of the Gmail label you wish to manage.
```

## Contributing

Contributions to the gmail_label_manager or any other component of the Gmail Label Email Processor toolkit are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.