from generate_baseline_template import *
import json
from util import *

def main():
    json_dict = load_loi_tloi_list()
    tloi_list = json_dict["tloi"]
    loi_list = json_dict["loi"]
    
    for i in range(len(tloi_list)):
        print("\n <---------- \n")
        tloi = tloi_list[i]
        loi_id = tloi["loiId"]
        loi = find_loi_from_id(loi_id,loi_list)
        if "dataQuery" in tloi and tloi["dataQuery"] is not None:
                data_query = tloi["dataQuery"]
                project_results_triple_dict = retrieve_project_results_triples(data_query.replace("\n","").split("."))
                # hypothesis_variable_bindings_list = extract_hypothesis_variable_bindings_from_loi(loi)
                explanation = generate_baseline_template(project_results_triple_dict)
                explanation = add_p_value(tloi["confidenceValue"],explanation)
                print(explanation)
    print("\n ----------> \n")



if __name__ == "__main__":
    main()