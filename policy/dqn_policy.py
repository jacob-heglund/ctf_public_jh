"""Random agents policy generator.

This module demonstrates an example of a simple heuristic policy generator
for Capture the Flag environment.
    http://github.com/osipychev/missionplanner/

DOs/Denis Osipychev
    http://www.denisos.com
"""

class PolicyGen:
    """Policy generator class for CtF env.

    This class can be used as a template for policy generator.
    Designed to summon an AI logic for the team of units.

    Methods:
        gen_action: Required method to generate a list of actions.
    """
    #TODO modify to take a hyperparameter dict
    def __init__(self, free_map, agent_list):
        model = ModelClass()
        model.load_state_dict(torch.load(state_dict_path))


    def gen_action(self, agent_list, observation, free_map=None):
        """Action generation method.

        This is a required method that passes a list of
        actions generated by the policy to the environment.
        """
        action_list = []

        for i in len(agent_list):
            #TODO print observationt omake sure it is the right thing
            state = observation

            if np.random.rand(1) < epsilon:
                q_values = self.online_model(state)
                action = env.action_space.sample()

            else:
                q_values = self.online_model(state)
                _, action = torch.max(q_values, 1)
                action = action.item()

            return action, q_values

            action =
        return action_list