# Gmail API Authentication Module

The `gmail_api_auth` module serves as the foundation of the Gmail Label Email Processor toolkit, providing secure authentication with the Gmail API. This module handles the OAuth2 flow, allowing other components of the toolkit to access and manipulate Gmail data under user consent.

## Features

- Implements OAuth2 authentication flow for Gmail API.
- Securely manages tokens, including token refresh.
- Facilitates seamless integration with Gmail API for email processing tasks.

## Installation

Ensure you have Python 3.6 or later installed on your system. This module is part of the Gmail Label Email Processor toolkit,

## Setup

Before using the gmail_api_auth module, you need to create a project in the Google Developer Console, enable the Gmail API, and obtain your credentials.json file. Follow these steps:

Visit the Google Developer Console.
Create a new project.
Search for the Gmail API and enable it.
Go to the Credentials page, create OAuth client ID credentials, and download the credentials.json file.
Place the credentials.json file in the root directory of the cloned repository.

## Usage

The gmail_api_auth module is used internally by other components of the Gmail Label Email Processor toolkit. However, you can directly utilize it for testing or extending the toolkit:

```bash
from gmail_api_auth import authenticate_gmail_api

# Authenticate and get the Gmail API service object
service = authenticate_gmail_api()

# Now you can use the service object to make Gmail API calls
```

## Contributing

Contributions to the Gmail API Authentication Module or any part of the Gmail Label Email Processor toolkit are welcome. 

## License

This project is licensed under the MIT License - see the LICENSE file for details.