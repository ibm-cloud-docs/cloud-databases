#!/bin/python
# Generate the table content for the metrics dictionary for the IBM
# documentation from the json onboarding document
#
# A typical example of how this script can be run is something like this,
# which includes only the metrics starting with "wmi" and adds the labels
# instance and region to all metrics :
#
#    python collect_onboarding.py --input metrics.json --output metrics-docs.md
#
import os
import argparse
import json

# Filters that we do not include in the per metric tables
global_filters = ["ibm_ctype", "ibm_scope", "ibm_service_name", "ibm_location", "ibm_resource_group_name", "ibm_resource_type","ibm_resource"]

# Language used for the lookups
language = "en"

# Check mark image for tables
check_mark_image='![Checkmark icon](../../icons/checkmark-icon.svg)'

# Default tags that do not need to be in the onboarding docs
crn_tags = [ { "name" : "ibm_ctype", "readableName" : {"en": "Cloud Type"},  "helpText" : {"en": "The cloud type is a value of public, dedicated or local"}},
             { "name" : "ibm_service_name", "readableName" : {"en": "Service name"}, "helpText" : {"en": "Name of the service generating this metric"}},
             { "name" : "ibm_scope", "readableName" : {"en": "Scope"}, "helpText" : {"en": "The scope is the account, organization or space GUID associated with this metric"}},
             { "name" : "ibm_location", "readableName": {"en": "Location"}, "helpText": {"en": "The location of the monitored resource - this may be a region, data center or global"}},
             { "name" : "ibm_service_instance", "readableName": {"en": "Service instance"}, "helpText": {"en": "The service instance segment identifies the instance the metric is associated with"}},
             { "name" : "ibm_service_instance_name", "readableName": {"en": "Service instance name"}, "helpText": {"en": "The service instance name provides the user-provided name of the service instance which isn't necessarily a unique value depending on the name provided by the user."}},
             { "name" : "ibm_resource_group_name", "readableName": {"en": "Resource group"}, "helpText": {"en": "The resource group where the service instance was created"}},
             { "name" : "ibm_quantile", "readableName" : {"en": "Quantile"}, "helpText" : {"en": "The quantile represented when a metric supports segmenting by quantile"}},
             { "name" : "ibm_resource", "readableName" : {"en": "Resource"}, "helpText" : {"en": "The resource being measured by the service - typically a indentifying name or GUID"}},
             { "name" : "ibm_resource_type", "readableName" : {"en": "Resource Type"}, "helpText" : {"en": "The type of the resource being measured by the service"}}
]


class Metric:
    '''
    The Metric object models the metric elements in the beaconMetadata structure
    that is not of type tag
    '''
    service_metadata = None

    def __init__(self, service_metadata, metric_record):
        try:
            self.service_metadata = service_metadata
            self.name = metric_record['name']
            self.readable_name = metric_record['readableName'][language]
            self.description = metric_record['helpText'][language]
            self.type = metric_record['type']
            self.frequency = metric_record['frequency']
            self.unit = metric_record['unit']
            self.labels = metric_record['labels']
            if "plans" in metric_record:
                self.plans = metric_record["plans"]
            else:
                self.plans = None
        except Exception as e:
            print("Exception processing record - {}.  Message={}".format(metric_record, e))

        # Increase the usage count for the tags(labels)
        for tagName in self.labels:
            if tagName in service_metadata.all_tags:
                tag = service_metadata.all_tags[tagName]
                tag.inc_usage()
            else:
                # Tag not found
                print("Error: The tag {} was not found in the onboarding json file".format(tagName))

    def write_table_entry(self, file):
        '''
        write_table_entry writes a markdown table to the file handle
        passed as a parameter
        '''
        file.write("\n\n### {}\n".format(self.readable_name))
        file.write("{: ")
        file.write("#{}".format(self.name))
        file.write("}\n\n")
        file.write("{}\n\n".format(self.description))
        file.write("| Metadata | Description |\n")
        file.write("|----------|-------------|\n")
        file.write("| `Metric Name` | `{}`|\n".format(self.name))
        file.write("| `Metric Type` | `{}` |\n".format(self.type))
        file.write("| `Value Type`  | `{}` |\n".format(self.unit))
        segments = ""
        for l in self.labels:
            tag = self.service_metadata.all_tags[l]
            if tag.name in global_filters:
                # exclude attributes in the global filters list to reduce
                # clutter in the metric specific Segment By section
                continue

            if segments == "":
                segments = tag.readable_name
            else:
                segments = segments + ", " + tag.readable_name 
        file.write("| `Segment By` | `{}` |\n".format(segments))


