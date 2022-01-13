class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, n_customer):
        if n_customer not in self.customers:
            self.customers.append(n_customer)

    def add_trainer(self, n_trainer):
        if n_trainer not in self.trainers:
            self.trainers.append(n_trainer)

    def add_equipment(self, n_equipment):
        if n_equipment not in self.equipment:
            self.equipment.append(n_equipment)

    def add_plan(self, n_plan):
        if n_plan not in self.plans:
            self.plans.append(n_plan)

    def add_subscription(self, n_subscription):
        if n_subscription not in self.subscriptions:
            self.subscriptions.append(n_subscription)

    def subscription_info(self, subscription_id):
        current_sub = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == current_sub.customer_id][0]
        trainer = [t for t in self.trainers if t.id == current_sub.trainer_id][0]
        plan = [p for p in self.plans if p.trainer_id == trainer.id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]

        return f'{current_sub}\n{customer}\n{trainer}\n{equipment}\n{plan}'
