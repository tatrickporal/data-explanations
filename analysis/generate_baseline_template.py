from Explanation import Explanation

def generate_baseline_template(project_results_list):
    explanation = Explanation()
    working_template = explanation.original_template
    add_data_source_to_template("",working_template)
    working_template = add_data_query_variables(project_results_list,working_template)
    return working_template


def add_p_value(p_value, working_template):
    return working_template.replace("{p_value}"," [" + str(p_value) + "] ")

def add_data_source_to_template(datasource,working_template):
    pass

def add_data_query_variables(project_results_list, working_template):
    string = ""
    i = 0
    while i < len(project_results_list):
        results = project_results_list[i]
        sanitized_query = results[1].replace("?","").replace("prop","").replace("Prop","")
        sanitized_parameter = results[2].replace("?","")
        and_string = ""
        comma = ""
        if i == len(project_results_list) - 1:
            and_string = "and "
        else :
            comma = ","
        string+= " " + and_string + sanitized_query + " = " + sanitized_parameter + comma
        i+=1
    return working_template.replace("{dataQueryVariables}"," [" + string + "] ")
