import meraki
import json
import config
import csv

dashboard = meraki.DashboardAPI(config.api_key,single_request_timeout=999999)

# Uses the Meraki library to grab Organization info.
orgs = dashboard.organizations.getOrganizations()

# Displays the org name and ID 
for org in orgs:
    print("Organization name: " + str(org["name"]) + " | " + "ID: " + str(org["id"]))

# Prompts user to select Organization ID

org_id = input("Select an organization id: ")

# Displays dashboard orrganization mapped to organization ID
networks = dashboard.organizations.getOrganizationNetworks(organizationId=org_id)

# Displays all networks in the organization the user has selected

for network in networks:
    print("Network name: " + str(network["name"]) + " | " + "ID: " + str(network["id"]))

print("-------------------------------------")
breaker = "1"
networks_to_output = []
