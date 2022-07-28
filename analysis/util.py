import json
import re

def retrieve_project_results_triples(data_query):
    project_results_triple = []
    project_results_dict = {}
    for statement in data_query:
        if "?ProjectResults" in statement:
            triple = statement.split()
            if triple[0] == "?ProjectResults":
                criteria = triple[1].replace("?","").replace("prop","")
                project_results_dict[criteria] = statement
                project_results_triple.append(triple)
    return project_results_triple

def load_loi_tloi_json():
    tloi_json_file = open("./examples/1-example/TriggeredLOI-2RF28NkrEBea.json")
    loi_json_file = open("./examples/1-example/LOI-wLTSfEcLyeY8.json")
    ret = {}
    ret["tloi"] = json.load(tloi_json_file)
    ret["loi"] = json.load(loi_json_file)
    return ret

def load_loi_tloi_list():
    tloi_json_file = open("./examples/1-example/tlois.json")
    loi_json_file = open("./examples/1-example/lois.json")
    ret = {}
    ret["tloi"] = json.load(tloi_json_file)
    ret["loi"] = json.load(loi_json_file)
    return ret

def extract_hypothesis_variable_bindings_from_loi(loi_json):
    workflows = loi_json["workflows"]
    parameters = []
    if workflows is not None:
        for workflow in workflows:
            parameters += workflow["parameters"]
    return parameters

def insert_space(string):
    return re.sub(r"(?<=\w)([A-Z])", r" \1", string)

def find_loi_from_id(id,list):
    for loi in list:
        if id == loi["id"]:
            return loi
