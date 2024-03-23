import abc
import torch

from RLFramework.RLTrainer import RLTrainer
from RLFramework.Network import Network
from RLFramework.Environment import Environment
from RLFramework.Agent import Agent


class QActorCriticTrainer(RLTrainer):
    def __init__(self, policy_net: Network, q_net: Network, environment: Environment, agent: Agent,
                 alpha=1, gamma=1, epsilon=1e-5, grad_clip=None):
        """
        :param gamma: Discount factor of Reward
        :param epsilon: Small value that is added for log calculation.
        :param grad_clip: Gradient Clipping norm magnitude.
        """
        super().__init__(environment=environment, agent=agent)

        self.policy_net = policy_net
        self.q_net = q_net
        self.alpha = alpha
        self.gamma = gamma
        self.eps = epsilon
        self.grad_clip = grad_clip

    def train(self, state, action, reward, next_state):
        """
        :param state: Current state of an environment.
        :param action: Current action of an agent.
        :param reward: Current reward of current state-action set.
        :param next_state: Next state of an environment.
        :return A tuple of (policy loss, value loss) of the train step.
        Train by Q Actor-Critic method.
        Expect unbatched input.
        """

        pred_q = self.q_net.predict(state)

        if next_state is None:
            pred_next_q = torch.tensor([0])
        else:
            pred_next_action = torch.argmax(self.policy_net.predict(next_state))
            pred_next_q = self.q_net.predict(next_state)[pred_next_action]

        target_q = pred_q.cpu()
        target_q[action] = target_q[action] + self.alpha * (reward + self.gamma * pred_next_q - target_q[action])

        policy_loss_function = lambda p, t: -torch.log(p[action]) * t[action]
        value_loss_function = lambda p, t: torch.pow(torch.norm(p - t), 2) / 2

        policy_loss = self.policy_net.train_batch(state, target_q, loss_function=policy_loss_function, clip=self.grad_clip)
        q_loss = self.q_net.train_batch(state, target_q, loss_function=value_loss_function, clip=self.grad_clip)

        return policy_loss, q_loss

    def check_train(self):
        return True

    @abc.abstractmethod
    def check_reset(self):
        """
        :return: Bool value for whether to reset an Environment.
        """
        pass

    @abc.abstractmethod
    def reset_params(self):
        pass