class Tag:
    '''
    The Tag object models the tag element in the beaconMetadata structure of type tag
    '''

    def __init__(self, tag_record):
        self.name = tag_record['name']
        self.description = tag_record['helpText'][language]
        self.readable_name = tag_record['readableName'][language]
        self.used_count = 0
    
    def inc_usage(self):
        self.used_count += 1

    def is_used(self):
        if self.used_count > 0:
            return True
        else:
            return False

class ServiceMetadata:
    '''
    ServiceMetadata stores the tag and metric data retrieved from the 
    onboarding json file and provides methods to process the metadata
    '''

    metrics = {}
    all_tags = {}
    all_metrics = {}

    def __init__(self, json_filename):
        with open(json_filename) as json_file:
            data = json.load(json_file)

            print("Json file loaded : {} ".format(json_file))
            self.metrics = data['beaconMetadata']['metrics']
            if len(self.metrics) == 0:
                print("No metrics data found in the file")
                return
            else:
                print("Found {} metrics".format(len(self.metrics)))

        self.generate_tag_objects()

    def get_tag(self, name):
        if name in self.all_tags:
            return self.all_tags[name]
        else:
            return None        

    def is_ready(self):
        if len(self.metrics) > 0:
            return True
        else:
            return False

    # Generates a sorted list tuple with ( name, object ) sorted by readable_name
    def get_metrics_sorted_by_readable_name(self):
        sorted_tuples = sorted(self.all_metrics.items(), key=lambda x: x[1].readable_name )
        return sorted_tuples

    def get_plans(self):
        '''
        Returns a dictionary of plan -> array of metrics
        '''
        plans = {}
        for _, metric in self.all_metrics.items():
            if metric.plans != None:
                # Loop over all of the plans and add the metric readable
                # name to the plan dictionary
                for plan_name in metric.plans:
                    if plan_name in plans:
                        plans[plan_name].append(metric.readable_name)
                    else:
                        plans[plan_name] = []
                        plans[plan_name].append(metric.readable_name)
        return plans

    def write_plan_table_to_file(self, file, table_counter=1):
        '''
        Generate a markdown table containing the list of metrics for
        a given plan.
        '''
        plans = self.get_plans()
        plan_names = plans.keys()  # List of plans
        file.write("\n\n## Metrics available by Service Plan\n{: metrics-by-plan}\n\n")

        file.write("| Metric Name |")
        for plan_name in plan_names:
            file.write("{}|".format(plan_name))
        file.write("\n|-----------|")
        for plan_name in plans.keys():
            file.write("--------|")
        file.write("\n")

        # Now loop over all of the metrics and
        sorted_metrics = self.get_metrics_sorted_by_readable_name()
        for _, metric in sorted_metrics:
            plan_line = ""
            for plan_column in plan_names:
                if plan_column in metric.plans:
                    plan_line += " " + check_mark_image + " |"
                else:
                    plan_line += "   |"
            file.write("| [{}](#{}) | {}\n".format(metric.readable_name, metric.name, plan_line))
        file.write('{: caption="Table ' + str(table_counter) + ': Metrics Available by Plan Names" caption-side="top"}')

    def generate_tag_objects(self):
        '''
        Create the all_tags dictionary used in later processing
        by looping over the raw json map and the global default tags
        '''

        # Create the default tags ( whether used or not )
        for crn_tag in crn_tags:
            tag = Tag(crn_tag)
            self.all_tags[tag.name] = tag

        # Build the list of tags first
        for metric in self.metrics:
            if metric['type'] == 'tag':
                tag = Tag(metric)
                self.all_tags[tag.name] = tag


    def generate_metric_objects(self):
        '''
        builds the metrics dictionary from the raw json dictionary
        '''

        # Loop over the list of metrics and filter out any internal metrics
        for metric in self.metrics:
            
            if 'internal' in metric['name']:
                print("Skipping internal metric : {}".format(metric['name']))
                continue

            if metric['type'] == 'tag':
                continue

            print("Processing {}".format(metric['name']))
            metricObj = Metric(self, metric)
            self.all_metrics[metricObj.name] = metricObj

    def write_metrics_to_file(self, file, table_counter=1):
        '''
        Writes the metric documentation information in markdown format 
        to the provided filename
        '''
        print("Building the documentation and writing to a file")

        # Need a sorted list of the metrics by readable name
        sorted_metrics = self.get_metrics_sorted_by_readable_name()

        for _, metric in sorted_metrics:
            print("Processing Name: {}".format(metric.name))
            metric.write_table_entry(file)

            # We need to label each table
            file.write('{: caption="Table ' + str(table_counter) + ': ' + metric.readable_name + ' metric metadata" caption-side="top"}')
            table_counter += 1

        # Once we've written all of the metric definitions, append the
        # tag (segmentation) details
        self.write_metrics_segmentation_details(file)


    def write_metrics_segmentation_details(self, file):
        '''
        Writes the segmentation details in markdown format to the provided file handle
        '''

        file.write("\n\n## Attributes for Segmentation\n{: attributes}\n\n")

        file.write("### Global Attributes\n{: global-attributes}\n\n")
        file.write("The following attributes are available for segmenting all of the metrics listed above\n\n")
        file.write("| Attribute | Attribute Name | Attribute Description |\n")
        file.write("|-----------|----------------|-----------------------|\n")

        # Sort the filters - create a dict where the key is the readable name
        filter_dict = {}
        for tag_name in global_filters:
            tag = self.all_tags[tag_name]
            filter_dict[tag.readable_name] = tag
        
        sorted_tuples = sorted(filter_dict.items(), key=lambda x: x[1].readable_name )

        for _, tag in sorted_tuples:
            file.write("| `{}` | `{}` | {} |\n".format(tag.readable_name, tag.name, tag.description))
        
        file.write("\n### Additional Attributes\n{: additional-attributes}\n\n")
        file.write("The following attributes are available for segmenting one or more attributes as described in the reference above.  Please see the individual metrics for segmentation options.\n\n")
        file.write("| Attribute | Attribute Name | Attribute Description |\n")
        file.write("|-----------|----------------|-----------------------|\n")

        # Sort the filters - create dict where the key is the readable name
        sorted_tuples = sorted(self.all_tags.items(), key=lambda x: x[1].readable_name )

        for _, tag in sorted_tuples:
            if tag.name in global_filters or tag.is_used() == False:
                continue
            file.write("| `{}` | `{}` | {} |\n".format(tag.readable_name, tag.name, tag.description))
        
        file.write("\n")



def main(input_filename, output_filename):
    print("Reading from {} and writing to {}".format(input_filename, output_filename))

    # Read the onboarding file
    service_metadata = ServiceMetadata(input_filename)

    # If we want to add additional filtering, we can add
    # logic here to manipulate the ServiceMetadata

    service_metadata.generate_metric_objects()

    with open(output_filename, 'w') as f:
        service_metadata.write_plan_table_to_file(f)

        # Write the metadata to a file.
        service_metadata.write_metrics_to_file(f, table_counter=2)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        dest="input_filename",
                        default="onboarding.json",
                        help="Onboarding json file to read from"
                        )
    parser.add_argument('-o', '--output',
                        dest="output_filename",
                        default="onboarding-docs.md",
                        help="Target filename to write the onboarding documentation content"
                        )
    args = parser.parse_args()

    main(args.input_filename, args.output_filename)
