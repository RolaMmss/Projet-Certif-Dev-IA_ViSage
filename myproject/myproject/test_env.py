import os

# Get the environment variable
connection_string = os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')

# Print the environment variable
print(f'APPLICATIONINSIGHTS_CONNECTION_STRING={connection_string}')
