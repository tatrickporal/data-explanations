class Explanation:
    def __init__(self):
        self.original_template = "A Cohort was sampled by querying the{datasource} by{dataQueryVariables}. Additional metrics  {deltaQueryDelta} were extracted from {deltaQueryDeltaLocations}. This query resulted in {numberSetsReturned} {fileFormat} datasets out of {totalSets} datasets available in the catalog. {numberSetsReturned} {fileFormat} datasets were used as the input collection to the {workflowName}. Additional required parameters {workflowParameters} were mapped to the values {workflowValues}. The optional parameters {optionalParametersNotUsed} were not used in the workflow. The workflow resulted in a p value of {p_value}."
        self.working_template = self.original_template