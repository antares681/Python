from Ex04_Gym.equipment import Equipment
from Ex04_Gym.customer import Customer
from Ex04_Gym.trainer import Trainer
from Ex04_Gym.subscription import Subscription
from Ex04_Gym.exercise_plan import ExercisePlan

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer:Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer:Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment:Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan:ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription:Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sbs = [subscription for subscription in self.subscriptions if subscription.id == subscription_id][0]
        cst = [customer for customer in self.customers if customer.id == subscription_id][0]
        trn = [trainer for trainer in self.trainers if trainer.id == subscription_id][0]
        pln = [plan for plan in self.plans if plan.id == subscription_id][0]
        eqp = [eqp for eqp in self.equipment if eqp.id == subscription_id][0]
        return f'{sbs}\n{cst}\n{trn}\n{eqp}\n{pln}'

