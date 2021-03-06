# Some prerequisites are needed
# To execute in your gcloud environment run the line below
# python gcp_list_vms.py <your-key.json>
from pprint import pprint
from googleapiclient import discovery
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
from six.moves import input

import googleapiclient.discovery
import argparse
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/FelipePiton/Desktop/Felipe/Curso/Bootcamp/GCP/Missão-1/project-bootcamp-89-4c5ee838c44e.json"

# Project ID for this request.
project = "project-bootcamp-89"
zone =  "us-east1-b"
compute = googleapiclient.discovery.build('compute', 'v1')
space = ' '

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()

    print ("{:<7} {:<11} {:<13} {:<12} {:<12} {:<15} {:<0}".format('NAME','ZONE','MACHINE_TYPE','PREEMPTIBLE','INTERNAL_IP','EXTERNAL_IP','STATUS'))

    for item in result['items']:
        if item['status'] == "RUNNING":

            var_name = item['name']
            var_zone = item['zone']
            var_machine_type = item['machineType']
            var_preemptible = item['scheduling']['preemptible']
            var_internal_ip = item['networkInterfaces'][0]['networkIP']
            var_external_ip = '{:<14}'.format(item['networkInterfaces'][0]['accessConfigs'][0]['natIP'])
            var_status = item['status'].rjust(0)

            print ("{:<7} {:<11} {:<13} {:<12} {:<12} {:<15} {:<0}".format(var_name, var_zone.rsplit('/', 1)[-1], var_machine_type.rsplit('/', 1)[-1], str(var_preemptible),var_internal_ip, var_external_ip,var_status))
    return result['items'] if 'items' in result else None
list_instances(compute, project, zone)
