class ObjectiveDefined:
    def __init__(self, objective_id, objective_name, objective_description):
        self.objective_id = objective_id
        self.objective_name = objective_name
        self.objective_description = objective_description

    def to_dict(self):
        return {
            "objective_id": self.objective_id,
            "objective_name": self.objective_name,
            "objective_description": self.objective_description
        }