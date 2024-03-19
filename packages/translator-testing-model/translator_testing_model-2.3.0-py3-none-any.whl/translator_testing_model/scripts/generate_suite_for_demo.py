from src.translator_testing_model.datamodel.pydanticmodel import TestAsset, TestCase, TestSuite, TestMetadata, Qualifier
import csv
import json
import requests
import yaml
import bmt
toolkit = bmt.Toolkit()


def retrieve_predicate_mapping():
    # URL of the YAML file
    predicate_mapping_url = "https://w3id.org/biolink/predicate_mapping.yaml"

    # Fetch the content of the YAML file
    request_response = requests.get(predicate_mapping_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the YAML content into a Python dictionary
        predicate_mapping = yaml.safe_load(request_response.content)

        # Return the parsed dictionary
        return predicate_mapping
    else:
        # Handle errors or unsuccessful requests
        print(f"Failed to retrieve the file. HTTP Status Code: {request_response.status_code}")
        return None


def parse_tsv(filename):
    """
    Parse a TSV file and return a list of dictionaries.

    :param filename: The path to the TSV file.
    :return: A list of dictionaries, where each dictionary represents a row in the TSV.
    """
    with open(filename, newline='', encoding='utf-8') as tsvfile:
        # Use csv.DictReader, specifying the delimiter as a tab
        reader = csv.DictReader(tsvfile, delimiter='\t')

        # Convert the reader into a list of dictionaries
        return list(reader)


# Functions to create TestAssets, TestCases, and TestSuite
def create_test_assets_from_tsv(test_assets):
    assets = []
    for row in test_assets:
        if row.get("Relationship") == "":
            continue

        converted_predicate = None
        biolink_qualified_predicate = ""
        biolink_object_aspect_qualifier = ""
        biolink_object_direction_qualifier = ""
        specified_predicate = row.get("Relationship").lower().strip()
        if specified_predicate == "decreases abundance or activity of":
            specified_predicate = "decreases activity or abundance of"
            print("specified predicate", specified_predicate)
        if toolkit.get_element(specified_predicate) is not None:
            converted_predicate = toolkit.get_element(specified_predicate).name
            converted_predicate = converted_predicate.replace(" ", "_")
            print("converted predicate", specified_predicate)
        else:
            pred_mapping = toolkit.pmap
            for collct in pred_mapping.values():
                for map_item in collct:
                    if map_item.get("mapped predicate") == specified_predicate:
                        print("mapped it", map_item.get("mapped predicate"))
                        converted_predicate = map_item.get("predicate")
                        converted_predicate = converted_predicate.replace(" ", "_")
                        biolink_object_aspect_qualifier = map_item.get("object aspect qualifier")
                        biolink_object_direction_qualifier = map_item.get("object direction qualifier")
                        biolink_qualified_predicate = "biolink:"+map_item.get("qualified predicate")

        if row.get("Expected Result / Suggested Comparator") == "4_NeverShow":
            expected_output = "NeverShow"
        elif row.get("Expected Result / Suggested Comparator") == "3_BadButForgivable":
            expected_output = "BadButForgivable"
        elif row.get("Expected Result / Suggested Comparator") == "2_Acceptable":
            expected_output = "Acceptable"
        elif row.get("Expected Result / Suggested Comparator") == "1_TopAnswer":
            expected_output = "TopAnswer"
        elif row.get("Expected Result / Suggested Comparator") == "5_OverlyGeneric":
            expected_output = "OverlyGeneric"
        else:
            print(f"{row.get('id')} has invalid expected output")
            print(row.get("Expected Result / Suggested Comparator"))
            continue
        output_category = None
        input_category = None
        if row.get("InputID").startswith("NCBIGene:"):
            input_category = 'biolink:Gene'

        chem_prefixes = toolkit.get_element("chemical entity").id_prefixes

        if any(row.get("InputID").startswith(prefix) for prefix in chem_prefixes):
            input_category = 'biolink:ChemicalEntity'
        if row.get("InputID").startswith("MONDO:"):
            input_category = 'biolink:Disease'
        if row.get("InputID").startswith("UBERON:"):
            input_category = 'biolink:AnatomicalEntity'
        if row.get("InputID").startswith("HP:"):
            input_category = 'biolink:PhenotypicFeature'
        if any(row.get("OutputID").startswith(prefix) for prefix in chem_prefixes):
            output_category = 'biolink:ChemicalEntity'
        if row.get("OutputID").startswith("MONDO:"):
            output_category = 'biolink:Disease'
        if row.get("OutputID").startswith("UBERON:"):
            output_category = 'biolink:AnatomicalEntity'
        if row.get("OutputID").startswith("HP:"):
            output_category = 'biolink:PhenotypicFeature'
        if row.get("OutputID").startswith("DRUGBANK:"):
            output_category = 'biolink:ChemicalEntity'

        print(converted_predicate, row, expected_output)
        ta = TestAsset(id=row.get("id").replace(":", "_"),
                       name=expected_output + ': ' + row.get("OutputName").strip() +" "+ row.get("Relationship").strip().lower() +" "+ row.get("InputName").strip(),
                       description=expected_output + ': ' + row.get("OutputName").strip() +" "+ row.get("Relationship").strip().lower() +" "+ row.get("InputName").strip(),
                       input_id=row.get("InputID").strip(),
                       predicate_name=converted_predicate,
                       predicate_id="biolink:"+converted_predicate,
                       output_id=row.get("OutputID").strip(),
                       output_name=row.get("OutputName").strip(),
                       output_category=output_category,
                       expected_output=expected_output.strip(),
                       test_metadata=TestMetadata(id=1),
                       input_category=input_category,
                       )
        ta.input_name = row.get("InputName").strip()
        if row.get("Translator GitHubIssue") != "" and row.get("Translator GitHubIssue") is not None:
            tmd = TestMetadata(id=1,
                               test_source="SMURF",
                               test_reference=row.get("Translator GitHubIssue").strip(),
                               test_objective="AcceptanceTest")
            ta.test_metadata = tmd
        else:
            tmd = TestMetadata(id=1,
                               test_source="SMURF",
                               test_objective="AcceptanceTest")
            ta.test_metadata = tmd
        ta.runner_settings = [row.get("Settings").lower()]

        if biolink_qualified_predicate != "":
            qp = Qualifier(parameter="biolink_qualified_predicate",
                           value=biolink_qualified_predicate)
            oaq = Qualifier(parameter="biolink_object_aspect_qualifier",
                            value=biolink_object_aspect_qualifier.replace(" ", "_"))
            odq = Qualifier(parameter="biolink_object_direction_qualifier",
                            value=biolink_object_direction_qualifier)
            qualifiers = [qp, oaq, odq]

            ta.qualifiers=qualifiers
        if row.get("Well Known") == "yes":
            ta.well_known = True
        else:
            ta.well_known = False
        assets.append(ta)

    return assets


def create_test_cases_from_test_assets(test_assets, test_case_model):
    # Group test assets based on input_id and relationship
    grouped_assets = {}
    for test_asset in test_assets:
        key = (test_asset.input_id, test_asset.predicate_name)
        if key not in grouped_assets:
            grouped_assets[key] = []
        grouped_assets[key].append(test_asset)

    # Create test cases from grouped test assets
    test_cases = []
    for idx, (key, assets) in enumerate(grouped_assets.items()):
        test_case_id = f"TestCase_{idx}"
        descriptions = '; '.join(asset.description for asset in assets)
        test_case = test_case_model(id=test_case_id,
                                    name="what " + key[1] + " " + key[0],
                                    description=descriptions,
                                    test_env="ci",
                                    components=["ars"],
                                    test_case_objective="AcceptanceTest",
                                    test_assets=assets,
                                    test_case_runner_settings=["inferred"]
                                    )
        if test_case.test_assets is None:
            print("test case has no assets", test_case)

        if test_case.test_case_objective == "AcceptanceTest":
            test_input_id = ""
            test_case_predicate_name = ""
            for asset in assets:
                test_input_id = asset.input_id
                test_case_predicate_name = asset.predicate_name

            test_case.test_case_input_id = test_input_id
            test_case.test_case_predicate_name = test_case_predicate_name
            test_case.test_case_predicate_id = "biolink:" + test_case_predicate_name
            test_cases.append(test_case)

    return test_cases


def create_test_suite_from_test_cases(test_cases, test_suite_model):
    test_suite_id = "TestSuite_1"
    test_cases_dict = {test_case.id: test_case for test_case in test_cases}
    tmd = TestMetadata(id=1,
                          test_source="SMURF",
                          test_objective="AcceptanceTest")
    return test_suite_model(id=test_suite_id, test_cases=test_cases_dict, test_metadata=tmd)


if __name__ == '__main__':

    # Reading the TSV file
    tsv_file_path = 'pf_test_assets_031524.tsv'
    tsv_data = parse_tsv(tsv_file_path)
    print(tsv_data[0])

    # Create TestAsset objects
    test_assets = create_test_assets_from_tsv(tsv_data)
    for asset in test_assets:
        if asset.test_metadata is None or asset.test_metadata == "":
            print(asset)

    # Create TestCase objects
    test_cases = create_test_cases_from_test_assets(test_assets, TestCase)
    for case in test_cases:
        if case.test_assets is None or case.test_assets == "":
            print(case)
    #

    for i, item in enumerate(test_cases):
        file_prefix = item.id
        filename = f"{file_prefix}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(item.dict(), file, ensure_ascii=False, indent=4)

    for i, item in enumerate(test_assets):
        file_prefix = item.id
        filename = f"{file_prefix}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(item.dict(), file, ensure_ascii=False, indent=4)

    url = 'https://raw.githubusercontent.com/TranslatorSRI/Benchmarks/main/benchmarks_runner/config/benchmarks.json'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        for k, v in data.items():
            tmd = TestMetadata(id=1,
                               test_source="SMURF",
                               test_objective="QuantitativeTest")
            ta = TestAsset(id=k,
                            name=k,
                            description=k,
                            test_metadata=tmd
                            )
            tc = TestCase(id=k,
                          name=k,
                          description=k,
                          test_assets=[ta],
                          test_env="ci",
                          components=["ars"],
                          test_case_objective="QuantitativeTest",
                          test_case_runner_settings=["limit_queries"]
                          )
            file_prefix = k
            if k.startswith("DrugCentral_subset"):
                test_cases.append(tc)
            filename = f"{file_prefix}.json"
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(tc.dict(), file, ensure_ascii=False, indent=4)

    else:
        print(f'Failed to retrieve the file. Status code: {response.status_code}')

    # Assemble into a TestSuite
    test_suite = create_test_suite_from_test_cases(test_cases, TestSuite)
    #
    # Convert to JSON and save to file
    test_suite_json = test_suite.json(indent=4)

    suite_json_output_path = 'test_suite_output.json'

    with open(suite_json_output_path, 'w') as file:
        file.write(test_suite_json)
